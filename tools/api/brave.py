#!/usr/bin/env python3
"""Brave Search API. Free tier: 2,000 queries/month.

Endpoints:
  /web/search        — standard SERP
  /summarizer/search — AI summary (requires summary=1 on first call to mint a key)

CLI:
    brave.py "<query>" [--count 10] [--summary] [--news] [--json]
"""
from __future__ import annotations

import argparse
import os
import sys
import time

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "brave"
WEB = "https://api.search.brave.com/res/v1/web/search"
NEWS = "https://api.search.brave.com/res/v1/news/search"
SUMM = "https://api.search.brave.com/res/v1/summarizer/search"


def _headers(key):
    return {"Accept": "application/json", "X-Subscription-Token": key}


def search(query: str, count: int = 10, with_summary: bool = False, news: bool = False, timeout: int = 30) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No BRAVE_API_KEY in keys.env. Sign up: https://brave.com/search/api/")
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="brave free-tier limit reached this month")

    endpoint = NEWS if news else WEB
    params = {"q": query, "count": min(count, 20)}
    if with_summary and not news:
        params["summary"] = 1

    try:
        resp = requests.get(endpoint, headers=_headers(key), params=params, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    items = (data.get("web") or data.get("news") or {}).get("results", [])
    results = [{
        "title":   it.get("title", ""),
        "url":     it.get("url", ""),
        "snippet": it.get("description", ""),
        "date":    it.get("age") or it.get("page_age"),
    } for it in items[:count]]

    ai_summary = None
    summarizer_key = (data.get("summarizer") or {}).get("key")
    if with_summary and summarizer_key:
        try:
            time.sleep(0.4)  # summarizer endpoint is async; brief poll
            sresp = requests.get(SUMM, headers=_headers(key), params={"key": summarizer_key}, timeout=timeout)
            if sresp.ok:
                sdata = sresp.json()
                blocks = sdata.get("summary") or []
                if isinstance(blocks, list) and blocks:
                    ai_summary = "\n".join(b.get("text", "") for b in blocks if isinstance(b, dict)) or None
        except Exception as e:
            ai_summary = f"(summary failed: {e})"

    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=ai_summary)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query")
    ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--news", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    r = search(a.query, a.count, with_summary=a.summary, news=a.news)
    cli_print(r, compact=not a.json)


if __name__ == "__main__":
    main()
