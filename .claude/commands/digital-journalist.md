---
description: Run the Digital Journalist on a topic — research, verify, then write (two stages, two rounds of clarifying questions)
argument-hint: <topic>
---

Run the **Digital Journalist** on this topic: **$ARGUMENTS**

If `$ARGUMENTS` is empty (or appears literally because your agent didn't substitute it), the topic should be in the user's most recent message — extract it and confirm with the user before proceeding. If `profile/writer.md` is missing, suggest running `/onboard` first (the ~5-minute onboarding flow). At the start, also read `memory/learnings.md`, `memory/source-quality.md`, `memory/failure-modes.md`, and `memory/writing-standards.md` so you apply prior lessons.

Then follow the run protocol in [CLAUDE.md](CLAUDE.md) **exactly** — two stages with two rounds of clarifying questions. The protocol is non-optional: a headless workflow can't prompt mid-run, so the clarifying questions live in this conversation.

## Round 1 — scope (before research)

1. **Quick scan (~1 min):** run `python3 tools/api/search.py "<topic>" --count 4 --aggregate` (and optionally one native `WebSearch`). Skim the AI summaries + top results to ground your question options.
2. **Ask 2–4 questions via `AskUserQuestion`**, options informed by the scan:
   - **Angle** — what's the cut?
   - **Audience** — who reads this? (Atlantic/Bloomberg generalist by default)
   - **Initial POV/stance** — thesis or neutral? (neutral = empty string)
   - **Must-include** — people, sources, sub-questions to cover
3. **Launch Stage 1 — research:**

```js
Workflow({ name: "digital-journalist", args: {
  topic: "<topic>",
  angle: "<from Q>",
  audience: "<from Q>",
  pov: "<from Q — empty string = neutral>",
  clarifications: { "Angle": "...", "Stance": "..." },
  mustInclude: ["..."],
  mustAvoid: ["..."],
  timestamp: "<today's date in YYYY-MM-DD>"
}})
```

Stage 1 builds `articles/<slug>/master.md`, `verification.md`, `synthesis.md`, and `research/round2-questions.md`. **It stops before writing** — the dossier is a durable checkpoint.

> If your agent has no `Workflow` runtime (Codex, Openclaw, etc.), run the **same methodology as a guided process**: read `digital-journalist.workflow.js` as the spec, then drive the phases yourself (scope → 6–8 lens searches via `tools/api/search.py` → `master.md` → adversarial verification → `synthesis.md` → write `research/round2-questions.md`), writing the same files to `articles/<slug>/`.

## Round 2 — voice & POV (after research, informed by evidence)

4. **Read `articles/<slug>/research/round2-questions.md`** — the engine proposes 3–4 deeper questions grounded in what the research actually found (real tensions, the killer stat, the contrarian twist).
5. **Ask those questions via `AskUserQuestion`.** They cover:
   - Where to **land** now that evidence is in (stay neutral / take the side the evidence favors / foreground a specific tension)
   - **Voice/tone**
   - What to **lead with**
   - What to **emphasize or cut**
   - Headline direction

   If the user says "you decide," use the file's "Suggested default answers."
6. **Launch Stage 2 — write:**

```js
Workflow({ scriptPath: "dj-write.workflow.js", args: {
  srcFolder: "articles/<slug>",
  outFolder: "articles/<slug>",
  topic: "<topic>",
  audience: "<from Q>",
  stance: "<from Q — where to land>",
  voice: "<measured-analytical | narrative-literary | punchy-provocative | contrarian-sharp>",
  leadWith: "<the human story | the killer stat | the contrarian twist | the historical parallel>",
  emphasize: ["..."],
  deemphasize: ["..."],
  timestamp: "<today's date in YYYY-MM-DD>"
}})
```

Stage 2 produces `article.md`, `sources.md`, `titles.md`, `meta.json` and updates `memory/*.md`. (On agents without a Workflow runtime, drive these phases as a guided process from `dj-write.workflow.js`.)

## Notes

- **"Just do the whole thing":** still split into two stages — run Stage 1, then answer Round 2 yourself from `round2-questions.md`'s "Suggested default answers," then run Stage 2.
- **Spin a new angle off the same research** (no re-research): run Stage 2 again with `outFolder` ≠ `srcFolder`.
- The POV guides emphasis only — **the contrarian lens stays mandatory** and counter-evidence is never suppressed.
- Hard rule: pass `timestamp` via args. The Workflow runtime forbids `Date.now()`.
- Stick to the core principles in [CLAUDE.md](CLAUDE.md): boil the ocean, contrarian by default, cite or skip, authoritative sources first, save the receipts, improve every run.
