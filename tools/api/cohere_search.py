#!/usr/bin/env python3
"""Cohere Command-R/R+ with web-search connector — grounded gen-AI search via plain HTTP.

CLI:
    cohere_search.py "<query>"                       # command-r-plus + web-search connector
    cohere_search.py "<query>" --model command-r
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "cohere"
ENDPOINT = "https://api.cohere.com/v1/chat"


def search(query: str, count: int = 10, model: str = "command-r-plus", timeout: int = 60) -> dict:
    _ = count  # Cohere decides its own result count
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No COHERE_API_KEY in keys.env. Get free trial: https://cohere.com")
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="cohere free-tier limit reached")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "message": query,
        "connectors": [{"id": "web-search"}],
    }
    try:
        resp = requests.post(ENDPOINT, json=payload, headers=headers, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    answer = data.get("text", "")
    docs = data.get("documents") or []
    citations = data.get("citations") or []
    results = []
    seen = set()
    # Pull cited URLs first, then any other documents
    for c in citations:
        for d_id in c.get("document_ids", []):
            for d in docs:
                if d.get("id") == d_id and d.get("url") not in seen:
                    seen.add(d.get("url"))
                    results.append({
                        "title":   d.get("title") or d.get("snippet", "")[:80],
                        "url":     d.get("url", ""),
                        "snippet": d.get("snippet", "")[:500],
                    })
    for d in docs:
        if d.get("url") and d.get("url") not in seen:
            seen.add(d.get("url"))
            results.append({
                "title":   d.get("title") or d.get("snippet", "")[:80],
                "url":     d.get("url", ""),
                "snippet": d.get("snippet", "")[:500],
            })
    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=answer)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query"); ap.add_argument("--model", default="command-r-plus"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cli_print(search(a.query, model=a.model), compact=not a.json)


if __name__ == "__main__":
    main()
