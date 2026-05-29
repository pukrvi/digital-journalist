# Search Providers

The aggregator (`tools/api/search.py`) is a unified harness over **18 providers**. It fans out across every
provider you've enabled, de-duplicates by URL (a URL surfaced by multiple providers is a relevance signal),
and attaches each provider's AI summary as a lead.

```bash
python3 tools/api/search.py "<query>" --count 8 --aggregate     # fan out across enabled free providers
python3 tools/api/search.py "<query>" --paid                    # include paid tier (if ALLOW_PAID=1)
python3 tools/api/search.py --status                            # what's wired up + usage
python3 tools/api/ping.py                                       # health-check every provider
```

## Routing policy (hard-coded)

**keyless → free-with-key (within limits) → paid (only if enabled).** Usage is tracked per period in
`tools/api/usage.json`; a provider self-skips when its limit is hit. Paid providers run only when
`ALLOW_PAID=1` (in `keys.env`) or `--paid`/`--force-paid` is passed.

## The 18

| Provider | Tier | Free quota | Key env | Signup |
|---|---|---|---|---|
| DuckDuckGo | keyless | unlimited\* | — | — |
| Jina Reader | keyless/free | ~200/day | `JINA_API_KEY` | jina.ai |
| LangSearch | free | varies | `LANGSEARCH_API_KEY` | langsearch.com |
| Brave | free | 2,000/mo | `BRAVE_API_KEY` | brave.com/search/api |
| Tavily | free | 1,000/mo | `TAVILY_API_KEY` | tavily.com |
| Serper | free | 2,500 once | `SERPER_API_KEY` | serper.dev |
| SerpApi | free | 100/mo | `SERPAPI_API_KEY` | serpapi.com |
| Exa | free | $10 credit | `EXA_API_KEY` | exa.ai |
| Firecrawl | free | 500–1k/mo | `FIRECRAWL_API_KEY` | firecrawl.dev |
| Google CSE | free | 100/day | `GOOGLE_CSE_API_KEY` + `GOOGLE_CSE_CX` | programmablesearchengine.google.com |
| You.com | free | 100/day | `YOU_API_KEY` | api.you.com |
| NewsAPI | free | 100/day | `NEWSAPI_API_KEY` | newsapi.org |
| Gemini | free | 1,500/day | `GEMINI_API_KEY` | aistudio.google.com |
| Cohere | free | trial | `COHERE_API_KEY` | cohere.com |
| Perplexity | **paid** | — | `PERPLEXITY_API_KEY` | docs.perplexity.ai |
| OpenAI | **paid** | — | `OPENAI_API_KEY` | platform.openai.com |
| Anthropic | **paid** | — | `ANTHROPIC_API_KEY` | console.anthropic.com |
| xAI Grok | **paid** | — | `XAI_API_KEY` | docs.x.ai |

\* DuckDuckGo throttles after bursts; the aggregator handles it gracefully.

## Which provider for which job

See [`memory/search-providers.md`](../memory/search-providers.md) — a living playbook the journalist
consults during scoping (independent index → Brave; AI-ready text → Tavily/Firecrawl; semantic → Exa;
live web → Gemini; academic → SerpApi Scholar / arxiv; deep research → Perplexity). It also carries a
**source-class playbook** for reaching government/agency, consulting/market-research, and comparable sources.

## Adding a key

```bash
python3 onboarding/keys_manager.py set tavily "tvly-..."   # or onboarding/onboard.py key --provider ...
python3 tools/api/ping.py                                  # confirm it's green
```

Real-world cost: one full boil-the-ocean article used ~340 DuckDuckGo + 56 Tavily + 56 Serper + 16 Gemini
calls. Search is **not** the bottleneck — spend on more lenses/verification, not more providers.
