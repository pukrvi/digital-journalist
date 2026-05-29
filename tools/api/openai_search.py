#!/usr/bin/env python3
"""OpenAI with web search. Uses chat completions w/ tools — model gpt-4o-search-preview
or gpt-5-search-preview if available. Paid.

CLI:
    openai_search.py "<query>"
    openai_search.py "<query>" --model gpt-4o-search-preview
"""
from __future__ import annotations

import argparse
import os
import re
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print


NAME = "openai_search"
ENDPOINT = "https://api.openai.com/v1/chat/completions"


def _paid_allowed():
    return os.environ.get("ALLOW_PAID", "0") in ("1", "true", "yes")


def search(query: str, count: int = 10, model: str = "gpt-4o-search-preview", force_paid: bool = False, timeout: int = 120) -> dict:
    _ = count
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No OPENAI_API_KEY in keys.env. Sign up: https://platform.openai.com")
    if not (force_paid or _paid_allowed()):
        return normalize_result(NAME, query, error="paid provider blocked; set ALLOW_PAID=1 in keys.env or pass --force-paid")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": query}],
        "web_search_options": {},  # enable built-in search where supported
    }
    try:
        resp = requests.post(ENDPOINT, json=payload, headers=headers, timeout=timeout)
        if resp.status_code != 200:
            return normalize_result(NAME, query, error=f"HTTP {resp.status_code}: {resp.text[:300]}")
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    answer = data["choices"][0]["message"]["content"] if data.get("choices") else ""
    annotations = []
    if data.get("choices"):
        annotations = (data["choices"][0]["message"].get("annotations") or [])
    results = []
    for a in annotations:
        if a.get("type") == "url_citation":
            uc = a.get("url_citation") or {}
            results.append({"title": uc.get("title", ""), "url": uc.get("url", ""), "snippet": ""})
    # If no annotations, fall back to extracting URLs from the body
    if not results and answer:
        for url in set(re.findall(r"https?://[^\s)>\]\"]+", answer)):
            results.append({"title": url, "url": url, "snippet": ""})
    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=answer, extra={"model": model, "usage_tokens": data.get("usage", {})})


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query"); ap.add_argument("--model", default="gpt-4o-search-preview")
    ap.add_argument("--force-paid", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cli_print(search(a.query, model=a.model, force_paid=a.force_paid), compact=not a.json)


if __name__ == "__main__":
    main()
