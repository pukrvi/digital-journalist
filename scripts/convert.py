#!/usr/bin/env python3
"""Convert between common formats: md ↔ html, html ↔ md, json ↔ csv, csv ↔ json, md ↔ pdf.

Usage:
    convert.py article.md article.html              # md → html (auto-detected from extension)
    convert.py page.html page.md                    # html → md
    convert.py data.csv data.json                   # csv → json
    convert.py data.json data.csv                   # json → csv (array of objects)
    convert.py article.md article.pdf               # md → pdf (requires pandoc + wkhtmltopdf, falls back to ReportLab)
"""
import argparse
import csv
import json
import os
import shutil
import subprocess
import sys


def md_to_html(src, dst):
    import markdown
    with open(src, encoding="utf-8") as f:
        html = markdown.markdown(f.read(), extensions=["fenced_code", "tables", "toc"])
    body = f"""<!doctype html><html><head><meta charset='utf-8'><title>{os.path.basename(src)}</title>
<style>body{{max-width:760px;margin:2em auto;padding:0 1em;font-family:-apple-system,Helvetica,Arial,sans-serif;line-height:1.6;color:#222}}
pre{{background:#f5f5f5;padding:1em;overflow:auto;border-radius:4px}}
code{{background:#f5f5f5;padding:.1em .3em;border-radius:3px}}
blockquote{{border-left:3px solid #ccc;padding-left:1em;color:#555}}
table{{border-collapse:collapse}}th,td{{border:1px solid #ddd;padding:.4em .8em}}</style>
</head><body>{html}</body></html>"""
    with open(dst, "w", encoding="utf-8") as f:
        f.write(body)


def html_to_md(src, dst):
    from markdownify import markdownify
    with open(src, encoding="utf-8") as f:
        md = markdownify(f.read(), heading_style="ATX")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(md)


def csv_to_json(src, dst):
    import pandas as pd
    df = pd.read_csv(src)
    df.fillna("").to_json(dst, orient="records", indent=2)


def json_to_csv(src, dst):
    with open(src, encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        print("ERROR: JSON must be an array of objects for CSV conversion", file=sys.stderr); sys.exit(2)
    if not data:
        open(dst, "w").close(); return
    keys = list(data[0].keys())
    with open(dst, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for row in data:
            w.writerow({k: row.get(k, "") for k in keys})


def md_to_pdf(src, dst):
    if shutil.which("pandoc"):
        subprocess.check_call(["pandoc", src, "-o", dst, "--pdf-engine=wkhtmltopdf" if shutil.which("wkhtmltopdf") else "--pdf-engine=weasyprint"] if shutil.which("wkhtmltopdf") or shutil.which("weasyprint") else ["pandoc", src, "-o", dst])
        return
    # Fallback: simple text → pdf via reportlab
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    except ImportError:
        print("ERROR: install pandoc, or 'pip install reportlab markdown'", file=sys.stderr); sys.exit(2)
    import markdown as md_mod
    with open(src, encoding="utf-8") as f:
        text = f.read()
    html = md_mod.markdown(text)
    doc = SimpleDocTemplate(dst, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    for line in html.split("\n"):
        if line.strip():
            story.append(Paragraph(line, styles["BodyText"]))
            story.append(Spacer(1, 6))
    doc.build(story)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("source")
    ap.add_argument("dest")
    a = ap.parse_args()

    src_ext = os.path.splitext(a.source)[1].lower()
    dst_ext = os.path.splitext(a.dest)[1].lower()
    pair = (src_ext, dst_ext)

    handlers = {
        (".md", ".html"): md_to_html, (".md", ".htm"): md_to_html,
        (".html", ".md"): html_to_md, (".htm", ".md"): html_to_md,
        (".csv", ".json"): csv_to_json,
        (".json", ".csv"): json_to_csv,
        (".md", ".pdf"): md_to_pdf,
    }
    handler = handlers.get(pair)
    if not handler:
        print(f"ERROR: no handler for {src_ext} → {dst_ext}", file=sys.stderr); sys.exit(2)
    handler(a.source, a.dest)
    print(f"Wrote {a.dest}")


if __name__ == "__main__":
    main()
