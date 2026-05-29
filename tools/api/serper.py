#!/usr/bin/env python3
"""Serper.dev — fast Google SERP. Free tier: 2,500 queries (one-time).

CLI:
    serper.py "<query>" [--count 10] [--news] [--json]
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "serper"


def search(query: str, count: int = 10, news: bool = False, timeout: int = 30) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No SERPER_API_KEY in keys.env. Sign up: https://serper.dev")
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="serper free credits exhausted")

    endpoint = "https://google.serper.dev/news" if news else "https://google.serper.dev/search"
    payload = {"q": query, "num": count}
    headers = {"X-API-KEY": key, "Content-Type": "application/json"}
    try:
        resp = requests.post(endpoint, json=payload, headers=headers, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    items = data.get("news") if news else data.get("organic", [])
    results = [{
        "title":   it.get("title", ""),
        "url":     it.get("link", ""),
        "snippet": it.get("snippet", ""),
        "date":    it.get("date"),
        "score":   it.get("position"),
    } for it in (items or [])[:count]]

    ai_summary = data.get("answerBox", {}).get("answer") if isinstance(data.get("answerBox"), dict) else None
    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=ai_summary)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query"); ap.add_argument("--count", type=int, default=10)
    ap.add_argument("--news", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cli_print(search(a.query, a.count, news=a.news), compact=not a.json)


if __name__ == "__main__":
    main()
