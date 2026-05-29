#!/usr/bin/env python3
"""Compute readability, source diversity, citation density on a text or article folder.

Usage:
    text_stats.py article.md                              # one file
    text_stats.py articles/sf-algebra/article.md          # finished article stats
    text_stats.py articles/sf-algebra/                    # whole article folder
    text_stats.py file.md --json
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import Counter
from urllib.parse import urlparse


def syllables(word):
    word = word.lower()
    if len(word) <= 3: return 1
    word = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", word)
    word = re.sub(r"^y", "", word)
    return max(1, len(re.findall(r"[aeiouy]+", word)))


def flesch(text):
    sentences = max(1, len(re.findall(r"[.!?]+", text)))
    words = re.findall(r"[A-Za-z']+", text)
    if not words: return 0
    syls = sum(syllables(w) for w in words)
    return round(206.835 - 1.015 * (len(words) / sentences) - 84.6 * (syls / len(words)), 1)


def gather(path):
    if os.path.isdir(path):
        files = sorted(glob.glob(os.path.join(path, "**", "*.md"), recursive=True))
    else:
        files = [path]
    text = ""
    for f in files:
        with open(f, encoding="utf-8", errors="replace") as fh:
            text += fh.read() + "\n"
    return text, files


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    text, files = gather(a.path)
    words = re.findall(r"[A-Za-z']+", text)
    sentences = re.split(r"(?<=[.!?])\s+", text)
    urls = re.findall(r"https?://[^\s)\]]+", text)
    domains = Counter(urlparse(u).netloc.lower() for u in urls)
    quotes = re.findall(r'"[^"]{20,400}"', text)
    citations = re.findall(r"\[(\d+)\]", text)

    stats = {
        "files": len(files),
        "words": len(words),
        "sentences": len([s for s in sentences if s.strip()]),
        "avg_sentence_words": round(len(words) / max(1, len([s for s in sentences if s.strip()])), 1),
        "characters": len(text),
        "flesch_reading_ease": flesch(text),
        "urls_total": len(urls),
        "urls_unique": len(set(urls)),
        "domains_unique": len(domains),
        "top_domains": domains.most_common(10),
        "quotes": len(quotes),
        "citations_inline": len(citations),
        "citations_unique": len(set(citations)),
    }

    if a.json:
        print(json.dumps(stats, indent=2))
    else:
        print(f"Files: {stats['files']}")
        print(f"Words: {stats['words']:,}    Sentences: {stats['sentences']:,}    Avg sent length: {stats['avg_sentence_words']}")
        print(f"Flesch reading ease: {stats['flesch_reading_ease']}  (60-70 = plain English; lower = harder)")
        print(f"URLs:  {stats['urls_total']} total, {stats['urls_unique']} unique across {stats['domains_unique']} domains")
        print(f"Quotes: {stats['quotes']}")
        print(f"Inline citations: {stats['citations_inline']} ({stats['citations_unique']} unique)")
        if stats["top_domains"]:
            print("Top domains:")
            for d, n in stats["top_domains"]:
                print(f"  {n:3d}  {d}")


if __name__ == "__main__":
    main()
