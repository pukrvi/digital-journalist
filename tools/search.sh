#!/usr/bin/env bash
# Free DuckDuckGo search via ddgs.
# Usage:
#   tools/search.sh "<query>"                  # 10 results, plain text
#   tools/search.sh "<query>" 20               # 20 results
#   tools/search.sh "<query>" 10 json          # JSON output
#   tools/search.sh -n "<query>" 10            # news search
#   tools/search.sh -i "<query>" 10            # images
set -euo pipefail
export PYTHONWARNINGS=ignore
DDGS="$HOME/Library/Python/3.9/bin/ddgs"
[[ -x "$DDGS" ]] || DDGS="$(command -v ddgs)"

MODE="text"
case "${1:-}" in
  -n|--news) MODE="news"; shift ;;
  -i|--images) MODE="images"; shift ;;
  -v|--videos) MODE="videos"; shift ;;
esac

QUERY="${1:?Usage: tools/search.sh [-n|-i|-v] \"<query>\" [max=10] [json|text]}"
MAX="${2:-10}"
FMT="${3:-text}"

if [[ "$FMT" == "json" ]]; then
  "$DDGS" "$MODE" -q "$QUERY" -m "$MAX" -o json 2>/dev/null
else
  "$DDGS" "$MODE" -q "$QUERY" -m "$MAX" 2>/dev/null
fi
