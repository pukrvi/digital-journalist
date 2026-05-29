# Architecture

The journalist runs in **two stages** with a round of clarifying questions before each. A workflow is
headless (it can't prompt you mid-run), so the questions live in the conversation — and splitting the job
also makes research a **durable checkpoint**.

## Why two stages

Research is ~80% of the cost. In an earlier monolithic version, a single end-of-run agent missed its
structured output and a ~2-hour, 2.1M-token run was lost. Splitting means:
- A write-stage hiccup costs minutes, not the whole job (the dossier is on disk).
- The second, *evidence-informed* round of questions becomes physically possible.
- The write stage is **schema-free** (writes files, returns text), so it can't hit that failure mode.

## Stage 1 — research (`digital-journalist.workflow.js`, 9 phases)

1. **Load memory** — apply prior lessons from `memory/*`.
2. **Scope** — grounded in a live search; core question, 6–8 lenses (contrarian mandatory), POV handling.
3. **Setup** — article folder + `scope.md`.
4. **Multi-lens research** — one agent per lens, in parallel, using **both** native `WebSearch` **and** the
   aggregator, under a **source-class mandate** (government/agency, consulting/market-research, comparables).
5. **Master dossier** → `master.md`: exec synthesis, view spectrum, authority-ordered quote bank,
   tier-ordered fact/data ledger, source index.
6. **Adversarial verification** — extract 8–12 load-bearing claims, *try to refute each*.
7. **Fill gaps** — completeness critic fills what's missing.
8. **Synthesize** → `synthesis.md` (big insight, disputes, hidden patterns, traps).
9. **Round-2 questions** → `research/round2-questions.md`. **Stops here.**

## Stage 2 — write (`dj-write.workflow.js`, 4 phases, schema-free)

1. **Writer brief** — apply the Round-2 voice/POV + your `profile/writing-style.md`; pick the lede and quotes.
2. **Write** → `article.md` + `sources.md` (NYT/WSJ/Bloomberg standard, credibility-ordered citations).
3. **SEO headlines** → `titles.md` (10, differentiated from every source).
4. **Meta + memory** → `meta.json` + memory updates.

Run it with `outFolder` == `srcFolder` to finish a run, or `outFolder` ≠ `srcFolder` to **spin a new angle
off the same research** — no re-research. (The two `examples/` articles share one dossier this way.)

## Output

```
articles/<slug>/
├── article.md        master.md        titles.md        sources.md        meta.json
└── research/  scope · <lens>×N · verification · gaps · synthesis · round2-questions · writer-brief
```

## Workflow runtime gotchas

- No `Date.now()` / `Math.random()` — pass `timestamp` via args.
- Always `JSON.parse` string args defensively.
- Heavy file-writing agents → schema-free; reserve JSON schemas for small control-flow returns.
- `node --check` both scripts; keep `meta.phases` in sync with `phase()` calls.

## Recovery

If a run ever aborts, the research is on disk. Re-run Stage 2 (`dj-write`) pointed at the folder to finish
from the checkpoint — no re-research.
