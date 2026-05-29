#!/usr/bin/env python3
"""Read an EPUB. Defaults to chapter-by-chapter markdown. Useful for citing books.

Usage:
    read_epub.py book.epub                       # all chapters
    read_epub.py book.epub --toc                 # table of contents
    read_epub.py book.epub --chapter 3           # one chapter (1-indexed)
    read_epub.py book.epub --search "algebra"    # excerpts containing the phrase
    read_epub.py book.epub --json
"""
import argparse
import json
import re
import sys


def epub_chapters(path):
    from ebooklib import epub, ITEM_DOCUMENT
    book = epub.read_epub(path)
    meta = {
        "title": book.get_metadata("DC", "title")[0][0] if book.get_metadata("DC", "title") else None,
        "creator": book.get_metadata("DC", "creator")[0][0] if book.get_metadata("DC", "creator") else None,
        "language": book.get_metadata("DC", "language")[0][0] if book.get_metadata("DC", "language") else None,
    }
    chapters = []
    for item in book.get_items_of_type(ITEM_DOCUMENT):
        html = item.get_body_content().decode("utf-8", errors="replace")
        import trafilatura
        text = trafilatura.extract(html, output_format="markdown", include_comments=False) or ""
        if text.strip():
            chapters.append({"title": item.get_name(), "text": text})
    return meta, chapters


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("epub")
    ap.add_argument("--toc", action="store_true")
    ap.add_argument("--chapter", type=int, help="1-indexed chapter")
    ap.add_argument("--search", help="excerpts containing this phrase (case-insensitive)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--context", type=int, default=2, help="paragraphs of context around --search hits")
    a = ap.parse_args()
    meta, chs = epub_chapters(a.epub)

    if a.toc:
        toc = [{"index": i + 1, "title": c["title"], "chars": len(c["text"])} for i, c in enumerate(chs)]
        out = {"metadata": meta, "chapters": toc}
        print(json.dumps(out, indent=2) if a.json else "\n".join(f"{c['index']:3d}. {c['title']} ({c['chars']:,} chars)" for c in toc))
        return

    if a.chapter:
        c = chs[a.chapter - 1]
        if a.json:
            print(json.dumps({"metadata": meta, "chapter": c}, indent=2))
        else:
            print(f"# {c['title']}\n\n{c['text']}")
        return

    if a.search:
        pattern = re.compile(re.escape(a.search), re.IGNORECASE)
        hits = []
        for i, c in enumerate(chs):
            paras = c["text"].split("\n\n")
            for j, p in enumerate(paras):
                if pattern.search(p):
                    start = max(0, j - a.context)
                    end = min(len(paras), j + a.context + 1)
                    hits.append({"chapter": i + 1, "title": c["title"], "context": "\n\n".join(paras[start:end])})
        if a.json:
            print(json.dumps(hits, indent=2))
        else:
            for h in hits:
                print(f"\n=== Chapter {h['chapter']}: {h['title']} ===\n{h['context']}\n")
        return

    # full
    if a.json:
        print(json.dumps({"metadata": meta, "chapters": chs}, indent=2))
    else:
        if meta.get("title"):
            print(f"# {meta['title']}\n")
        if meta.get("creator"):
            print(f"*by {meta['creator']}*\n")
        for c in chs:
            print(f"## {c['title']}\n\n{c['text']}\n")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr); sys.exit(2)
