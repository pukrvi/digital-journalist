#!/usr/bin/env python3
"""LangSearch — free, LLM-oriented web search. Key recommended but anonymous works.
https://langsearch.com

CLI:
    langsearch.py "<query>" [--count 10] [--summary] [--json]
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print


NAME = "langsearch"
ENDPOINT = "https://api.langsearch.com/v1/web-search"


def search(query: str, count: int = 10, summary: bool = False, timeout: int = 30) -> dict:
    key = get_key(NAME)
    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = f"Bearer {key}"
    payload = {"query": query, "count": count, "freshness": "noLimit", "summary": bool(summary)}
    try:
        resp = requests.post(ENDPOINT, json=payload, headers=headers, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    items = (data.get("data") or {}).get("webPages", {}).get("value") or data.get("results", []) or []
    results = [{
        "title":   it.get("name") or it.get("title", ""),
        "url":     it.get("url", ""),
        "snippet": it.get("snippet") or it.get("summary", ""),
        "date":    it.get("datePublished"),
    } for it in items[:count]]
    ai_summary = (data.get("data") or {}).get("summary") or data.get("summary")
    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=ai_summary)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query"); ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--summary", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cli_print(search(a.query, a.count, summary=a.summary), compact=not a.json)


if __name__ == "__main__":
    main()
