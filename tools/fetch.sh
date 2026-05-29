#!/usr/bin/env bash
# Clean article-body extraction via trafilatura.
# Strips nav, ads, footers, and boilerplate. Returns the main content.
# Usage:
#   tools/fetch.sh <url>                       # markdown-style plain text
#   tools/fetch.sh <url> --json                # JSON with metadata
#   tools/fetch.sh <url> --xml                 # XML with structure
set -euo pipefail
export PYTHONWARNINGS=ignore
TRAF="$HOME/Library/Python/3.9/bin/trafilatura"
[[ -x "$TRAF" ]] || TRAF="$(command -v trafilatura)"

URL="${1:?Usage: tools/fetch.sh <url> [--json|--xml]}"
FMT="${2:-}"

case "$FMT" in
  --json) "$TRAF" --URL "$URL" --json --no-comments 2>/dev/null ;;
  --xml)  "$TRAF" --URL "$URL" --xml  --no-comments 2>/dev/null ;;
  *)      "$TRAF" --URL "$URL" --formatting --no-comments 2>/dev/null ;;
esac
