#!/usr/bin/env python3
"""Unified search router.

Routing policy (boil-the-ocean):
  1. Fan out to every KEYLESS provider (always).
  2. Fan out to every FREE-TIER provider that has a key AND is within its limit.
  3. Touch PAID providers only when --paid is set AND ALLOW_PAID=1 in keys.env (or --force-paid).

CLI:
    search.py "<query>"                            # auto fan-out, free only
    search.py "<query>" --providers ddg,brave      # explicit list
    search.py "<query>" --tier keyless             # just keyless
    search.py "<query>" --tier free                # keyless + free
    search.py "<query>" --tier paid                # ALL tiers including paid (gated)
    search.py "<query>" --provider tavily          # one provider only
    search.py "<query>" --count 8                  # per-provider count
    search.py "<query>" --aggregate                # dedupe across providers
    search.py "<query>" --aggregate --json
    search.py --status                             # print available providers + usage
"""
from __future__ import annotations

import argparse
import importlib
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import LIMITS, has_key, check_limit, get_usage, KEY_FOR, OPTIONAL_KEY, cli_print


# Mapping: provider name → (module name, callable)
PROVIDERS = {
    "duckduckgo":       ("ddg",              "search"),
    "jina_reader":      ("jina",             "search"),
    "langsearch":       ("langsearch",       "search"),
    "brave":            ("brave",            "search"),
    "tavily":           ("tavily",           "search"),
    "serper":           ("serper",           "search"),
    "serpapi":          ("serpapi",          "search"),
    "exa":              ("exa",              "search"),
    "firecrawl":        ("firecrawl",        "search"),
    "google_cse":       ("google_cse",       "search"),
    "you_com":          ("you_com",          "search"),
    "newsapi":          ("newsapi",          "everything"),
    "gemini":           ("gemini",           "search"),
    "cohere":           ("cohere_search",    "search"),
    "perplexity":       ("perplexity",       "search"),
    "openai_search":    ("openai_search",    "search"),
    "anthropic_search": ("anthropic_search", "search"),
    "xai_grok":         ("xai_grok",         "search"),
}


def _tier(provider: str) -> str:
    return (LIMITS.get(provider) or {}).get("tier") or "unknown"


def _available(provider: str) -> tuple[bool, str]:
    """Return (usable, reason). usable=True means this provider can be called right now."""
    if provider not in PROVIDERS:
        return False, "unknown provider"
    tier = _tier(provider)
    if tier == "keyless":
        return True, "keyless"
    needs_key = KEY_FOR.get(provider)
    if needs_key is None or provider in OPTIONAL_KEY:
        return True, "keyless (optional key)"
    if not has_key(provider):
        return False, "no key"
    if tier == "free" and not check_limit(provider):
        return False, f"limit reached ({get_usage(provider)['used']}/{get_usage(provider)['limit']})"
    if tier == "paid":
        if os.environ.get("ALLOW_PAID", "0") not in ("1", "true", "yes"):
            return False, "paid (ALLOW_PAID=0)"
    return True, "ok"


def _call(provider: str, query: str, count: int) -> dict:
    mod_name, fn_name = PROVIDERS[provider]
    try:
        mod = importlib.import_module(mod_name)
        fn = getattr(mod, fn_name)
    except Exception as e:
        return {"provider": provider, "ok": False, "error": f"import: {e}", "results": []}
    try:
        # All provider functions take (query, count=...) as their two leading args
        return fn(query, count)
    except TypeError:
        # Some take different signatures (e.g. gemini.search(query, model))
        try:
            return fn(query)
        except Exception as e:
            return {"provider": provider, "ok": False, "error": str(e), "results": []}
    except Exception as e:
        return {"provider": provider, "ok": False, "error": str(e), "results": []}


def status() -> dict:
    rows = []
    for name in PROVIDERS:
        ok, reason = _available(name)
        usage = get_usage(name) if name in LIMITS else {}
        rows.append({
            "provider": name,
            "tier": _tier(name),
            "available": ok,
            "reason": reason,
            "has_key": has_key(name) if KEY_FOR.get(name) else "n/a",
            "usage": f"{usage.get('used', 0)}{'/' + str(usage['limit']) if usage.get('limit') else ''}",
            "best_for": (LIMITS.get(name) or {}).get("best_for", ""),
        })
    return {"providers": rows}


