#!/usr/bin/env python3
"""You.com Search API. Free tier: 100/day.

CLI:
    you_com.py search "<query>" [--count 10]
    you_com.py news "<query>" [--count 10]
    you_com.py rag "<query>"                 # LLM-Search endpoint with answer
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "you_com"
BASE = "https://chat-api.you.com"


def _h(key):
    return {"X-API-Key": key}


def _search(endpoint: str, query: str, count: int, key: str, timeout: int = 30) -> dict:
    try:
        resp = requests.get(f"{BASE}/{endpoint}", params={"query": query, "num_web_results": count}, headers=_h(key), timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        return {"_error": str(e)}


def search(query: str, count: int = 10) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No YOU_API_KEY in keys.env. Sign up: https://api.you.com")
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="you.com daily limit reached")
    data = _search("search", query, count, key)
    if "_error" in data:
        return normalize_result(NAME, query, error=data["_error"])
    items = data.get("hits", [])
    results = [{
        "title":   it.get("title", ""),
        "url":     it.get("url", ""),
        "snippet": " ".join(it.get("snippets", [])[:2])[:500],
        "date":    it.get("published"),
    } for it in items[:count]]
    increment_usage(NAME)
    return normalize_result(NAME, query, results)


def rag(query: str) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No YOU_API_KEY in keys.env")
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="you.com daily limit reached")
    data = _search("rag", query, 10, key)
    if "_error" in data:
        return normalize_result(NAME, query, error=data["_error"])
    answer = data.get("answer") or data.get("response")
    items = data.get("hits") or data.get("search_results", [])
    results = [{
        "title":   it.get("title", ""),
        "url":     it.get("url", ""),
        "snippet": " ".join(it.get("snippets", [])[:2])[:500] if isinstance(it.get("snippets"), list) else it.get("snippet", ""),
    } for it in items[:10]]
    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=answer)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--count", type=int, default=10)
    n = sub.add_parser("news"); n.add_argument("query"); n.add_argument("--count", type=int, default=10)
    r = sub.add_parser("rag"); r.add_argument("query")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.cmd == "rag":
        res = rag(a.query)
    else:
        res = search(a.query, a.count)
    cli_print(res, compact=not a.json)


if __name__ == "__main__":
    main()
