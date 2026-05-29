#!/usr/bin/env python3
"""Ping every search provider with a small query. Reports which work, which need keys.

Usage:
    ping.py                           # tests all providers
    ping.py --include-paid            # also tests paid (requires ALLOW_PAID or keys)
    ping.py --query "OpenAI o1 model" # custom test query
    ping.py --json
"""
from __future__ import annotations

import argparse
import importlib
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import LIMITS, has_key, KEY_FOR, OPTIONAL_KEY


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


def _tier(p):
    return (LIMITS.get(p) or {}).get("tier") or "unknown"


def _ping_one(name, query):
    tier = _tier(name)
    needs = KEY_FOR.get(name)
    if needs is not None and name not in OPTIONAL_KEY and not has_key(name):
        return {"provider": name, "tier": tier, "status": "NO_KEY", "ok": False, "elapsed_ms": 0, "results": 0, "error": None, "note": "Add key to keys.env"}
    if tier == "paid" and os.environ.get("ALLOW_PAID", "0") not in ("1", "true", "yes"):
        return {"provider": name, "tier": tier, "status": "PAID_DISABLED", "ok": False, "elapsed_ms": 0, "results": 0, "error": None, "note": "Set ALLOW_PAID=1 in keys.env or pass --include-paid"}
    mod_name, fn_name = PROVIDERS[name]
    try:
        mod = importlib.import_module(mod_name)
        fn = getattr(mod, fn_name)
    except Exception as e:
        return {"provider": name, "tier": tier, "status": "IMPORT_ERROR", "ok": False, "elapsed_ms": 0, "results": 0, "error": str(e), "note": ""}
    t0 = time.time()
    try:
        # All provider .search functions accept (query, count=...) but some take different first kwargs.
        try:
            res = fn(query, 3)
        except TypeError:
            res = fn(query)
    except Exception as e:
        return {"provider": name, "tier": tier, "status": "EXCEPTION", "ok": False, "elapsed_ms": int((time.time() - t0) * 1000), "results": 0, "error": str(e)[:200], "note": ""}
    dt = int((time.time() - t0) * 1000)
    if res.get("ok"):
        return {"provider": name, "tier": tier, "status": "OK", "ok": True, "elapsed_ms": dt,
                "results": len(res.get("results", [])), "ai_summary": bool(res.get("ai_summary")), "error": None, "note": ""}
    return {"provider": name, "tier": tier, "status": "ERROR", "ok": False, "elapsed_ms": dt,
            "results": 0, "error": (res.get("error") or "")[:200], "note": ""}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--query", default="OpenAI GPT-5 release date")
    ap.add_argument("--include-paid", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--parallel", type=int, default=6)
    a = ap.parse_args()
    if a.include_paid:
        os.environ["ALLOW_PAID"] = "1"

    targets = list(PROVIDERS.keys())
    results = []
    with ThreadPoolExecutor(max_workers=a.parallel) as ex:
        futs = {ex.submit(_ping_one, p, a.query): p for p in targets}
        for f in as_completed(futs):
            results.append(f.result())
    # preserve order
    results.sort(key=lambda r: list(PROVIDERS.keys()).index(r["provider"]))

    if a.json:
        print(json.dumps(results, indent=2))
        return

    print(f"\nPing query: {a.query}\n")
    print(f"{'PROVIDER':<20} {'TIER':<10} {'STATUS':<16} {'RES':<5} {'MS':<6} NOTE / ERROR")
    print("-" * 110)
    for r in results:
        note = r.get("error") or r.get("note") or ""
        ai = " +AI" if r.get("ai_summary") else ""
        print(f"{r['provider']:<20} {r['tier']:<10} {r['status']:<16} {r['results']:<5} {r['elapsed_ms']:<6} {note[:60]}{ai}")
    ok = [r for r in results if r["ok"]]
    no_key = [r for r in results if r["status"] == "NO_KEY"]
    failed = [r for r in results if r["status"] not in ("OK", "NO_KEY", "PAID_DISABLED")]
    print(f"\nSummary: {len(ok)} working, {len(no_key)} need keys, {len(failed)} errored.")
    if no_key:
        print("\nNeed keys:")
        for r in no_key:
            print(f"  - {r['provider']}  ({r['tier']} tier)")


if __name__ == "__main__":
    main()
