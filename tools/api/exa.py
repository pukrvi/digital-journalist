#!/usr/bin/env python3
"""Exa (formerly Metaphor) — semantic / neural search. Free credits: $10.

Two modes:
  - search: neural/keyword over the open web
  - contents: fetch full text + highlights for a list of URLs (the killer feature)

CLI:
    exa.py search "<query>" [--count 10] [--type neural|keyword] [--text]
    exa.py contents <url1> <url2> ... [--highlights] [--summary]
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "exa"
BASE = "https://api.exa.ai"


def _h(key):
    return {"x-api-key": key, "Content-Type": "application/json"}


def search(query: str, count: int = 10, type_: str = "neural", with_text: bool = False, timeout: int = 30) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No EXA_API_KEY in keys.env. Sign up: https://exa.ai")
    payload = {"query": query, "numResults": count, "type": type_, "useAutoprompt": True}
    if with_text:
        payload["contents"] = {"text": True}
    try:
        resp = requests.post(f"{BASE}/search", json=payload, headers=_h(key), timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    results = []
    for it in data.get("results", []):
        results.append({
            "title":   it.get("title", ""),
            "url":     it.get("url", ""),
            "snippet": (it.get("text") or it.get("highlight") or "")[:600],
            "date":    it.get("publishedDate"),
            "score":   it.get("score"),
        })
    increment_usage(NAME)
    return normalize_result(NAME, query, results)


def contents(urls, highlights: bool = False, summary: bool = False, timeout: int = 45) -> dict:
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, ",".join(urls), error="No EXA_API_KEY")
    payload = {"ids": urls}
    if highlights:
        payload["highlights"] = {"numSentences": 3, "highlightsPerUrl": 3}
    if summary:
        payload["summary"] = True
    payload["text"] = True
    try:
        resp = requests.post(f"{BASE}/contents", json=payload, headers=_h(key), timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, ",".join(urls), error=str(e))

    out = []
    for it in data.get("results", []):
        out.append({
            "title":   it.get("title", ""),
            "url":     it.get("url", ""),
            "snippet": (it.get("text") or "")[:2000],
            "extra":   {"highlights": it.get("highlights"), "summary": it.get("summary")},
        })
    increment_usage(NAME, len(urls))
    return normalize_result(NAME, ",".join(urls), out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--count", type=int, default=10)
    s.add_argument("--type", dest="type_", default="neural", choices=["neural", "keyword", "auto"])
    s.add_argument("--text", action="store_true")
    c = sub.add_parser("contents"); c.add_argument("urls", nargs="+")
    c.add_argument("--highlights", action="store_true"); c.add_argument("--summary", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.cmd == "search":
        r = search(a.query, a.count, type_=a.type_, with_text=a.text)
    else:
        r = contents(a.urls, highlights=a.highlights, summary=a.summary)
    cli_print(r, compact=not a.json)


if __name__ == "__main__":
    main()
