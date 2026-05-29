# Search providers — when to reach for which

Updated at the end of every digital-journalist run. The workflow consults this file during the scoping phase to pick the best providers for the topic at hand.

See [`tools/api/README.md`](../tools/api/README.md) for full signup links + quotas.

## When to use which

| Lens / need | Best provider(s) | Why |
|---|---|---|
| Quick general scan | `duckduckgo`, `serper` | Unlimited and fast SERP. Always run first. |
| Independent index (escape Google's bubble) | `brave` | Brave's index is built independently — surfaces sources Google's algo deprioritizes. |
| Academic / peer-reviewed | `serpapi --engine google_scholar`, `arxiv` (in tools/) | Scholar surfaces papers; arxiv for preprints. |
| Recent news | `newsapi`, `brave --news`, `serper --news` | NewsAPI has the widest source list; Brave news is independent. |
| AI-ready context (LLM consumption) | `tavily`, `firecrawl`, `exa contents` | All return clean text optimized for grounding. |
| Semantic / "find similar" | `exa` | Neural search beats keyword for conceptual queries. |
| Real-time / very recent | `gemini`, `you_com`, `xai_grok` | Live web grounding; Grok has unique X/Twitter signal. |
| Deep multi-step research | `perplexity --deep`, `anthropic_search`, `openai_search` | Paid; produces synthesized, cited reports. Use after free pass. |
| URL → clean body text | `jina read`, `firecrawl scrape` | Strips boilerplate better than naive HTTP. |
| Restricted to specific domains | `google_cse --site domain.com` | CSE lets you scope at search time. |

## Source-class playbook (MANDATE — reach for these every run, not just journalism)

The default failure is over-relying on news/blogs. For every topic deliberately query for each class below.

| Source class | How to reach it | Notes |
|---|---|---|
| **Government / agency (Tier 1)** | `site:bls.gov` / `site:census.gov` / `site:*.federalreserve.org` / `site:dallasfed.org` / `site:cbo.gov` / `site:gao.gov` / `site:oecd.org` / `site:imf.org` / `site:worldbank.org` / `site:sec.gov` via `google_cse --site` or aggregator; `bash tools/api/search.py "<topic> BLS OR Census OR Federal Reserve data"` | The regional Feds (Dallas/SF/St. Louis FRED) are gold for labor/econ. SEC EDGAR for company filings. |
| **Peer-reviewed / academic (Tier 1)** | `bash tools/arxiv.sh "<q>"` (mark preprint); `google_cse --site nber.org`; university lab sites (Stanford HAI/Digital Economy Lab, MIT) | Verify preprint vs version-of-record. |
| **Market research & consulting (Tier 2-3)** | `bash tools/api/search.py "<topic> Gartner OR Forrester OR IDC OR McKinsey OR BCG OR Bain OR Deloitte report"` | Name firm + report + date; note the commercial incentive. Press releases are free; full reports often paywalled — cite the dated release. |
| **Comparables / peers (Tier 1-2)** | search the focal company's competitors + their filings/earnings calls | Triangulate — never let one firm's self-report be the whole basis. |
| **Established journalism (Tier 2)** | aggregator default (Serper/Tavily surface these) | Strong baseline; still verify big numbers against Tier 1. |

**(run: the-ai-cost-reckoning) what worked:** the Dallas Fed wage series, Gartner/Forrester press releases, Stanford Digital Economy Lab, and SEC-adjacent disclosures were the load-bearing Tier 1-2 anchors; the viral figures that needed debunking all came from SEO-aggregator blogs. The lesson is baked into the engine: research prompts now carry a SOURCE_PRIORITY block and lens agents report which classes they reached.

## Provider quirks (running notes — updated by runs)

(Seed observations; runs append below.)

- **DuckDuckGo** throttles after bursts (~50 queries in a minute). Stagger calls or run in batches with `time.sleep(2)`.
- **Brave Summarizer** requires two calls: first SERP with `summary=1`, then poll `/summarizer/search?key=...`. The summarizer key can take 1-2 seconds to populate; if first poll returns empty, retry once after a 1s delay.
- **Jina Reader** anonymous endpoint returns 401 as of late 2025/early 2026. Need a key now even for `r.jina.ai`.
- **Gemini** grounding only attaches `grounding_chunks` when the model actually used search. If a query doesn't trigger search (model thinks it knows), no citations are returned.
- **Tavily `search_depth=advanced`** costs 2x credits but returns far better snippets — worth it for the contrarian lens.
- **Perplexity `sonar-deep-research`** can use 50k+ tokens per call. Token-max, but check your spend.
- **Exa neural search** works best with declarative phrasings ("a study on X") rather than questions ("what is X?").
- **SerpApi** has the best Google Scholar wrapper of the bunch.
- **(run: the-ai-cost-reckoning, 2026-05-29)** The free aggregator carried this entire run — **DuckDuckGo + Tavily + Serper** together surfaced essentially every source that made the dossier; no paid provider was needed. **Gemini was rate-limited intermittently** (grounding calls returned empty / 429'd mid-run), so don't make it a critical-path dependency. **Tavily's AI summaries were useful as leads** — they pointed to the right primaries fast — but each summarized claim required independent verification before it could be cited (Tavily happily summarized the aggregation-drifted figures alongside the real ones).

## Source-quality crossovers (from runs)

(Empty — populated by runs. Format: `<domain> — surfaced by <providers>, useful for <use case>, tier <1-5>.`)

## Failure modes specific to providers

(Populated by runs.)
