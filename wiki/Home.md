# Digital Journalist — Wiki

An agentic, self-improving newsroom that does the work of a high-quality investigative journalist: it boils
the ocean of sources, adversarially verifies the load-bearing claims, and writes a fully-cited article in
your voice — entirely inside your AI coding agent (Claude Code, Codex, Openclaw).

New here? Read the [README](../README.md) first, then onboard.

## Guides

- **[Onboarding](Onboarding.md)** — the 5-step, ~5-minute setup that learns you and connects your search providers.
- **[Architecture](Architecture.md)** — the two-stage design, every phase, and how recovery works.
- **[Search Providers](Search-Providers.md)** — all 18 providers, signup links, free-tier limits, routing policy.
- **[Writing & Sources](Writing-and-Sources.md)** — the NYT/WSJ/Bloomberg house style + the credibility & quote hierarchy.
- **[Security](Security.md)** — exactly how your API keys are stored.
- **[Memory](Memory.md)** — how the journalist learns and gets smarter every run.
- **[Tools & Scripts](Tools-and-Scripts.md)** — the 30+ helper scripts (readers, transcription, analysis, math).
- **[FAQ](FAQ.md)** — common questions.

## The 60-second mental model

```
You: "Run the digital-journalist on: <topic>"
  │
  ├─ Round 1 questions (angle, audience, POV)         ← in chat
  ├─ STAGE 1  research → master dossier → verify       ← digital-journalist.workflow.js
  ├─ Round 2 questions (voice, where to land)          ← in chat, informed by the evidence
  └─ STAGE 2  write → 10 SEO titles → update memory     ← dj-write.workflow.js
        │
        ▼
   articles/<slug>/article.md  (+ master.md, sources.md, titles.md, research/)
```

## Principles (non-negotiable)

1. Boil the ocean — 15–25 sources, not 1–3.
2. Contrarian by default — steelman the strongest counter-argument.
3. Cite or skip — every fact has a verifiable source.
4. Authoritative sources first — government/agency, peer-reviewed, consulting/market-research, comparables.
5. Butter to the recipe — synthesize insight no single source stated.
6. Improve every run — memory grows.

## License

Apache 2.0. Created by Puneet Vishnawat. © 2026 INFINITIGRID TECHNOLOGIES (OPC) PRIVATE LIMITED.
