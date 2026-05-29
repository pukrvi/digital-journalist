#!/usr/bin/env python3
"""Extract clean text/markdown from a LOCAL HTML file. For URLs, use tools/fetch.sh.

Usage:
    read_html.py page.html                  # markdown
    read_html.py page.html --text           # plain text only
    read_html.py page.html --json           # JSON with title + body
    read_html.py page.html --links          # list outbound URLs
"""
import argparse
import json
import re
import sys
from urllib.parse import urlparse


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("html")
    ap.add_argument("--text", action="store_true", help="plain text only")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--links", action="store_true", help="list URLs found")
    a = ap.parse_args()

    with open(a.html, encoding="utf-8", errors="replace") as f:
        html = f.read()

    if a.links:
        urls = re.findall(r'href="(https?://[^"]+)"', html)
        urls = sorted(set(urls))
        if a.json:
            print(json.dumps(urls, indent=2))
        else:
            for u in urls:
                print(u)
        return

    import trafilatura
    result = trafilatura.extract(
        html, output_format="markdown" if not a.text else "txt",
        include_comments=False, include_tables=True, with_metadata=True
    )

    if a.json:
        meta = trafilatura.extract_metadata(html)
        out = {
            "title": meta.title if meta else None,
            "author": meta.author if meta else None,
            "date": meta.date if meta else None,
            "url": meta.url if meta else None,
            "body": result or "",
        }
        print(json.dumps(out, indent=2, default=str))
    else:
        print(result or "")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr); sys.exit(2)
