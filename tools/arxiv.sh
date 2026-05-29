#!/usr/bin/env bash
# Search arxiv.org for academic papers.
# Usage:
#   tools/arxiv.sh "<query>"                   # 10 most relevant
#   tools/arxiv.sh "<query>" 20                # 20 results
set -euo pipefail
export PYTHONWARNINGS=ignore

QUERY="${1:?Usage: tools/arxiv.sh \"<query>\" [max=10]}"
MAX="${2:-10}"

python3 - <<PYEOF "$QUERY" "$MAX"
import sys, arxiv
query, max_n = sys.argv[1], int(sys.argv[2])
client = arxiv.Client()
search = arxiv.Search(query=query, max_results=max_n, sort_by=arxiv.SortCriterion.Relevance)
for r in client.results(search):
    print(f"## {r.title}")
    print(f"Authors: {', '.join(a.name for a in r.authors)}")
    print(f"Published: {r.published.date()}")
    print(f"URL: {r.entry_id}")
    print(f"PDF: {r.pdf_url}")
    print(f"Abstract: {r.summary.strip()}")
    print()
PYEOF
