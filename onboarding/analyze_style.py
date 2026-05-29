#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 INFINITIGRID TECHNOLOGIES (OPC) PRIVATE LIMITED. Created by Puneet Vishnawat.
"""Extrapolate a writer's quantitative style fingerprint from a sample they wrote.

Reads .txt/.md directly, .pdf via pdfplumber, .docx via python-docx. Emits measurable style
features the agent combines with its own qualitative read to write profile/writing-style.md.

Usage:
  analyze_style.py <file>            # human-readable fingerprint
  analyze_style.py <file> --json     # JSON (for the onboarding agent to consume)
  cat sample.txt | analyze_style.py -    # read stdin
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter

STOP = set("""a an the and or but if then else of in on at to for with by from is are was were be been being
have has had do does did this that these those i you he she it we they them their there here as not no nor so
too very can will just into about over under again more most other some such only own same than then it's i'm""".split())


def load(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    low = path.lower()
    if low.endswith((".txt", ".md", ".markdown")):
        return open(path, encoding="utf-8", errors="replace").read()
    if low.endswith(".pdf"):
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            return "\n".join((p.extract_text() or "") for p in pdf.pages)
    if low.endswith(".docx"):
        from docx import Document
        return "\n".join(p.text for p in Document(path).paragraphs)
    return open(path, encoding="utf-8", errors="replace").read()


def syllables(w: str) -> int:
    w = w.lower()
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    return max(1, len(re.findall(r"[aeiouy]+", w)))


def analyze(text: str) -> dict:
    words = re.findall(r"[A-Za-z']+", text)
    sents = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s.strip()]
    paras = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    n_words = max(1, len(words))
    n_sents = max(1, len(sents))
    sent_lens = [len(re.findall(r"[A-Za-z']+", s)) for s in sents] or [0]
    syl = sum(syllables(w) for w in words)
    per_1k = lambda c: round(c / n_words * 1000, 1)
    long_words = [w for w in words if len(w) >= 7]
    content = [w.lower() for w in words if w.lower() not in STOP and len(w) > 3]

    short = sum(1 for L in sent_lens if L < 12)
    med = sum(1 for L in sent_lens if 12 <= L <= 25)
    long = sum(1 for L in sent_lens if L > 25)

    flesch = round(206.835 - 1.015 * (n_words / n_sents) - 84.6 * (syl / n_words), 1)

    return {
        "words": len(words),
        "sentences": len(sents),
        "paragraphs": len(paras),
        "avg_sentence_words": round(n_words / n_sents, 1),
        "sentence_mix_pct": {"short(<12)": round(short / n_sents * 100), "medium(12-25)": round(med / n_sents * 100), "long(>25)": round(long / n_sents * 100)},
        "longest_sentence_words": max(sent_lens),
        "avg_paragraph_sentences": round(len(sents) / max(1, len(paras)), 1),
        "avg_word_length": round(sum(len(w) for w in words) / n_words, 2),
        "long_word_pct": round(len(long_words) / n_words * 100, 1),
        "flesch_reading_ease": flesch,
        "type_token_ratio": round(len(set(w.lower() for w in words)) / n_words, 3),
        "punctuation_per_1k": {
            "em_dash": per_1k(text.count("—") + text.count("--")),
            "semicolon": per_1k(text.count(";")),
            "colon": per_1k(text.count(":")),
            "parenthetical": per_1k(text.count("(")),
            "question": per_1k(text.count("?")),
            "exclamation": per_1k(text.count("!")),
            "comma": per_1k(text.count(",")),
        },
        "favorite_content_words": [w for w, _ in Counter(content).most_common(20)],
        "reading_grade_hint": ("very accessible" if flesch >= 70 else "plain" if flesch >= 60 else "fairly demanding" if flesch >= 50 else "demanding/academic"),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    try:
        text = load(a.file)
    except FileNotFoundError:
        print(f"ERROR: file not found: {a.file}", file=sys.stderr); sys.exit(2)
    if len(text.split()) < 60:
        print("WARNING: sample is short (<60 words); style fingerprint will be rough.", file=sys.stderr)
    feats = analyze(text)
    if a.json:
        print(json.dumps(feats, indent=2))
    else:
        print("=== Writing-style fingerprint (quantitative) ===")
        for k, v in feats.items():
            print(f"{k:>26}: {v}")
        print("\nHand this to the onboarding agent; it adds the qualitative read (voice, tone,\nsignature moves) to produce profile/writing-style.md.")


if __name__ == "__main__":
    main()
