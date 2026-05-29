#!/usr/bin/env python3
"""xAI Grok with Live Search. Paid. OpenAI-compatible API.

CLI:
    xai_grok.py "<query>"
    xai_grok.py "<query>" --model grok-2-latest
"""
from __future__ import annotations

import argparse
import os
import sys

import requests

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print


NAME = "xai_grok"
ENDPOINT = "https://api.x.ai/v1/chat/completions"


def _paid_allowed():
    return os.environ.get("ALLOW_PAID", "0") in ("1", "true", "yes")


def search(query: str, count: int = 10, model: str = "grok-2-latest", force_paid: bool = False, timeout: int = 120) -> dict:
    _ = count
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No XAI_API_KEY in keys.env. Sign up: https://docs.x.ai")
    if not (force_paid or _paid_allowed()):
        return normalize_result(NAME, query, error="paid provider blocked; set ALLOW_PAID=1 in keys.env or pass --force-paid")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": query}],
        "search_parameters": {"mode": "auto", "return_citations": True},
    }
    try:
        resp = requests.post(ENDPOINT, json=payload, headers=headers, timeout=timeout)
        if resp.status_code != 200:
            return normalize_result(NAME, query, error=f"HTTP {resp.status_code}: {resp.text[:300]}")
        data = resp.json()
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    answer = data["choices"][0]["message"]["content"] if data.get("choices") else ""
    citations = data.get("citations") or []
    results = []
    for c in citations:
        if isinstance(c, str):
            results.append({"title": c, "url": c, "snippet": ""})
        elif isinstance(c, dict):
            results.append({"title": c.get("title", ""), "url": c.get("url", ""), "snippet": c.get("snippet", "")})
    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=answer, extra={"model": model})


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query"); ap.add_argument("--model", default="grok-2-latest")
    ap.add_argument("--force-paid", action="store_true"); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cli_print(search(a.query, model=a.model, force_paid=a.force_paid), compact=not a.json)


if __name__ == "__main__":
    main()
