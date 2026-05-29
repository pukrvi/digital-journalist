# Tools

Free, no-API-key research wrappers. Use these inside agents (via `Bash`) as the unlimited fallback when Claude's `WebSearch`/`WebFetch` are slow or rate-limited.

All scripts live in this directory and shell out to Python tools installed at `~/Library/Python/3.9/bin/`.

## Quick reference

| Tool | Purpose | Example |
|------|---------|---------|
| `tools/search.sh` | DuckDuckGo search | `tools/search.sh "SF middle school algebra policy" 15` |
| `tools/fetch.sh` | Clean article-body extraction | `tools/fetch.sh https://example.com/article` |
| `tools/wiki.sh` | Wikipedia summary | `tools/wiki.sh "San Francisco Unified School District"` |
| `tools/arxiv.sh` | Academic papers | `tools/arxiv.sh "math tracking detracking outcomes" 10` |
| `tools/feed.sh` | RSS/Atom feed | `tools/feed.sh https://www.sfusd.edu/rss.xml` |

## search.sh

```bash
tools/search.sh "<query>"                # 10 results, plain text
tools/search.sh "<query>" 20             # 20 results
tools/search.sh "<query>" 10 json        # JSON output (easier to parse)
tools/search.sh -n "<query>" 10          # news search
tools/search.sh -i "<query>" 10          # images
tools/search.sh -v "<query>" 10          # videos
```

DuckDuckGo doesn't require an API key and doesn't impose hard rate limits at this volume. If queries start failing with `Aborted!`, wait 30 seconds and retry — DuckDuckGo's bot detection occasionally throttles.

## fetch.sh

```bash
tools/fetch.sh <url>                     # plain markdown-style text
tools/fetch.sh <url> --json              # JSON with title, author, date, body
tools/fetch.sh <url> --xml               # structured XML
```

`trafilatura` strips navigation, ads, comments, and boilerplate. The `--json` form is the most useful for downstream parsing — it returns `title`, `author`, `date`, `hostname`, `text`.

If a fetch returns empty or 403s, fall back to Claude's `WebFetch` which uses different infrastructure.

## wiki.sh

```bash
tools/wiki.sh "<topic>"                  # summary paragraph
tools/wiki.sh "<topic>" --full           # full article text
```

Wikipedia is **Tier 3** — use for the canonical history and to surface primary-source citations, never as the citation itself. Always follow the footnotes to the underlying sources.

## arxiv.sh

```bash
tools/arxiv.sh "<query>" [max]
```

Returns title, authors, publication date, abstract, and a PDF URL. arxiv is **Tier 1–2** depending on whether the paper is published vs. preprint. Always note the publication status.

## feed.sh

```bash
tools/feed.sh <rss-or-atom-url> [max]
```

For ongoing topics, RSS feeds from authoritative outlets give you the most recent items without needing search. Useful when scoping a topic with a long news arc.

## Composing

Common pattern — search then fetch the top result body:

```bash
URL=$(tools/search.sh "your query" 5 json | jq -r '.[0].href')
tools/fetch.sh "$URL" --json | jq -r '.text' | head -50
```

Or get all 10 result bodies in a loop:

```bash
tools/search.sh "your query" 10 json | jq -r '.[].href' | while read url; do
  echo "=== $url ==="
  tools/fetch.sh "$url" --json | jq -r '"\(.title)\n\(.date)\n\(.text[:1500])"'
  echo
done
```

## Maintenance

If a tool stops working after a system update:

```bash
python3 -m pip install --user --upgrade ddgs trafilatura wikipedia-api arxiv feedparser
```

The `~/Library/Python/3.9/bin/` path is added to `~/.zshrc` so the binaries are available in new shells.
