#!/usr/bin/env bash
# Pull recent items from an RSS/Atom feed.
# Usage:
#   tools/feed.sh <feed-url>                   # 20 most recent
#   tools/feed.sh <feed-url> 50                # 50 most recent
set -euo pipefail
export PYTHONWARNINGS=ignore

URL="${1:?Usage: tools/feed.sh <feed-url> [max=20]}"
MAX="${2:-20}"

python3 - <<PYEOF "$URL" "$MAX"
import sys, feedparser
url, max_n = sys.argv[1], int(sys.argv[2])
feed = feedparser.parse(url)
print(f"# {feed.feed.get('title', url)}")
print(f"Source: {url}")
print()
for e in feed.entries[:max_n]:
    print(f"## {e.get('title', 'Untitled')}")
    print(f"URL: {e.get('link', '')}")
    print(f"Date: {e.get('published', e.get('updated', 'Undated'))}")
    summary = e.get('summary', '').strip()
    if summary:
        print(f"Summary: {summary[:400]}")
    print()
PYEOF
