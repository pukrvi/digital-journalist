#!/usr/bin/env python3
"""Google Programmable Search (Custom Search JSON API). Free tier: 100/day.

Requires BOTH a Google API key AND a Custom Search Engine ID (CX).
Setup: https://programmablesearchengine.google.com → create engine (search whole web)
       https://console.cloud.google.com → enable Custom Search JSON API → create key

CLI:
    google_cse.py "<query>" [--count 10] [--site example.com]
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "google_cse"
ENDPOINT = "https://customsearch.googleapis.com/customsearch/v1"


def search(query: str, count: int = 10, site: str | None = None, timeout: int = 30) -> dict:
    creds = get_key(NAME)
    if not creds or not isinstance(creds, tuple):
        return normalize_result(NAME, query, error="Need both GOOGLE_CSE_API_KEY and GOOGLE_CSE_CX in keys.env")
    api_key, cx = creds
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="google_cse daily limit (100) reached")
    q = f"{query} site:{site}" if site else query
    # CSE caps num at 10; loop for more
    all_items = []
    for start in range(1, count + 1, 10):
        params = {"q": q, "key": api_key, "cx": cx, "num": min(10, count - len(all_items)), "start": start}
        try:
            resp = requests.get(ENDPOINT, params=params, timeout=timeout)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            return normalize_result(NAME, query, error=str(e))
        all_items.extend(data.get("items", []))
        if len(all_items) >= count or len(data.get("items", [])) < 10:
            break
    results = [{
        "title":   it.get("title", ""),
        "url":     it.get("link", ""),
        "snippet": it.get("snippet", ""),
        "date":    it.get("pagemap", {}).get("metatags", [{}])[0].get("article:published_time"),
    } for it in all_items[:count]]
    increment_usage(NAME)
    return normalize_result(NAME, query, results)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query"); ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--site", help="restrict to a domain")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cli_print(search(a.query, a.count, site=a.site), compact=not a.json)


if __name__ == "__main__":
    main()
