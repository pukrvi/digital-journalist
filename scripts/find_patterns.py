#!/usr/bin/env python3
"""Find recurring patterns across a corpus: top n-grams, repeated phrases, recurring names/orgs.

Usage:
    find_patterns.py articles/sf-algebra/research/         # all .md in dir
    find_patterns.py file1.md file2.md                     # specific files
    find_patterns.py articles/ --ngram 3 --top 30          # 3-grams, top 30
    find_patterns.py articles/ --names                     # capitalized phrases (names, orgs)
    find_patterns.py articles/ --quotes                    # repeated direct quotes
    find_patterns.py articles/ --json
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import Counter


STOPWORDS = set("""a an the and or but if then else of in on at to for with by from is are was were be been
being have has had do does did this that these those i you he she it we they them their there here as
not no nor so too very can will just up out into about against between through during before after
above below over under further also which who whom whose what when where why how all any both each
few more most other some such only own same than then once will would could should may might must shall
""".split())


def gather_text(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for f in glob.glob(os.path.join(p, "**", "*.md"), recursive=True):
                files.append(f)
        elif os.path.isfile(p):
            files.append(p)
    text = []
    for f in files:
        with open(f, encoding="utf-8", errors="replace") as fh:
            text.append(fh.read())
    return "\n".join(text)


def top_ngrams(text, n=2, top=20, exclude_stop=True):
    tokens = re.findall(r"[A-Za-z][A-Za-z\-']+", text.lower())
    if exclude_stop and n == 1:
        tokens = [t for t in tokens if t not in STOPWORDS]
    grams = []
    for i in range(len(tokens) - n + 1):
        g = tokens[i:i+n]
        if exclude_stop and (g[0] in STOPWORDS or g[-1] in STOPWORDS):
            continue
        grams.append(" ".join(g))
    return Counter(grams).most_common(top)


def names_orgs(text, top=30):
    # Crude: 2+ capitalized words in a row, ignoring sentence-start fluke
    candidates = re.findall(r"(?<![.!?]\s)([A-Z][a-z]+(?: [A-Z][a-z]+){1,4})", text)
    return Counter(candidates).most_common(top)


def repeated_quotes(text, min_len=40, top=20):
    quotes = re.findall(r'"([^"]{%d,300})"' % min_len, text)
    return Counter(quotes).most_common(top)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--ngram", type=int, default=2)
    ap.add_argument("--top", type=int, default=20)
    ap.add_argument("--names", action="store_true")
    ap.add_argument("--quotes", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    text = gather_text(a.paths)
    out = {}

    if a.names:
        out["names_orgs"] = names_orgs(text, a.top)
    if a.quotes:
        out["repeated_quotes"] = repeated_quotes(text, top=a.top)
    if not a.names and not a.quotes:
        out[f"top_{a.ngram}grams"] = top_ngrams(text, n=a.ngram, top=a.top)

    if a.json:
        print(json.dumps(out, indent=2))
    else:
        for k, items in out.items():
            print(f"\n## {k}\n")
            for term, count in items:
                print(f"  {count:4d}  {term}")


if __name__ == "__main__":
    main()
