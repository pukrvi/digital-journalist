#!/usr/bin/env python3
"""Search across all research files for a phrase / regex. Wraps ripgrep with article-aware output.

Usage:
    corpus_search.py "algebra tracking"                 # search all articles' research/
    corpus_search.py "(?i)NBER|peer.review" --regex     # regex
    corpus_search.py "algebra" --article sf-algebra      # one article only
    corpus_search.py "tax credit" --files-only           # just list matching files
    corpus_search.py "ratio" --context 3                 # 3 lines of context
"""
import argparse
import os
import shutil
import subprocess
import sys


def find_project_root():
    cur = os.getcwd()
    while cur != "/":
        if os.path.isdir(os.path.join(cur, "articles")) and os.path.isfile(os.path.join(cur, "CLAUDE.md")):
            return cur
        cur = os.path.dirname(cur)
    return os.getcwd()


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query")
    ap.add_argument("--regex", action="store_true", help="treat query as regex")
    ap.add_argument("--article", help="restrict to articles/<name>/")
    ap.add_argument("--files-only", "-l", action="store_true")
    ap.add_argument("--context", "-C", type=int, default=2)
    ap.add_argument("--case", action="store_true", help="case-sensitive (default: smart-case)")
    a = ap.parse_args()

    if not shutil.which("rg"):
        print("ERROR: ripgrep (rg) not installed. Install: brew install ripgrep", file=sys.stderr)
        sys.exit(2)

    root = find_project_root()
    if a.article:
        search_path = os.path.join(root, "articles", a.article)
        if not os.path.isdir(search_path):
            print(f"ERROR: no article named {a.article} at {search_path}", file=sys.stderr); sys.exit(2)
    else:
        search_path = os.path.join(root, "articles")
        if not os.path.isdir(search_path):
            print("ERROR: no articles/ folder found", file=sys.stderr); sys.exit(2)

    cmd = ["rg", "--color=never", "--heading", "--line-number"]
    if not a.case:
        cmd.append("--smart-case")
    if not a.regex:
        cmd.append("--fixed-strings")
    if a.files_only:
        cmd.append("-l")
    else:
        cmd += ["-C", str(a.context)]
    cmd += [a.query, search_path]
    sys.exit(subprocess.call(cmd))


if __name__ == "__main__":
    main()
