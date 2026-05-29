"""Shared helpers for every search provider script.

- load_keys(): read tools/api/keys.env (if present) into os.environ. Safe to call multiple times.
- get_key(NAME): return the API key for a provider, or None.
- has_key(NAME): bool helper.
- check_limit(NAME): bool — within the configured free-tier limit?
- increment_usage(NAME): atomic counter bump in usage.json.
- get_usage(NAME): return {"used": int, "limit": int|None, "remaining": int|None, "period": str}.
- normalize_result(...): produce the unified result shape every provider returns.
- KEY_FOR / LIMITS / TIERS: dicts loaded from limits.json.
"""
from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


HERE = Path(__file__).resolve().parent
KEYS_FILE = HERE / "keys.env"
LIMITS_FILE = HERE / "limits.json"
USAGE_FILE = HERE / "usage.json"

# Provider name → env var(s)
KEY_FOR = {
    "duckduckgo":       None,
    "jina_reader":      "JINA_API_KEY",     # optional
    "langsearch":       "LANGSEARCH_API_KEY",  # optional
    "brave":            "BRAVE_API_KEY",
    "tavily":           "TAVILY_API_KEY",
    "serper":           "SERPER_API_KEY",
    "serpapi":          "SERPAPI_API_KEY",
    "exa":              "EXA_API_KEY",
    "firecrawl":        "FIRECRAWL_API_KEY",
    "google_cse":       ("GOOGLE_CSE_API_KEY", "GOOGLE_CSE_CX"),
    "you_com":          "YOU_API_KEY",
    "newsapi":          "NEWSAPI_API_KEY",
    "gemini":           "GEMINI_API_KEY",
    "cohere":           "COHERE_API_KEY",
    "perplexity":       "PERPLEXITY_API_KEY",
    "openai_search":    "OPENAI_API_KEY",
    "anthropic_search": "ANTHROPIC_API_KEY",
    "xai_grok":         "XAI_API_KEY",
}

OPTIONAL_KEY = {"jina_reader", "langsearch"}  # work without a key, key just lifts quota


def load_keys(env_file: Path = KEYS_FILE) -> None:
    """Read KEY=VALUE lines into os.environ. Lines starting with # are ignored."""
    if not env_file.exists():
        return
    for raw in env_file.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if value and key not in os.environ:
            os.environ[key] = value


load_keys()


def _load_limits() -> Dict[str, Dict[str, Any]]:
    try:
        return json.loads(LIMITS_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


LIMITS = _load_limits()


def get_key(provider: str) -> Optional[str] | tuple:
    name = KEY_FOR.get(provider)
    if name is None:
        return ""  # keyless
    if isinstance(name, tuple):
        vals = tuple(os.environ.get(n, "").strip() for n in name)
        return vals if all(vals) else None
    return os.environ.get(name, "").strip() or None


def has_key(provider: str) -> bool:
    if provider not in KEY_FOR:
        return False
    if KEY_FOR[provider] is None:
        return True  # keyless
    key = get_key(provider)
    if isinstance(key, tuple):
        return all(key)
    return bool(key)


def _period_token(period: str) -> str:
    now = datetime.now(timezone.utc)
    if period == "day":
        return now.strftime("%Y-%m-%d")
    if period == "month":
        return now.strftime("%Y-%m")
    return "all-time"


def _load_usage() -> Dict[str, Any]:
    if not USAGE_FILE.exists():
        return {}
    try:
        return json.loads(USAGE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_usage(data: Dict[str, Any]) -> None:
    USAGE_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def get_usage(provider: str) -> Dict[str, Any]:
    info = LIMITS.get(provider, {})
    period = info.get("period", "month")
    token = _period_token(period)
    usage = _load_usage().get(provider, {})
    used = usage.get(token, 0)
    limit = info.get("limit")
    remaining = None if limit is None else max(0, limit - used)
    return {"period": period, "period_token": token, "used": used, "limit": limit, "remaining": remaining, "tier": info.get("tier")}


def check_limit(provider: str) -> bool:
    """True if a call to this provider would stay within its free-tier limit."""
    u = get_usage(provider)
    if u["limit"] is None:
        return True
    return u["remaining"] > 0


def increment_usage(provider: str, n: int = 1) -> None:
    info = LIMITS.get(provider, {})
    period = info.get("period", "month")
    token = _period_token(period)
    data = _load_usage()
    bucket = data.setdefault(provider, {})
    bucket[token] = bucket.get(token, 0) + n
    bucket["_last_used"] = datetime.now(timezone.utc).isoformat()
    _save_usage(data)


def normalize_result(
    provider: str,
    query: str,
    results: List[Dict[str, Any]] | None = None,
    ai_summary: Optional[str] = None,
    error: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Unified result shape returned by every provider."""
    out_results = []
    for r in (results or []):
        out_results.append({
            "title":   r.get("title") or r.get("name") or "",
            "url":     r.get("url") or r.get("link") or r.get("href") or "",
            "snippet": r.get("snippet") or r.get("description") or r.get("content") or r.get("body") or "",
            "date":    r.get("date") or r.get("published") or r.get("publishedAt") or None,
            "score":   r.get("score") or r.get("relevance"),
            "extra":   r.get("extra"),
        })
    return {
        "provider": provider,
        "tier": LIMITS.get(provider, {}).get("tier"),
        "query": query,
        "ok": error is None,
        "error": error,
        "ai_summary": ai_summary,
        "results": out_results,
        "extra": extra or {},
        "usage_after": get_usage(provider),
    }


def cli_print(result: Dict[str, Any], compact: bool = False) -> None:
    if compact:
        print(f"[{result['provider']}] {len(result['results'])} results", file=sys.stderr)
        if result.get("error"):
            print(f"  ERROR: {result['error']}", file=sys.stderr)
        if result.get("ai_summary"):
            print(f"\n--- AI Summary ---\n{result['ai_summary']}\n")
        for i, r in enumerate(result["results"], 1):
            print(f"{i:2d}. {r['title']}\n    {r['url']}\n    {r['snippet'][:200]}\n")
    else:
        print(json.dumps(result, indent=2, default=str))
