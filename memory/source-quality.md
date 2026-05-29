# Source Quality Ledger

Running record of which domains have been reliable and which have not, with the reason. Updated at the end of every run. Used during scoping and verification.

## Format

```
- <domain> — <tier-when-encountered> — <reliable/mixed/unreliable> — <why> — (run: <slug>)
```

---

## Reliable

- **fortune.com** — Tier 2 — reliable — Jake Angelo's Uber/Microsoft AI-cost reporting was the most accurate primary on this beat; the article's confirmable facts (Uber's four-month coding-tools-budget burn, the real $1,200 demo figure, COO ROI doubt) all trace cleanly to Fortune, and Fortune did NOT carry the aggregation-drifted per-engineer cluster. — (run: the-ai-cost-reckoning)
- **digitaleconomy.stanford.edu / Stanford Digital Economy Lab (+ Stanford HAI AI Index)** — Tier 1 — reliable — primary source for the agentic-token-consumption mechanism (Pei et al., arXiv:2604.22750) and for the inference-deflation curve (HAI AI Index: ~280x cheaper GPT-3.5-class in ~18 mo). Note the token-consumption paper is a preprint, not yet peer-reviewed. — (run: the-ai-cost-reckoning)
- **gartner.com (press releases + Helen Poitevin)** — Tier 1/2 — reliable — the "AI layoffs may create budget room but don't deliver returns" survey (n=350, $1B+ revenue) was the strongest ROI-skeptic anchor; verbatim Poitevin "no connection or correlation" quote sourced via Computerworld. Cite the dated press release, not third-party rewrites of it. — (run: the-ai-cost-reckoning)

## Mixed (verify case-by-case)

- **The Information (via aggregators)** — Tier 2 original but paywalled — mixed-by-access — the real reporting behind the contested Uber per-engineer cluster and the vendor-margin figures (Anthropic 38%→70%, OpenAI 40%→33%) is genuine The Information journalism, but it's only reachable through aggregators that mangle and mis-attribute it. Attribute as "reported by The Information," treat the specific numbers as reported-not-audited. — (run: the-ai-cost-reckoning)

## Unreliable / avoid

- **aiweekly.co (AI Weekly)** — Tier 5 — unreliable — documented aggregation-drift vector: imported the contested Uber per-engineer cluster, mis-captioned it as Fortune-origin, and attached a "CTO Praveen Neppalli Naga confirmed" attribution that exists in no primary. NEVER cite for numbers. — (run: the-ai-cost-reckoning)
- **storyboard18.com, designrush.com, startupfortune (Startup Fortune)** — Tier 4-5 — unreliable for figures — SEO-aggregator sites that propagated the same conflated Uber/Meta/Microsoft figures; useful at most to discover that a claim is circulating, never as the source of a number. — (run: the-ai-cost-reckoning)

## Seed observations (pre-first-run)

- **Government primary data (`.gov`, `.gov.uk`, `bls.gov`, `census.gov`, `cdc.gov`)** — Tier 1 by default. Verify the URL is the actual data source, not a press release about the data.
- **Peer-reviewed (`*.edu` papers, `nber.org`, `arxiv.org`, journal sites)** — Tier 1, but check whether the paper is the version of record or a preprint.
- **Established journalism (NYT, WSJ, FT, Reuters, AP, BBC, Bloomberg, The Atlantic, ProPublica, The Economist)** — Tier 2. Strong factual baseline; opinion sections need separate treatment.
- **Wikipedia** — Tier 3 for the topic overview. Always follow the inline citations to primary sources for any specific claim.
- **Substack / personal blogs** — Tier 3 if the author is a named domain expert with a track record. Tier 4 otherwise.
- **Twitter / X, LinkedIn, Reddit** — Tier 4. Good for surfacing arguments and named individuals to look up. Never cite directly for a factual claim.
- **Content-farm aggregators, SEO blogspam, AI-generated rewrites** — Tier 5. Do not cite. Track which domains repeatedly produce this so we can deprioritize them.
