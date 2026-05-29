#!/usr/bin/env python3
"""Anthropic Claude with the web_search server tool. Paid.

CLI:
    anthropic_search.py "<query>"
    anthropic_search.py "<query>" --model claude-sonnet-4-6
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print


NAME = "anthropic_search"
ENDPOINT = "https://api.anthropic.com/v1/messages"
DEFAULT_MODEL = "claude-sonnet-4-6"


def _paid_allowed():
    return os.environ.get("ALLOW_PAID", "0") in ("1", "true", "yes")


def search(query: str, count: int = 10, model: str = DEFAULT_MODEL, max_uses: int = 5, force_paid: bool = False, timeout: int = 120) -> dict:
    _ = count
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No ANTHROPIC_API_KEY in keys.env. Sign up: https://console.anthropic.com")
    if not (force_paid or _paid_allowed()):
        return normalize_result(NAME, query, error="paid provider blocked; set ALLOW_PAID=1 in keys.env or pass --force-paid")
    headers = {
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    payload = {
        "model": model,
        "max_tokens": 4096,
        "tools": [{"type": "web_search_20250305", "name": "web_search", "max_uses": max_uses}],
        "messages": [{"role": "user", "content": query}],
    }
    try:
        resp = requests.post(ENDPOINT, json=payload, headers=headers, timeout=timeout)
        if resp.status_code != 200:
            return normalize_result(NAME, query, error=f"HTTP {resp.status_code}: {resp.text[:300]}")
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    text_parts = []
    citations = []
    for block in data.get("content", []) or []:
        if block.get("type") == "text":
            text_parts.append(block.get("text", ""))
            for c in block.get("citations", []) or []:
                if c.get("type") in ("web_search_result_location", "url_citation"):
                    citations.append({
                        "title": c.get("title", ""),
                        "url":   c.get("url", ""),
                        "snippet": c.get("cited_text", "") or "",
                    })
    # Dedupe by URL preserving order
    seen, dedup = set(), []
    for c in citations:
        if c["url"] and c["url"] not in seen:
            seen.add(c["url"]); dedup.append(c)
    increment_usage(NAME)
    return normalize_result(NAME, query, dedup, ai_summary="\n".join(text_parts), extra={"model": model, "usage": data.get("usage", {})})


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query"); ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max-uses", type=int, default=5)
    ap.add_argument("--force-paid", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cli_print(search(a.query, model=a.model, max_uses=a.max_uses, force_paid=a.force_paid), compact=not a.json)


if __name__ == "__main__":
    main()
