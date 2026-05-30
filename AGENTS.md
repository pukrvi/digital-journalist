# AGENTS.md — entry point for AI coding agents

This file orients any AI agent (Codex, Openclaw, Claude Code, Cursor, etc.) working in this repo.
The deep operating manual is **[CLAUDE.md](CLAUDE.md)** — read it before running a job.

## What this is

**Digital Journalist** — an agentic, self-improving investigative-journalism system. Give it a topic;
it "boils the ocean" (15–25 sources across 6–8 lenses), adversarially verifies the load-bearing claims,
and writes a fully-cited, NYT/WSJ/Bloomberg-grade article in the user's voice. It learns from every run.

## First run: onboard the user (≈5 min)

If `profile/writer.md` is missing, onboard first. Run the playbook **[onboarding/onboard.md](onboarding/onboard.md)**:
1. Who they are → 2. Writing style → 3. Upload a sample (extrapolate voice) → 4. Pick search providers → 5. Add API keys.
Check progress with `python3 onboarding/onboard.py status`. In Claude Code use the `/onboard` command (or `/digital-journalist <topic>` once onboarded).

## Slash commands

Two slash commands ship with the repo, in `.claude/commands/`:

- **`/onboard`** — runs the 5-step onboarding playbook.
- **`/digital-journalist <topic>`** — runs the full two-stage research → write protocol with both rounds of clarifying questions in the conversation.

**Claude Code** loads them automatically from `.claude/commands/` when the agent starts in this repo.
**Codex CLI** reads slash commands from `~/.codex/prompts/` (user-level only) — run `bash scripts/install-slash-commands.sh` once to copy them there. Other agents without a slash system: the markdown files are plain prompts; the body is the spec you should follow when the user says "run the digital journalist on X."

## Running a job (two stages, two rounds of questions)

A workflow is headless and cannot prompt mid-run, so clarifying questions live in the conversation.

1. **Round 1 (scope):** quick scan (`python3 tools/api/search.py "<topic>" --count 4 --aggregate`), ask 2–4
   questions (angle, audience, POV, must-include), then run **Stage 1**:
   `Workflow({ name: "digital-journalist", args: { topic, angle, audience, pov, clarifications, mustInclude, timestamp } })`
   → builds `articles/<slug>/master.md`, `verification.md`, `synthesis.md`, and `research/round2-questions.md`. **Stops before writing.**
2. **Round 2 (voice/POV):** read `articles/<slug>/research/round2-questions.md`, ask those evidence-informed
   questions (where to land, voice, what to lead with), then run **Stage 2**:
   `Workflow({ scriptPath: "dj-write.workflow.js", args: { srcFolder, outFolder, topic, audience, stance, voice, leadWith, emphasize, timestamp } })`
   → writes `article.md`, `sources.md`, `titles.md`, `meta.json`; updates memory.

Set `outFolder` ≠ `srcFolder` to spin a new angle off the same research (no re-research).

> **If your agent has no Workflow runtime** (Codex, Openclaw, etc.): the `Workflow({...})` calls above are
> Claude Code-specific. Run the **same methodology as a guided process** — read `digital-journalist.workflow.js`
> and `dj-write.workflow.js` as the spec, then drive the phases yourself (scope → 6–8 lens searches via
> `tools/api/search.py` → `master.md` → adversarial verification → `synthesis.md` → ask Round 2 → write →
> titles → memory), writing the same files to `articles/<slug>/`. Onboarding, the search aggregator, secure
> key storage, and every `scripts/` helper are plain Python/shell and work unchanged.

## Hard rules (see CLAUDE.md for the full set)

- **Contrarian lens is mandatory**; steelman opposing views.
- **Cite or skip** — every fact/quote needs a real source URL with author, publication, date.
- **Authoritative sources first**: government/agency data, peer-reviewed work, market-research/consulting
  (Gartner, McKinsey, BCG, IDC), and company comparables — not journalism/blogs alone. Cite most-credible-first;
  a blog/social post never carries a load-bearing fact. Quote recognized authorities over anonymous voices.
- **Use both search systems**: native `WebSearch` + the aggregator at `tools/api/search.py` (free tiers first; paid only if enabled).
- **Memory**: read `memory/*.md` at the start of a job; the workflow updates it at the end.
- **Workflow gotchas**: the runtime forbids `Date.now()` (pass `timestamp` via args); always `JSON.parse` string
  args defensively; for heavy file-writing agents prefer schema-free returns.

## Map

```
digital-journalist.workflow.js  Stage 1 — research engine
dj-write.workflow.js            Stage 2 — schema-free writer (finish or spin-off)
onboarding/                     onboard.md playbook + onboard.py / keys_manager.py / analyze_style.py
profile/                        writer.md + writing-style.md (the user's voice; gitignored)
tools/  tools/api/              web search & fetch wrappers + the 18-provider aggregator
scripts/                        format readers, transcription, analysis, math (see scripts/README.md)
memory/                         learnings, source-quality, failure-modes, search-providers, writing-standards
articles/<slug>/                output per article
wiki/                           long-form docs
```

## Secrets

API keys live only in `tools/api/keys.env` (gitignored, `0600`, masked on display, fingerprinted).
Never print a full key, never commit one. `python3 onboarding/keys_manager.py check` audits the posture.
