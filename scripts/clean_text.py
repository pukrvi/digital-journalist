#!/usr/bin/env python3
"""Normalize text: collapse whitespace, fix encoding artifacts, strip boilerplate.

Usage:
    cat raw.txt | clean_text.py                  # stdin
    clean_text.py file.txt                       # file
    clean_text.py file.txt --aggressive          # also strip page numbers, headers
    clean_text.py file.txt --paragraphs          # one line per paragraph
"""
import argparse
import re
import sys
import unicodedata


SMART_QUOTES = {
    "‘": "'", "’": "'",
    "“": '"', "”": '"',
    "–": "-", "—": "--",
    "…": "...",
    "\xa0": " ",
}


def clean(text, aggressive=False, paragraphs=False):
    text = unicodedata.normalize("NFKC", text)
    for src, dst in SMART_QUOTES.items():
        text = text.replace(src, dst)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if aggressive:
        text = re.sub(r"^Page \d+ of \d+\s*$", "", text, flags=re.MULTILINE)
        text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)
        text = re.sub(r"\f", "\n", text)
        text = re.sub(r"^\s*[•·\-]\s*", "- ", text, flags=re.MULTILINE)
    if paragraphs:
        paras = [" ".join(p.split()) for p in re.split(r"\n\s*\n", text) if p.strip()]
        text = "\n".join(paras)
    return text.strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file", nargs="?", help="omit to read stdin")
    ap.add_argument("--aggressive", action="store_true")
    ap.add_argument("--paragraphs", action="store_true")
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8", errors="replace").read() if a.file else sys.stdin.read()
    print(clean(text, aggressive=a.aggressive, paragraphs=a.paragraphs))


if __name__ == "__main__":
    main()
