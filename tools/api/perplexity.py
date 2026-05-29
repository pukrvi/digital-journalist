#!/usr/bin/env python3
"""Perplexity Sonar models — paid, OpenAI-compatible API. Best for cited deep research.

Models (as of 2026):
  - sonar              (fast, cheapest)
  - sonar-pro          (better recall)
  - sonar-reasoning    (chain-of-thought)
  - sonar-deep-research  (deep, multi-step) — uses far more tokens, costs more

CLI:
    perplexity.py "<query>" [--model sonar-pro] [--max-tokens 4000]
    perplexity.py "<query>" --deep                       # → sonar-deep-research
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print


NAME = "perplexity"
ENDPOINT = "https://api.perplexity.ai/chat/completions"


def _paid_allowed():
    return os.environ.get("ALLOW_PAID", "0") in ("1", "true", "yes")


def search(query: str, count: int = 10, model: str = "sonar-pro", max_tokens: int = 4000, deep: bool = False, force_paid: bool = False, timeout: int = 120) -> dict:
    _ = count  # Perplexity returns its own citation set
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No PERPLEXITY_API_KEY in keys.env. Sign up: https://docs.perplexity.ai")
    if not (force_paid or _paid_allowed()):
        return normalize_result(NAME, query, error="paid provider blocked; set ALLOW_PAID=1 in keys.env or pass force_paid=True")
    if deep:
        model = "sonar-deep-research"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": query}],
        "max_tokens": max_tokens,
        "return_related_questions": False,
    }
    try:
        resp = requests.post(ENDPOINT, json=payload, headers=headers, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    answer = ""
    if data.get("choices"):
        answer = data["choices"][0]["message"]["content"]
    citations = data.get("citations") or data.get("search_results") or []
    results = []
    for c in citations:
        if isinstance(c, str):
            results.append({"title": c, "url": c, "snippet": ""})
        elif isinstance(c, dict):
            results.append({
                "title":   c.get("title", ""),
                "url":     c.get("url", ""),
                "snippet": c.get("snippet", ""),
                "date":    c.get("date"),
            })
    usage = data.get("usage", {})
    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=answer, extra={"usage_tokens": usage, "model": model})


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query"); ap.add_argument("--model", default="sonar-pro")
    ap.add_argument("--max-tokens", type=int, default=4000); ap.add_argument("--deep", action="store_true")
    ap.add_argument("--force-paid", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cli_print(search(a.query, model=a.model, max_tokens=a.max_tokens, deep=a.deep, force_paid=a.force_paid), compact=not a.json)


if __name__ == "__main__":
    main()
