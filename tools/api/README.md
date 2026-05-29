# tools/api — Web search aggregator

A unified harness over 18 web-search providers (keyless, free-with-key, and paid deep-research). One key file, one router, automatic usage tracking, and a policy that exhausts free options before touching paid.

## Why

For the Digital Journalist's "boil the ocean" research, no single search engine gives full coverage. Brave has an independent index. Tavily is optimized for AI. Gemini gives Google's own grounding. Exa does semantic. Perplexity does deep research. This harness lets the journalist fan out across all of them in one call.

## Files

```
tools/api/
├── keys.env                # YOUR keys (gitignored). Edit this.
├── keys.env.example        # template with signup links
├── limits.json             # free-tier limits per provider
├── usage.json              # auto-tracked usage per period (created on first call)
├── _common.py              # shared helpers (key loading, usage tracking, normalize)
├── search.py               # unified router — START HERE
├── ping.py                 # health check for all providers
│
├── ddg.py                  # DuckDuckGo (keyless)
├── jina.py                 # Jina Reader (keyless URL reader; key for SERP)
├── langsearch.py           # LangSearch
├── brave.py                # Brave Search + AI Summarizer
├── tavily.py               # Tavily
├── serper.py               # Serper.dev (Google SERP)
├── serpapi.py              # SerpApi (Google + Scholar + News)
├── exa.py                  # Exa neural search + contents
├── firecrawl.py            # Firecrawl search + scrape
├── google_cse.py           # Google Programmable Search
├── you_com.py              # You.com search + RAG
├── newsapi.py              # NewsAPI.org
├── gemini.py               # Google AI Studio (Gemini + Search grounding)
├── cohere_search.py        # Cohere Command-R/R+ with web-search connector
├── perplexity.py           # Perplexity Sonar (PAID)
├── openai_search.py        # OpenAI gpt-4o-search-preview (PAID)
├── anthropic_search.py     # Claude with web_search tool (PAID)
└── xai_grok.py             # xAI Grok with Live Search (PAID)
```

## Quick start

```bash
# See what's wired up and what needs keys
python3 tools/api/search.py --status

# Fan out across every available free provider, dedupe results
python3 tools/api/search.py "SF middle school algebra policy"

# Aggregated JSON for an agent to consume
python3 tools/api/search.py "topic" --aggregate --json

# Use a specific provider
python3 tools/api/search.py "topic" --provider tavily

# Include paid providers (after free)
python3 tools/api/search.py "topic" --paid
```

## Routing policy

Hard rules baked into `search.py`:

1. **Keyless providers always run** (currently: DuckDuckGo, with Jina/LangSearch keyless when their endpoints allow).
2. **Free-tier providers with a key, within their monthly/daily limit, run by default.** Usage is tracked in `usage.json` per `period_token` (`YYYY-MM-DD` for daily, `YYYY-MM` for monthly). When a limit is exhausted, that provider is silently skipped until the next period.
3. **Paid providers (Perplexity, OpenAI, Anthropic, xAI Grok) are gated.** They run only when:
   - `ALLOW_PAID=1` is set in `keys.env`, OR
   - `--paid` is passed to `search.py`, OR
   - The individual script is invoked with `--force-paid`.
4. **Order:** the router fans out in parallel, so "after free" means "paid is excluded from the default fan-out", not "paid runs sequentially after free."

To get the "free first, paid as fallback only if results are thin" behavior, run two calls — first without `--paid`, then with — and merge in your own code.

## Provider table

