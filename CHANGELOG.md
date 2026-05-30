# Changelog

All notable changes to the Digital Journalist. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [3.0.1] — 2026-05-30

### Added
- **`/digital-journalist <topic>` slash command** (`.claude/commands/digital-journalist.md`) — auto-loaded
  by Claude Code from the repo. Runs the full two-stage protocol (Round 1 scope → research workflow →
  Round 2 voice/POV → write workflow) directly from a slash, instead of typing the natural-language prompt.
- **`scripts/install-slash-commands.sh`** — copies `.claude/commands/*.md` into `~/.codex/prompts/` so
  `/digital-journalist` and `/onboard` also work in OpenAI Codex CLI (which only supports user-level prompts).

## [3.0.0] — 2026-05-29

The productization + reliability release.

### Added
- **LLM-native onboarding** (`onboarding/`) — a 5-step, ~5-minute flow (who you are → writing style →
  upload a sample to extrapolate voice → choose search providers → add keys), each step with a "why this
  helps." `/onboard` command for Claude Code; `onboard.md` playbook for any agent.
- **Secure key storage** (`onboarding/keys_manager.py`) — keys stored locally only, `0600`, masked on
  display, SHA-256 fingerprinted, optional encryption-at-rest (`lock`/`unlock`), and an audit (`check`).
- **Writer profile** (`profile/`) — `writer.md` + `writing-style.md`, learned at onboarding and emulated by
  the writer so drafts sound like the user.
- **Two-stage architecture** — `digital-journalist` (research) + `dj-write` (write), enabling a second,
  evidence-informed round of clarifying questions and a durable research checkpoint.
- **Source-class mandate** — research now actively seeks government/agency, consulting & market-research,
  and comparable-company sources; lenses report which classes they reached.
- **Credibility & quote hierarchy** — cite most-credible-first; quote recognized authorities over anonymous
  voices (color only). Codified in `memory/writing-standards.md` and enforced in the writer.
- Packaging: `LICENSE` (Apache 2.0), `NOTICE`, `AGENTS.md`, `CONTRIBUTING.md`, `wiki/`, `examples/`.

### Changed
- The write stage is **schema-free** (writes files, returns text) — structurally immune to the failure below.
- README rebuilt for GitHub.

### Fixed
- **Args delivered as a JSON string** mangled the slug and dropped every non-topic arg — all workflows now
  `JSON.parse` string args defensively.
- **Heavy schema agent skipped its structured output**, aborting a 2-hour run — hardened with explicit
  reminders and the schema-free write stage.

## [2.0.0] — 2026-05-29
- Master evidence dossier, adversarial verification, NYT/WSJ/Bloomberg writing standards, 10 SEO headlines,
  18-provider search aggregator, 30+ helper scripts.

## [1.0.0] — 2026-05-29
- Initial "boil the ocean" multi-lens research workflow with self-improving memory.
