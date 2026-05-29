#!/usr/bin/env python3
"""SerpApi — Google SERP. Free tier: 100 searches/month.

CLI:
    serpapi.py "<query>" [--count 10] [--engine google|google_news|google_scholar] [--json]
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "serpapi"


def search(query: str, count: int = 10, engine: str = "google", timeout: int = 30) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No SERPAPI_API_KEY in keys.env. Sign up: https://serpapi.com")
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="serpapi free-tier limit reached this month")

    params = {"q": query, "api_key": key, "num": count, "engine": engine}
    try:
        resp = requests.get("https://serpapi.com/search.json", params=params, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    key_for_items = {
        "google": "organic_results",
        "google_news": "news_results",
        "google_scholar": "organic_results",
    }.get(engine, "organic_results")

    items = data.get(key_for_items, []) or []
    results = [{
        "title":   it.get("title", ""),
        "url":     it.get("link", ""),
        "snippet": it.get("snippet") or it.get("publication_info", {}).get("summary", ""),
        "date":    it.get("date") or it.get("publication_info", {}).get("summary"),
        "score":   it.get("position"),
    } for it in items[:count]]

    ai_summary = (data.get("answer_box") or {}).get("answer") or (data.get("answer_box") or {}).get("snippet")
    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=ai_summary)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query"); ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--engine", default="google", choices=["google", "google_news", "google_scholar"])
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cli_print(search(a.query, a.count, engine=a.engine), compact=not a.json)


if __name__ == "__main__":
    main()
