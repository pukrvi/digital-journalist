#!/usr/bin/env python3
"""Google AI Studio (Gemini) with Google Search grounding. Free tier: 1,500/day on Flash.

CLI:
    gemini.py "<query>"                      # gemini-2.5-flash + grounding
    gemini.py "<query>" --model gemini-2.0-flash
    gemini.py "<query>" --json
"""
from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import normalize_result, increment_usage, get_key, cli_print, check_limit


NAME = "gemini"


def search(query: str, count: int = 10, model: str = "gemini-2.5-flash") -> dict:
    # count is accepted for uniform-signature compatibility with other providers; Gemini
    # decides on its own how many sources to ground against.
    _ = count
    key = get_key(NAME)
    if not key:
        return normalize_result(NAME, query, error="No GEMINI_API_KEY in keys.env. Get free: https://aistudio.google.com")
    if not check_limit(NAME):
        return normalize_result(NAME, query, error="gemini daily limit reached")
    try:
        os.environ["GEMINI_API_KEY"] = key
        from google import genai
        from google.genai import types
    except Exception as e:
        return normalize_result(NAME, query, error=f"google-genai not installed: {e}")
    try:
        client = genai.Client()
        resp = client.models.generate_content(
            model=model,
            contents=query,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
            ),
        )
    except Exception as e:
        return normalize_result(NAME, query, error=str(e))

    text = getattr(resp, "text", "") or ""
    results = []
    gm = getattr(resp.candidates[0], "grounding_metadata", None) if resp.candidates else None
    if gm and getattr(gm, "grounding_chunks", None):
        for chunk in gm.grounding_chunks:
            web = getattr(chunk, "web", None)
            if web:
                results.append({
                    "title":   getattr(web, "title", ""),
                    "url":     getattr(web, "uri", ""),
                    "snippet": "",
                })
    increment_usage(NAME)
    return normalize_result(NAME, query, results, ai_summary=text)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query"); ap.add_argument("--model", default="gemini-2.5-flash")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    cli_print(search(a.query, model=a.model), compact=not a.json)


if __name__ == "__main__":
    main()
