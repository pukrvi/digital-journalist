#!/usr/bin/env python3
"""NewsAPI.org — news search across 150k+ sources. Free tier: 100/day.
Note: free tier limits results to articles ≥24h old.

CLI:
    newsapi.py "<query>" [--count 20] [--from 2026-05-01] [--lang en] [--json]
    newsapi.py top [--country us] [--category business]
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "newsapi"
BASE = "https://newsapi.org/v2"


def everything(query: str, count: int = 20, frm: str | None = None, language: str = "en", timeout: int = 30) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No NEWSAPI_API_KEY in keys.env. Sign up: https://newsapi.org")
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="newsapi daily limit reached")
    params = {"q": query, "pageSize": min(count, 100), "language": language, "apiKey": key, "sortBy": "publishedAt"}
    if frm:
        params["from"] = frm
    try:
        resp = requests.get(f"{BASE}/everything", params=params, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))
    if data.get("status") != "ok":
        return normalize_result(NAME, query, error=data.get("message", "newsapi error"))
    items = data.get("articles", [])
    results = [{
        "title":   it.get("title", ""),
        "url":     it.get("url", ""),
        "snippet": it.get("description", "") or it.get("content", ""),
        "date":    it.get("publishedAt"),
        "extra":   {"source": (it.get("source") or {}).get("name"), "author": it.get("author")},
    } for it in items[:count]]
    increment_usage(NAME)
    return normalize_result(NAME, query, results)


def top(country: str = "us", category: str | None = None, count: int = 10, timeout: int = 30) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, "top-headlines", error="No NEWSAPI_API_KEY")
    if not check_limit(NAME):
        return normalize_result(NAME, "top-headlines", error="newsapi daily limit reached")
    params = {"country": country, "pageSize": count, "apiKey": key}
    if category:
        params["category"] = category
    try:
        resp = requests.get(f"{BASE}/top-headlines", params=params, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, "top-headlines", error=str(e))
    results = [{
        "title":   it.get("title", ""),
        "url":     it.get("url", ""),
        "snippet": it.get("description", ""),
        "date":    it.get("publishedAt"),
    } for it in data.get("articles", [])[:count]]
    increment_usage(NAME)
    return normalize_result(NAME, f"top-{country}-{category or ''}", results)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd")
    e = sub.add_parser("everything"); e.add_argument("query"); e.add_argument("--count", type=int, default=20)
    e.add_argument("--from", dest="frm"); e.add_argument("--lang", default="en")
    t = sub.add_parser("top"); t.add_argument("--country", default="us"); t.add_argument("--category"); t.add_argument("--count", type=int, default=10)
    # Allow bare query for convenience
    ap.add_argument("query", nargs="?")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.cmd == "top":
        r = top(a.country, a.category, a.count)
    else:
        q = a.query or (getattr(a, "query", None))
        if not q:
            ap.error("query required")
        r = everything(q, a.count if hasattr(a, "count") else 20, frm=getattr(a, "frm", None), language=getattr(a, "lang", "en"))
    cli_print(r, compact=not a.json)


if __name__ == "__main__":
    main()
