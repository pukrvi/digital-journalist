#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 INFINITIGRID TECHNOLOGIES (OPC) PRIVATE LIMITED. Created by Puneet Vishnawat.
"""Onboarding orchestration helper — the deterministic half of the LLM-native onboarding.

The AGENT runs the conversation (see onboarding/onboard.md); this CLI does the file writes,
secure key storage, and the status checklist so steps are idempotent and resumable.

Usage:
  onboard.py status                                  # what's configured / what's left
  onboard.py profile --name "..." --role "..." --beats "..." --audience "..." [--notes "..."]
  onboard.py style  --json <analysis.json|-> [--voice "..."] [--rhythm "..."] \
                    [--signature "..."] [--favors "..."] [--avoids "..."] [--admires "..."]
  onboard.py key --provider tavily --value "sk-..."  # secure-store (delegates to keys_manager)
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILE = ROOT / "profile"
WRITER = PROFILE / "writer.md"
STYLE = PROFILE / "writing-style.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import keys_manager as km  # noqa: E402

TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")


def cmd_profile(a):
    PROFILE.mkdir(parents=True, exist_ok=True)
    WRITER.write_text(f"""# Writer profile

*Read by the digital-journalist at the start of every job. Tells it who it's writing for.*

- **Name:** {a.name}
- **Role / title:** {a.role}
- **Beats / topics:** {a.beats}
- **Primary audience:** {a.audience}
- **Notes:** {a.notes or "(none)"}
- **Created:** {TODAY}

> The journalist stays a neutral referee on the *facts*; this profile shapes *altitude and relevance*
> (what to assume the reader knows, which angles matter to this beat), not the verdict.
""", encoding="utf-8")
    print(f"[saved] {WRITER.relative_to(ROOT)}")


def cmd_style(a):
    PROFILE.mkdir(parents=True, exist_ok=True)
    feats = {}
    if a.json:
        raw = sys.stdin.read() if a.json == "-" else Path(a.json).read_text(encoding="utf-8")
        try:
            feats = json.loads(raw)
        except Exception:
            feats = {}
    q = feats
    pun = q.get("punctuation_per_1k", {})
    quant = ""
    if q:
        quant = f"""## Measured fingerprint (from your sample)

| Metric | Value |
|---|---|
| Avg sentence length | {q.get('avg_sentence_words','?')} words |
| Sentence mix | {q.get('sentence_mix_pct','?')} |
| Avg paragraph | {q.get('avg_paragraph_sentences','?')} sentences |
| Reading ease (Flesch) | {q.get('flesch_reading_ease','?')} — {q.get('reading_grade_hint','?')} |
| Vocabulary richness (TTR) | {q.get('type_token_ratio','?')} |
| Long-word % | {q.get('long_word_pct','?')}% |
| Em-dash / 1k words | {pun.get('em_dash','?')} |
| Semicolon / 1k words | {pun.get('semicolon','?')} |
| Question / 1k words | {pun.get('question','?')} |
| Favorite words | {', '.join(q.get('favorite_content_words', [])[:12]) or '?'} |
"""
    STYLE.write_text(f"""# Writing style guide

*Read by the WRITE stage (dj-write). The article should sound like the user, not generic AI.
This is the **house voice**; a per-article `voice` arg can override it.*

## Voice & tone
{a.voice or "(describe: e.g. measured-analytical, warm but rigorous)"}

## Sentence rhythm
{a.rhythm or "(describe: e.g. mostly medium, broken by a short punch)"}

## Signature moves
{a.signature or "(e.g. opens on a concrete scene; ends on a forward-looking kicker; uses one vivid stat per section)"}

## Favors
{a.favors or "(words/structures the writer leans on)"}

## Avoids
{a.avoids or "(words/tics the writer dislikes — plus the global AI-slop blocklist in writing-standards.md)"}

## Writers / publications admired
{a.admires or "(targets to emulate)"}

{quant}

**Created:** {TODAY}
""", encoding="utf-8")
    print(f"[saved] {STYLE.relative_to(ROOT)}")


def cmd_key(a):
    km.set_key(a.provider, a.value)


def cmd_status(a):
    print("=== Digital Journalist — onboarding status ===\n")
    print(f"[{'x' if WRITER.exists() else ' '}] 1. Writer profile         {WRITER.relative_to(ROOT) if WRITER.exists() else '(run: onboard.py profile ...)'}")
    print(f"[{'x' if STYLE.exists() else ' '}] 2-3. Writing style guide   {STYLE.relative_to(ROOT) if STYLE.exists() else '(upload a sample; run analyze_style.py then onboard.py style ...)'}")
    pairs = km._read_env()
    set_providers = []
    for prov, env in km.PROVIDER_ENV.items():
        if pairs.get(env):
            set_providers.append(prov)
    print(f"[x] 4. Keyless search        duckduckgo (always on)")
    print(f"[{'x' if set_providers else ' '}] 5. Provider API keys     {', '.join(set_providers) if set_providers else '(run: onboard.py key --provider <p> --value <k>)'}")
    print()
    done = WRITER.exists() and STYLE.exists()
    if done and set_providers:
        print("Onboarding complete. Start your first article — say:\n  \"Run the digital-journalist on: <your topic>\"")
    else:
        print("Next: " + (
            "add a writer profile" if not WRITER.exists()
            else "add your writing style (upload a sample)" if not STYLE.exists()
            else "connect at least one search provider key (optional — DuckDuckGo already works)"))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    p = sub.add_parser("profile")
    p.add_argument("--name", required=True); p.add_argument("--role", default="")
    p.add_argument("--beats", default=""); p.add_argument("--audience", required=True); p.add_argument("--notes", default="")
    s = sub.add_parser("style")
    s.add_argument("--json", help="path to analyze_style.py JSON, or '-' for stdin")
    for f in ("voice", "rhythm", "signature", "favors", "avoids", "admires"):
        s.add_argument(f"--{f}", default="")
    k = sub.add_parser("key"); k.add_argument("--provider", required=True); k.add_argument("--value", required=True)
    a = ap.parse_args()
    {"status": cmd_status, "profile": cmd_profile, "style": cmd_style, "key": cmd_key}[a.cmd](a)


if __name__ == "__main__":
    main()
