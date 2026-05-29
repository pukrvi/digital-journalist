#!/usr/bin/env python3
"""Firecrawl — LLM-ready search + scrape. Free tier: 500-1000 credits/month.

CLI:
    firecrawl.py search "<query>" [--count 10]
    firecrawl.py scrape <url> [--format markdown|html|json]
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "firecrawl"
BASE = "https://api.firecrawl.dev/v1"


def _h(key):
    return {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}


def search(query: str, count: int = 10, timeout: int = 45) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No FIRECRAWL_API_KEY in keys.env. Sign up: https://firecrawl.dev")
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="firecrawl credits exhausted")
    try:
        resp = requests.post(f"{BASE}/search", json={"query": query, "limit": count}, headers=_h(key), timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    items = data.get("data") or data.get("results") or []
    results = [{
        "title":   it.get("title", ""),
        "url":     it.get("url", ""),
        "snippet": (it.get("description") or it.get("markdown") or "")[:500],
        "date":    it.get("publishedDate") or it.get("metadata", {}).get("publishedTime"),
    } for it in items[:count]]
    increment_usage(NAME)
    return normalize_result(NAME, query, results)


def scrape(url: str, fmt: str = "markdown", timeout: int = 60) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, url, error="No FIRECRAWL_API_KEY")
    payload = {"url": url, "formats": [fmt]}
    try:
        resp = requests.post(f"{BASE}/scrape", json=payload, headers=_h(key), timeout=timeout)
        resp.raise_for_status()
        data = resp.json().get("data", {})
    except Exception as e:
        return normalize_result(NAME, url, error=str(e))
    body = data.get(fmt) or data.get("markdown") or ""
    increment_usage(NAME)
    return normalize_result(NAME, url, [{
        "title":   data.get("metadata", {}).get("title", url),
        "url":     url,
        "snippet": body,
        "date":    data.get("metadata", {}).get("publishedTime"),
    }])


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--count", type=int, default=10)
    sc = sub.add_parser("scrape"); sc.add_argument("url"); sc.add_argument("--format", dest="fmt", default="markdown")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    r = search(a.query, a.count) if a.cmd == "search" else scrape(a.url, a.fmt)
    cli_print(r, compact=not a.json)


if __name__ == "__main__":
    main()
