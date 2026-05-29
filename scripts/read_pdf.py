#!/usr/bin/env python3
"""Extract text from a PDF, with optional page range, page-by-page output, or JSON.

Usage:
    read_pdf.py report.pdf                         # full text
    read_pdf.py report.pdf --pages 1-5             # first 5 pages
    read_pdf.py report.pdf --json                  # structured JSON (page-keyed)
    read_pdf.py report.pdf --tables                # also extract tables (markdown)
    read_pdf.py report.pdf --meta                  # metadata only
"""
import argparse
import json
import sys


def parse_pages(spec, total):
    if not spec:
        return list(range(total))
    if "-" in spec:
        a, b = spec.split("-", 1)
        a = int(a) - 1 if a else 0
        b = int(b) if b else total
        return list(range(max(0, a), min(total, b)))
    if "," in spec:
        return sorted({int(p) - 1 for p in spec.split(",") if p.strip()})
    return [int(spec) - 1]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pdf")
    ap.add_argument("--pages", help="e.g. 1-5 or 1,3,5 (1-indexed)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--tables", action="store_true", help="extract tables as markdown")
    ap.add_argument("--meta", action="store_true", help="print metadata only")
    a = ap.parse_args()

    import pdfplumber

    with pdfplumber.open(a.pdf) as pdf:
        meta = pdf.metadata or {}
        meta_out = {k: str(v) for k, v in meta.items()}
        meta_out["page_count"] = len(pdf.pages)

        if a.meta:
            if a.json:
                print(json.dumps(meta_out, indent=2))
            else:
                for k, v in meta_out.items():
                    print(f"{k}: {v}")
            return

        idx = parse_pages(a.pages, len(pdf.pages))
        pages_out = []
        for i in idx:
            page = pdf.pages[i]
            text = page.extract_text() or ""
            tables_md = []
            if a.tables:
                for tbl in page.extract_tables() or []:
                    if not tbl:
                        continue
                    head = tbl[0]
                    rows = tbl[1:]
                    md = "| " + " | ".join(c or "" for c in head) + " |\n"
                    md += "|" + "|".join("---" for _ in head) + "|\n"
                    for r in rows:
                        md += "| " + " | ".join((c or "").replace("\n", " ") for c in r) + " |\n"
                    tables_md.append(md)
            pages_out.append({"page": i + 1, "text": text, "tables": tables_md})

        if a.json:
            print(json.dumps({"metadata": meta_out, "pages": pages_out}, indent=2))
        else:
            for p in pages_out:
                print(f"\n========== PAGE {p['page']} ==========\n")
                print(p["text"])
                for t in p["tables"]:
                    print("\n--- TABLE ---")
                    print(t)


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr); sys.exit(2)
