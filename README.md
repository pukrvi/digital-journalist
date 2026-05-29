<div align="center">

# 📰 Digital Journalist

**An agentic, self-improving newsroom that does the work of a high-quality investigative journalist.**

Give it a topic. It reads the ocean — 15–25 sources across 6–8 lenses — adversarially fact-checks the
load-bearing claims, then writes a fully-cited, NYT/WSJ/Bloomberg-grade article *in your voice*.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
![Agents: Claude Code · Codex · Openclaw](https://img.shields.io/badge/agents-Claude_Code_·_Codex_·_Openclaw-6E56CF)
![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-3776AB)
![Search providers: 18](https://img.shields.io/badge/search_providers-18-0A9396)
![Status: production](https://img.shields.io/badge/status-production-2E7D32)

</div>

---

> "What if you absolutely boiled the ocean? If you were a human this would take a month. You can just zap
> the rocks harder… you should token-max." — the philosophy behind this project ([Idea.md](Idea.md))

Most "AI writers" do shallow, single-pass summarization. The Digital Journalist does the opposite: it
**token-maxes research**, **cross-references conflicting sources**, **tries to refute its own findings**,
and only then writes — synthesizing insight that existed in *no single source*. It runs entirely inside
your AI coding agent (Claude Code, Codex, Openclaw) and uses **free search APIs by default**.

## ✨ What makes it different

- **Boil the ocean.** 6–8 research lenses in parallel (mainstream, **contrarian (mandatory)**, data,
  historical, stakeholder, expert, comparative, follow-the-money), each gathering 6–10 sources.
- **Adversarial verification.** Before writing, it extracts the 8–12 load-bearing claims and *tries to
  refute each one* — catching the conflated, viral, and single-tweet "facts" that fool one-pass tools.
- **Authoritative sources first.** A hard mandate to reach for government/agency data, peer-reviewed work,
  and market-research/consulting (Gartner, McKinsey, BCG, IDC) — and to cite most-credible-first.
- **Writes in *your* voice.** Onboarding learns your style from a sample you've written; finished drafts
  sound like you, not generic AI.
- **Two rounds of clarifying questions** — scope up front, then *evidence-informed* questions about voice
  and angle once the research is in, so your POV comes through.
- **Self-improving memory.** Every run updates `memory/*.md` — reliable vs. unreliable sources, failure
  modes, what worked. The next article starts smarter.
- **Free by default.** DuckDuckGo works with zero setup; add free Tavily/Serper/Gemini/Brave keys for a
  wider net. Paid deep-research (Perplexity, etc.) is opt-in and only runs after the free pass.

## 🚀 Install

**Prerequisites:** macOS or Linux · Python 3.9+ · Node 18+ · `git` · (macOS) Homebrew. The setup script
installs everything else (ffmpeg, whisper.cpp, ripgrep, and the Python libraries).

```bash
git clone https://github.com/<your-org>/digital-journalist.git && cd digital-journalist
bash scripts/setup.sh           # Python libs + ffmpeg + whisper.cpp + ripgrep + whisper model
python3 scripts/check_deps.py   # verify everything is green
```

## ▶️ Run it in your agent

The Digital Journalist runs *inside* an AI coding agent. Install one, open this folder, **onboard once**
(~5 min), then ask for an article.

### Claude Code — full native experience
```bash
npm install -g @anthropic-ai/claude-code     # or: curl -fsSL https://claude.ai/install.sh | bash
cd digital-journalist && claude              # launch the agent in the repo
```
Then, inside Claude Code:
- **`/onboard`** — the 5-step setup (auto-loaded from `.claude/commands/`).
- **`Run the digital-journalist on: <your topic>`** — runs the two-stage engine (the `digital-journalist`
  named workflow → `dj-write`), pausing for the two rounds of questions.

### OpenAI Codex CLI
```bash
npm install -g @openai/codex                 # or: brew install --cask codex
cd digital-journalist && codex               # reads AGENTS.md on launch
```
Then type: **`Onboard me`** (runs `onboarding/onboard.md`), then **`Write a digital-journalist article on: <topic>`**.

### Openclaw / other agents
Install per the agent's own docs, open this folder, and say **`Read AGENTS.md and onboard me`**. Any agent
that can run shell + Python and read `AGENTS.md` / `CLAUDE.md` works.

> **One caveat, stated plainly.** The two-stage **engine** (`*.workflow.js`) uses Claude Code's parallel
> **Workflow runtime** — that's where Claude Code shines (dozens of research agents fanned out at once). On
> Codex, Openclaw, and others, the **same methodology runs as a guided process**: the agent follows the
> playbook in `AGENTS.md` / `CLAUDE.md`, driving the lenses → verification → write phases itself with the
> shared `tools/` and `scripts/`. **Onboarding, secure key storage, the 18-provider search aggregator, and
> all helper scripts are 100% cross-agent** (plain Python/shell).

That's the whole loop: quick scan → scoping questions → research → evidence-informed voice/angle questions → article.

## 🧭 How it works — two stages, two rounds of questions

A headless workflow can't stop to ask you things, so the journalist runs in two stages with a round of
clarifying questions before each. Research (~80% of the cost) becomes a **durable checkpoint** — a write
hiccup costs minutes, not the whole job.

```
         ROUND 1  ──────────────►  STAGE 1: RESEARCH  ──────────────►  ROUND 2  ──────────►  STAGE 2: WRITE
   (scope: angle,            (digital-journalist.workflow.js)     (voice/POV, informed     (dj-write.workflow.js)
    audience, POV)            scope → 6-8 lenses → master           by the evidence:         brief → article →
                              dossier → adversarial verify →        where to land, what       10 SEO titles →
                              fill gaps → synthesize →              to lead with)             meta → update memory
                              propose Round-2 questions                                       (schema-free)
                                      │                                                              │
                                      ▼                                                              ▼
                         articles/<slug>/master.md                                   articles/<slug>/article.md
                         + verification.md + synthesis.md                            + sources.md + titles.md
                         + research/round2-questions.md                              + meta.json
```

Run Stage 2 with `outFolder` == `srcFolder` to finish a run, or `outFolder` ≠ `srcFolder` to spin a
**new angle off the same research** — no re-researching. (That's how the two example articles below were made.)

Full detail: **[CLAUDE.md](CLAUDE.md)** · the **[Wiki](wiki/Home.md)**.

## 🔎 Search providers (18, free-first)

The aggregator (`tools/api/search.py`) fans out across every provider you've enabled and de-duplicates the
results. Routing is hard-coded: **keyless → free-with-key (within limits) → paid (only if you turn it on).**

| Tier | Providers | Setup |
|------|-----------|-------|
| **Keyless** | DuckDuckGo (+ Jina, LangSearch) | none — works now |
| **Free with key** | Tavily · Serper · Gemini · Brave · SerpApi · Exa · Firecrawl · Google CSE · You.com · NewsAPI · Cohere | onboarding Step 5 |
| **Paid (opt-in)** | Perplexity · OpenAI · Anthropic · xAI Grok | set `ALLOW_PAID=1` |

`python3 tools/api/search.py --status` shows what's wired up. One full article in testing used ~340
DuckDuckGo + ~56 Tavily + ~56 Serper + 16 Gemini calls — a rounding error against the free tiers. See the
[Search Providers wiki](wiki/Search-Providers.md).

## 🔐 Security: your keys never leave your machine

API keys must stay usable, so they can't be one-way hashed — instead they're protected the way real tools
protect them, and we're honest about it:

- Stored **only** in `tools/api/keys.env` — **gitignored**, `chmod 0600` (owner-only).
- **Masked** on every display (first 4 + last 4); **fingerprinted** (SHA-256) so you can confirm which key
  is loaded without exposing it.
- Optional **encryption at rest**: `python3 onboarding/keys_manager.py lock`.
- Audit anytime: `python3 onboarding/keys_manager.py check`.

## 🧰 What's in the box

- **Onboarding** — a 5-step, ~5-minute LLM-native flow that learns you and connects your search providers.
- **18-provider search aggregator** with usage tracking and free-tier limits.
- **30+ helper scripts** (`scripts/`) — read PDF/DOCX/XLSX/PPTX/EPUB/HTML, download & transcribe video
  (whisper.cpp), corpus search, pattern/finance/stats analysis, format conversion.
- **Self-improving memory** (`memory/`) — learnings, source-quality ledger, failure modes, provider tips,
  and a NYT/WSJ/Bloomberg writing-standards guide.

## 📂 Repository layout

```
digital-journalist.workflow.js   Stage 1 — research engine (named skill via .claude/workflows/)
dj-write.workflow.js             Stage 2 — schema-free writer (finish a run or spin a new angle)
CLAUDE.md / AGENTS.md            operating manuals for AI agents
onboarding/                      onboard.md playbook + onboard.py · keys_manager.py · analyze_style.py
profile/                         your writer.md + writing-style.md (gitignored; templates tracked)
tools/                           search.sh · fetch.sh · wiki.sh · arxiv.sh · feed.sh
tools/api/                       18-provider aggregator, keys.env.example, limits, usage
scripts/                         format readers, media, analysis, math (see scripts/README.md)
memory/                          learnings · source-quality · failure-modes · search-providers · writing-standards
examples/                        two finished sample articles (real output)
wiki/                            long-form documentation
articles/<slug>/                 your output: article.md · master.md · titles.md · sources.md · research/
```

## 📑 Example output

Two finished, fully-cited articles (built from one shared research dossier) live in [`examples/`](examples/):

- **The AI Cost Reckoning** — does replacing workers with AI actually save money? (3,682 words, 28 sources)
- **The AI Job Apocalypse: Is the Fear Real?** — the labor angle off the same research (3,552 words, 25 sources)

Both show the house standard: anecdotal lede → nut graf → evidence sections → steelmanned contrarian turn
→ an honest "What we don't know" → kicker, with every quote and statistic traced to a tiered source.

## 📖 Documentation

| Doc | What |
|-----|------|
| [CLAUDE.md](CLAUDE.md) | Full operating manual (the agent reads this) |
| [Wiki → Home](wiki/Home.md) | Index of all guides |
| [Wiki → Onboarding](wiki/Onboarding.md) | The 5-step flow in detail |
| [Wiki → Architecture](wiki/Architecture.md) | Two-stage design, phases, recovery |
| [Wiki → Search Providers](wiki/Search-Providers.md) | All 18, signup links, limits |
| [Wiki → Writing & Sources](wiki/Writing-and-Sources.md) | House style + credibility hierarchy |
| [Wiki → Security](wiki/Security.md) | How keys are stored |
| [Wiki → Memory](wiki/Memory.md) | How it learns |
| [Wiki → FAQ](wiki/FAQ.md) | Common questions |

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Issues and PRs welcome.

## 📜 License & attribution

Licensed under the **[Apache License 2.0](LICENSE)** — free to use, modify, and distribute, with attribution.

**Created by Puneet Vishnawat.**
Source code © 2026 **INFINITIGRID TECHNOLOGIES (OPC) PRIVATE LIMITED**. See [NOTICE](NOTICE).

Inspired by the "boil the ocean" methodology Garry Tan described for garrys.org.
