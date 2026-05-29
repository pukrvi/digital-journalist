#!/usr/bin/env python3
"""Tavily — AI-ready search aggregator. Free tier: 1,000 queries/month.

CLI:
    tavily.py "<query>" [--count 5] [--depth basic|advanced] [--answer] [--json]
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "tavily"
ENDPOINT = "https://api.tavily.com/search"


def search(query: str, count: int = 5, depth: str = "basic", include_answer: bool = True, timeout: int = 60) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No TAVILY_API_KEY in keys.env. Sign up: https://tavily.com")
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="tavily free-tier limit reached this month")

    payload = {
        "api_key": key,
        "query": query,
        "max_results": count,
        "search_depth": depth if depth in ("basic", "advanced") else "basic",
        "include_answer": include_answer,
    }
    try:
        resp = requests.post(ENDPOINT, json=payload, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    results = [{
        "title":   r.get("title", ""),
        "url":     r.get("url", ""),
        "snippet": r.get("content", ""),
        "score":   r.get("score"),
        "date":    r.get("published_date"),
    } for r in data.get("results", [])]

    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=data.get("answer"))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query")
    ap.add_argument("--count", type=int, default=5)
    ap.add_argument("--depth", choices=["basic", "advanced"], default="basic")
    ap.add_argument("--no-answer", action="store_true", help="skip AI-generated answer")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    r = search(a.query, a.count, depth=a.depth, include_answer=not a.no_answer)
    cli_print(r, compact=not a.json)


if __name__ == "__main__":
    main()