| Provider | Tier | Free quota | Key env var | Best for | Signup |
|---|---|---|---|---|---|
| DuckDuckGo | keyless | unlimited* | — | general fallback | n/a |
| Jina Reader | keyless†/free | ~200/day | `JINA_API_KEY` | URL → clean text, SERP | https://jina.ai |
| LangSearch | free | unspecified | `LANGSEARCH_API_KEY` | LLM-grounding | https://langsearch.com |
| Brave | free | 2,000/month | `BRAVE_API_KEY` | independent index, AI summary | https://brave.com/search/api/ |
| Tavily | free | 1,000/month | `TAVILY_API_KEY` | AI-agent context | https://tavily.com |
| Serper | free | 2,500 one-time | `SERPER_API_KEY` | fast Google SERP | https://serper.dev |
| SerpApi | free | 100/month | `SERPAPI_API_KEY` | Google + Scholar + News | https://serpapi.com |
| Exa | free | $10 credits | `EXA_API_KEY` | neural/semantic search | https://exa.ai |
| Firecrawl | free | 500-1k/month | `FIRECRAWL_API_KEY` | LLM-ready scraping | https://firecrawl.dev |
| Google CSE | free | 100/day | `GOOGLE_CSE_API_KEY` + `GOOGLE_CSE_CX` | Google's own index | https://programmablesearchengine.google.com |
| You.com | free | 100/day | `YOU_API_KEY` | real-time web | https://api.you.com |
| NewsAPI | free | 100/day | `NEWSAPI_API_KEY` | news, 150k+ sources | https://newsapi.org |
| Gemini | free | 1,500/day | `GEMINI_API_KEY` | Google Search grounding | https://aistudio.google.com |
| Cohere | free | trial | `COHERE_API_KEY` | Command R+ web-search | https://cohere.com |
| Perplexity | **paid** | — | `PERPLEXITY_API_KEY` | sonar-deep-research | https://docs.perplexity.ai |
| OpenAI | **paid** | — | `OPENAI_API_KEY` | gpt-4o-search-preview | https://platform.openai.com |
| Claude | **paid** | — | `ANTHROPIC_API_KEY` | claude w/ web_search tool | https://console.anthropic.com |
| xAI Grok | **paid** | — | `XAI_API_KEY` | Grok Live Search | https://docs.x.ai |

\* DuckDuckGo throttles via bot detection. † Jina Reader anonymous endpoint can return 401 lately; signup recommended.

## Adding a key

1. Sign up at the provider link.
2. Paste the key into `tools/api/keys.env`:
   ```
   BRAVE_API_KEY=BSA…your…key
   ```
3. `python3 tools/api/ping.py` should now show that provider as `OK`.

Keys live in `tools/api/keys.env` only — do **not** commit (already in `.gitignore`). When you need to rotate, edit that file once and every script picks it up automatically (loaded on import).

## Output schema

Every provider returns:

```json
{
  "provider": "brave",
  "tier": "free",
  "query": "...",
  "ok": true,
  "error": null,
  "ai_summary": "AI-generated answer (if the provider supports it)",
  "results": [
    {
      "title":   "...",
      "url":     "...",
      "snippet": "...",
      "date":    "YYYY-MM-DD or null",
      "score":   0.92,
      "extra":   {}
    }
  ],
  "extra": {},
  "usage_after": { "used": 5, "limit": 2000, "remaining": 1995, "period": "month" }
}
```

When `search.py --aggregate` is used (default for fan-out), results across providers are deduplicated by normalized URL, sorted by source-count (cross-provider agreement = signal), and each carries a `sources: [provider1, provider2]` array.

## Usage tracking

`usage.json` is a simple counter keyed by provider + period token. It's read at every call. Reset a provider by editing `usage.json` and removing the relevant key — useful when you've upgraded to a paid tier.

## Per-provider CLI

Every provider also runs standalone:

```bash
python3 tools/api/ddg.py "topic" --news
python3 tools/api/brave.py "topic" --summary
python3 tools/api/tavily.py "topic" --depth advanced
python3 tools/api/exa.py search "neural search" --type neural
python3 tools/api/exa.py contents https://arxiv.org/abs/2310.11511 --highlights
python3 tools/api/gemini.py "topic"
python3 tools/api/perplexity.py "topic" --deep --force-paid
```

All accept `--json` for structured output.

## Memory hook

When the digital-journalist workflow runs, it consults `memory/search-providers.md` to know which providers were most useful for past topics. After each run, it updates that file. See [memory/search-providers.md](../../memory/search-providers.md).
