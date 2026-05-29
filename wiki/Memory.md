# Memory — how it learns

The journalist reads `memory/*.md` at the start of every job and updates it at the end. Over months this is
what makes run N+1 smarter than run N.

| File | What it accumulates |
|------|---------------------|
| `learnings.md` | Durable, transferable lessons (research techniques, what worked) — one section per run. |
| `source-quality.md` | A ledger of domains found **reliable / mixed / unreliable**, with the reason and the run. |
| `failure-modes.md` | Mistakes encountered and how to avoid them (read at the start of every run). |
| `search-providers.md` | Which provider/tool suits which lens; the source-class playbook; provider quirks. |
| `writing-standards.md` | The NYT/WSJ/Bloomberg house style + the credibility/quote hierarchy (read by the writer). |

## How it's used

- **Start of a run:** the research stage loads memory and applies it (e.g., deprioritize a domain flagged
  unreliable; favor a provider noted as best for the contrarian lens).
- **End of a run:** the write stage appends what it learned — new reliable/unreliable domains, any failure
  mode, a craft note that worked.

## Examples already captured

- *Verify viral figures for aggregation drift* — a real $1,200 demo became a fictional "$1.2M budget"; check
  primaries for order-of-magnitude and conflation errors.
- *SEO-aggregator sites propagate conflated numbers* — surface-only, never cite for figures.
- *For heavy file-writing agents, prefer schema-free returns* — the structured-output failure that aborted a run.
- *Search is never the bottleneck* — free tiers were barely touched; spend on lenses/verification.

## Keeping it healthy

Memory should stay durable and transferable, not a diary. If an entry only makes sense for one article, it's
too specific — generalize it. Periodically condense the oldest run-log sections so files stay readable.
