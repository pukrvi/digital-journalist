#!/usr/bin/env python3
"""Find duplicate or near-duplicate sources across research files in an article.

Usage:
    dedup_sources.py articles/sf-algebra/research/
    dedup_sources.py articles/sf-algebra/                  # auto-finds research/
    dedup_sources.py articles/sf-algebra/ --json
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict
from urllib.parse import urlparse


URL_RE = re.compile(r"https?://[^\s)\]\"<>]+")
TITLE_RE = re.compile(r"^###\s*\[\d+\]\s*(.+?)\s*$", re.MULTILINE)


def normalize_url(u):
    p = urlparse(u.rstrip(".,;:'\""))
    return f"{p.netloc.lower()}{p.path.rstrip('/')}"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    research = a.path
    if os.path.isdir(os.path.join(a.path, "research")):
        research = os.path.join(a.path, "research")

    if not os.path.isdir(research):
        print(f"ERROR: not a directory: {research}", file=sys.stderr); sys.exit(2)

    files = sorted(glob.glob(os.path.join(research, "*.md")))

    by_url = defaultdict(list)
    by_title = defaultdict(list)

    for f in files:
        with open(f, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        urls = set(URL_RE.findall(text))
        titles = TITLE_RE.findall(text)
        for u in urls:
            by_url[normalize_url(u)].append((os.path.basename(f), u))
        for t in titles:
            by_title[t.strip().lower()].append(os.path.basename(f))

    dup_urls = {k: v for k, v in by_url.items() if len({lens for lens, _ in v}) > 1}
    dup_titles = {k: v for k, v in by_title.items() if len(set(v)) > 1}

    result = {
        "files_scanned": len(files),
        "unique_urls": len(by_url),
        "duplicate_urls_across_lenses": dup_urls,
        "duplicate_titles_across_lenses": dup_titles,
    }

    if a.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Files scanned: {len(files)}, unique URLs: {len(by_url)}")
        if dup_urls:
            print(f"\nURLs cited in multiple lenses ({len(dup_urls)}):")
            for k, v in sorted(dup_urls.items(), key=lambda kv: -len(kv[1])):
                lenses = sorted({lens for lens, _ in v})
                print(f"  {k}")
                print(f"    in: {', '.join(lenses)}")
        else:
            print("\nNo URL duplication across lenses. Good source diversity.")
        if dup_titles:
            print(f"\nTitles cited in multiple lenses ({len(dup_titles)}):")
            for t, lenses in sorted(dup_titles.items(), key=lambda kv: -len(kv[1])):
                print(f"  \"{t}\"")
                print(f"    in: {', '.join(sorted(set(lenses)))}")


if __name__ == "__main__":
    main()
