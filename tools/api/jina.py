#!/usr/bin/env python3
"""Jina AI Reader — works keyless (low quota) or with JINA_API_KEY (higher quota).
Two modes:
  - read:   fetch URL → clean LLM-friendly markdown   (s.jina.ai/<URL>)
  - search: SERP-style results for a query             (s.jina.ai/?q=<query>)
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print


NAME = "jina_reader"


def _headers():
    key = get_key(NAME)
    h = {"Accept": "application/json"}
    if key:
        h["Authorization"] = f"Bearer {key}"
    return h


def read(url: str, timeout: int = 30) -> dict:
    """Fetch a URL via Reader; returns markdown body in result[0].snippet."""
    api = f"https://r.jina.ai/{url}"
    try:
        resp = requests.get(api, headers={**_headers(), "X-Return-Format": "markdown"}, timeout=timeout)
        resp.raise_for_status()
        text = resp.text
        increment_usage(NAME)
        return normalize_result(NAME, url, [{
            "title": url,
            "url": url,
            "snippet": text,
        }])
    except Exception as e:
        return normalize_result(NAME, url, error=f"read failed: {e}")


def search(query: str, count: int = 10, timeout: int = 30) -> dict:
    """SERP-style search via s.jina.ai."""
    try:
        resp = requests.get(
            "https://s.jina.ai/",
            params={"q": query},
            headers={**_headers(), "X-Respond-With": "no-content", "Accept": "application/json"},
            timeout=timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        items = data.get("data", []) if isinstance(data, dict) else data
        results = [{
            "title":   item.get("title", ""),
            "url":     item.get("url", ""),
            "snippet": item.get("description") or item.get("content", ""),
            "date":    item.get("date"),
        } for item in items[:count]]
        increment_usage(NAME)
        return normalize_result(NAME, query, results)
    except Exception as e:
        return normalize_result(NAME, query, error=f"search failed: {e}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--count", type=int, default=10)
    r = sub.add_parser("read"); r.add_argument("url")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.cmd == "search":
        res = search(a.query, a.count)
    else:
        res = read(a.url)
    cli_print(res, compact=not a.json)


if __name__ == "__main__":
    main()
