#!/usr/bin/env python3
"""DuckDuckGo search — keyless, unlimited (subject to bot throttling).

CLI:
    ddg.py "<query>" [--count 10] [--news] [--json]
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, cli_print


NAME = "duckduckgo"


def search(query: str, count: int = 10, mode: str = "text") -> dict:
    try:
        from ddgs import DDGS
    except Exception as e:
        return normalize_result(NAME, query, error=f"ddgs not installed: {e}")
    try:
        with DDGS() as ddgs:
            if mode == "news":
                raw = list(ddgs.news(query, max_results=count))
            else:
                raw = list(ddgs.text(query, max_results=count))
        results = [{
            "title": r.get("title", ""),
            "url":   r.get("href") or r.get("url", ""),
            "snippet": r.get("body") or r.get("excerpt", ""),
            "date":  r.get("date"),
        } for r in raw]
        increment_usage(NAME, len(results))
        return normalize_result(NAME, query, results)
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query")
    ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--news", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    r = search(a.query, a.count, mode="news" if a.news else "text")
    cli_print(r, compact=not a.json)


if __name__ == "__main__":
    main()
