# Learnings

A durable log of techniques and insights from past article runs. The workflow appends to this file at the end of every run. Older sections may be condensed when this file exceeds ~300 lines.

Each entry should be actionable for an unrelated future article — not ephemera.

## Seed learnings (pre-first-run)

- **Search the contrarian framing explicitly.** Don't just search `"<topic>"` — also search `"<topic> debunked"`, `"<topic> criticism"`, `"why <conventional wisdom> is wrong"`. The contrarian view is rarely on the first page of a neutral query.
- **Primary sources beat aggregators.** When a news article cites a "report," find and read the report. Half the time the article misrepresents it.
- **Date every quote.** A quote from 2014 about a 2024 issue is suspect. Capture publication dates as part of source metadata.
- **Diversify outlets.** If half your sources are from one publication, you've inherited that outlet's blind spots. Force diversity by tagging each source's publication and reviewing the distribution.
- **Steelman is a search query.** "best argument for <unpopular view>" returns better contrarian material than "<unpopular view> arguments."

---

## Run log

(Each completed run appends a section below.)

### Run: the-ai-cost-reckoning (2026-05-29)

**Topic:** The AI cost reckoning — does replacing workers with AI actually save money?

**Outcome:** The master evidence dossier reached ~12 verified claims, each carried with an explicit confidence grade (e.g., C1 0.93 on the Uber four-month coding-tools-budget burn; C8 0.88 on the Meta "Claudeonomics" leaderboard; C10 0.90 on the Microsoft standardization-not-rejection framing; C2 0.78 on the "$1.2M Uber" figure being a conflation). Confidence-graded claims made it easy to decide what the article could assert as fact versus what had to be hedged as "reported but not confirmed in the accessible primary." Research was salvaged and the run finished via the schema-free finisher (dj-finisher) after the original run aborted on a StructuredOutput miss.

**Strongest durable lessons (apply to future runs):**
- **Verify viral figures for aggregation drift / conflation.** The most-circulated specifics degraded as they traveled: a real $1,200 Uber demo became a fictional "$1.2M budget" (1000x unit error or a conflation with OpenAI's $1.3M 3-person OpenClaw team); a real Meta token leaderboard spawned an uncorroborated "$500K/month engineer" figure from a single X post. When a number is going viral, find the primary and check for (a) order-of-magnitude unit errors and (b) two different stories being merged into one.
- **Name-entity traps.** Lenses split on whether the Uber "5,000 engineers / 32%→84% adoption / $150–$2,000 per engineer / 70% AI code" cluster was confirmed; the trail ran to The Information (paywalled) + a possibly-leaked all-hands, and aggregators mis-attributed it to Fortune and invented a "CTO confirmed" quote. When an attribution chain forks, state only what the accessible primary confirms as fact and tier the rest explicitly.
- **Token-price deflation is the key steelman to the cost-reckoning thesis.** The strongest counter to "AI replacement saves money / AI bills are exploding" is that per-token inference cost is collapsing (Epoch, Stanford HAI: ~280x cheaper for GPT-3.5-class in ~18 months; Gartner forecasts ~90% cheaper inference by 2030) — even the honest mainstream position carries the deflation curve and the demand-explosion curve (Goldman: 24x tokens by 2030) side by side, so the real verdict is "net direction depends on the workflow," not a settled answer. Lead the contrarian section with deflation, not with cherry-picked success stories.

### Run: the-ai-job-apocalypse-is-the-fear-real (2026-05-29) — spinoff

**Topic:** The AI job apocalypse — is the fear real? (labor-displacement angle)

**Outcome:** A second, distinct article produced from the *same* dossier as the-ai-cost-reckoning. Research, master.md, and verification.md were reused (not re-run); only the synthesis, article, titles, and sources are new.

**Durable lesson — spinning a distinct angle off shared research:**
- **Read the individual lens files, not master.md alone.** master.md is already compressed to the cost-reckoning thesis; its confidence-graded claims are the right *spine*, but the original-angle material (e.g., the Dallas Fed entry-level findings, the Altman/Amodei walkbacks, "AI washing" as a layoff cover, augment-vs-replace splits) lives in the per-lens `research/*.md` files. Going back to the lens files surfaced the labor-displacement evidence that master.md had pruned as off-thesis. For any spinoff, treat master as the verified fact-set and the lens files as the un-pruned raw material for the new angle.
- **A spinoff is a re-lede and re-sequence, not a re-summary.** Reusing the same sources for a new question means rebuilding the narrative arc (here: "the bloodbath that never showed up" → entry-level ladder erosion → AI-washing → the forecasters' own recants), re-picking which claim leads, and writing fresh headlines/sources — not lightly editing the companion article. If the synthesis reads like the first piece with words swapped, the angle hasn't actually shifted. Cross-link the two via meta.json `companionArticle` + a README pointer so readers can find the shared evidence base.

### Process upgrade: v3 two-stage architecture (2026-05-29)

**What changed and why:**
- **Split the monolith into Stage 1 (research → `digital-journalist`) and Stage 2 (write → `dj-write`).** The v2 monolith lost ~2 hours / 2.1M tokens when one end-of-run agent missed its StructuredOutput. Research is ~80% of the cost; making the dossier a durable checkpoint means a write-stage hiccup costs minutes. Stage 2 is schema-free (writes files + returns text), which structurally cannot hit that failure — proven by the finisher/spinoff runs (~350-500k tokens, ~20 min, 0 failures).
- **Two rounds of clarifying questions.** Round 1 (scope) before research; Round 2 (voice/POV/lede) *after* the evidence is in, generated by the engine into `research/round2-questions.md` and grounded in actual findings. A writer's POV should be formed by the evidence, not guessed before it — and the two-stage split is what makes a mid-job question physically possible (headless workflows can't prompt).
- **Source-class mandate + credibility/quote hierarchy** baked into prompts and `writing-standards.md`: actively seek government/agency, consulting/market-research, and comparable-company sources; cite most-credible-first; quote recognized authorities over anonymous voices (anonymous = color only).

**Durable lessons:**
- **For very large file-writing agents, prefer schema-free (write file + return short text) over schema returns.** Reserve schemas for small control-flow returns (scope, lens summaries, verdicts). Heavy "write a big document AND return JSON" agents are the fragile ones.
- **Always JSON.parse string args defensively** — the harness sometimes delivers `args` as a JSON string; assuming a string is the bare topic mangles the slug and drops every other arg.
- **Checkpoint expensive work to disk** so any failure is recoverable; never make a 2-hour run all-or-nothing on a final structured return.
- **Search was never the bottleneck.** One full article used DDG 342 / Serper 56 / Tavily 56 / Gemini 16 — a rounding error against the free tiers. Spend the budget on more lenses/verification, not more providers.
