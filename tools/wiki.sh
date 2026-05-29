#!/usr/bin/env bash
# Wikipedia page summary + URL via wikipedia-api.
# Usage:
#   tools/wiki.sh "<topic>"                    # summary text
#   tools/wiki.sh "<topic>" --full             # full page text
set -euo pipefail
export PYTHONWARNINGS=ignore

TOPIC="${1:?Usage: tools/wiki.sh \"<topic>\" [--full]}"
MODE="${2:-summary}"

python3 - <<PYEOF "$TOPIC" "$MODE"
import sys
import wikipediaapi
topic = sys.argv[1]
mode = sys.argv[2]
wiki = wikipediaapi.Wikipedia(user_agent="digital-journalist/1.0 (puneetv@gtmbuddy.ai)", language="en")
page = wiki.page(topic)
if not page.exists():
    print(f"NOT_FOUND: {topic}", file=sys.stderr)
    sys.exit(1)
print(f"# {page.title}")
print(f"URL: {page.fullurl}")
print()
print(page.text if mode == "--full" else page.summary)
PYEOF