def _select_providers(tier_filter: str, explicit: list[str] | None, single: str | None) -> list[str]:
    if single:
        return [single]
    if explicit:
        return explicit
    if tier_filter == "keyless":
        return [p for p in PROVIDERS if _tier(p) == "keyless"]
    if tier_filter == "free":
        return [p for p in PROVIDERS if _tier(p) in ("keyless", "free")]
    if tier_filter == "paid":
        return list(PROVIDERS.keys())
    return [p for p in PROVIDERS if _tier(p) in ("keyless", "free")]  # default = free


def fan_out(query: str, providers: list[str], count: int = 8, parallel: int = 6) -> list[dict]:
    usable = []
    skipped = []
    for p in providers:
        ok, reason = _available(p)
        if ok:
            usable.append(p)
        else:
            skipped.append({"provider": p, "skipped": reason})
    results = []
    with ThreadPoolExecutor(max_workers=parallel) as ex:
        futs = {ex.submit(_call, p, query, count): p for p in usable}
        for f in as_completed(futs):
            results.append(f.result())
    return results + skipped


def aggregate(results: list[dict]) -> dict:
    """Dedupe by normalized URL across providers. Returns unified result."""
    seen = {}
    summaries = {}
    for r in results:
        if not isinstance(r.get("results"), list):
            continue
        if r.get("ai_summary"):
            summaries[r.get("provider")] = r["ai_summary"]
        for it in r["results"]:
            url = it.get("url", "")
            if not url:
                continue
            norm = urlparse(url).netloc.lower() + urlparse(url).path.rstrip("/")
            if norm not in seen:
                seen[norm] = {
                    **it,
                    "sources": [r.get("provider")],
                }
            else:
                if r.get("provider") not in seen[norm]["sources"]:
                    seen[norm]["sources"].append(r.get("provider"))
    # Sort by source-count desc (multi-provider agreement = signal)
    merged = sorted(seen.values(), key=lambda x: -len(x.get("sources", [])))
    return {
        "query": (results[0].get("query") if results else None),
        "providers_used": [r["provider"] for r in results if r.get("ok", False) and r.get("results")],
        "providers_failed": [{"provider": r["provider"], "error": r.get("error") or r.get("skipped")} for r in results if not r.get("results")],
        "unique_results": len(merged),
        "results": merged,
        "ai_summaries": summaries,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query", nargs="?")
    ap.add_argument("--provider", help="single provider")
    ap.add_argument("--providers", help="comma-separated list")
    ap.add_argument("--tier", default="free", choices=["keyless", "free", "paid"])
    ap.add_argument("--count", type=int, default=8)
    ap.add_argument("--aggregate", action="store_true", help="merge results across providers")
    ap.add_argument("--paid", action="store_true", help="include paid tier")
    ap.add_argument("--parallel", type=int, default=6)
    ap.add_argument("--status", action="store_true", help="show provider availability")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.status:
        st = status()
        if a.json:
            print(json.dumps(st, indent=2))
        else:
            print(f"{'PROVIDER':<20} {'TIER':<10} {'STATUS':<10} {'KEY':<6} {'USAGE':<12} REASON / BEST FOR")
            print("-" * 100)
            for row in st["providers"]:
                k = "✓" if row["has_key"] is True else ("-" if row["has_key"] is False else " ")
                status_mark = "OK" if row["available"] else "—"
                print(f"{row['provider']:<20} {row['tier']:<10} {status_mark:<10} {k:<6} {row['usage']:<12} {row['reason']:<22} {row['best_for']}")
        return

    if not a.query:
        ap.error("query required (or use --status)")

    if a.paid:
        a.tier = "paid"

    providers = _select_providers(a.tier, a.providers.split(",") if a.providers else None, a.provider)
    results = fan_out(a.query, providers, count=a.count, parallel=a.parallel)

    if a.aggregate or len(providers) > 1:
        agg = aggregate(results)
        if a.json:
            print(json.dumps(agg, indent=2, default=str))
        else:
            print(f"\nQuery: {agg['query']}")
            print(f"Used:  {', '.join(agg['providers_used']) or '(none)'}")
            if agg["providers_failed"]:
                print(f"Skipped/failed: {len(agg['providers_failed'])} ({', '.join(r['provider'] for r in agg['providers_failed'])})")
            print(f"Unique results: {agg['unique_results']}\n")
            for i, r in enumerate(agg["results"][:30], 1):
                sources = "+".join(r.get("sources", []))
                print(f"{i:2d}. [{sources}] {r['title']}\n    {r['url']}\n    {(r['snippet'] or '')[:200]}\n")
            for prov, summ in agg["ai_summaries"].items():
                print(f"\n--- AI summary [{prov}] ---\n{summ[:1500]}\n")
    else:
        for r in results:
            cli_print(r, compact=not a.json)


if __name__ == "__main__":
    main()
