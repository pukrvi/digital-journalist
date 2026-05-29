#!/usr/bin/env python3
"""Extract embedded images from a PDF (charts, figures, photos).

Usage:
    extract_images_pdf.py report.pdf                   # to ./report-images/
    extract_images_pdf.py report.pdf -o out/           # to specific dir
    extract_images_pdf.py report.pdf --pages 1-10      # subset of pages
    extract_images_pdf.py report.pdf --render          # render full pages too (PNG)
"""
import argparse
import os
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pdf")
    ap.add_argument("-o", "--out", help="output directory (default: ./<basename>-images/)")
    ap.add_argument("--pages", help="e.g. 1-10")
    ap.add_argument("--render", action="store_true", help="also render each full page as PNG")
    a = ap.parse_args()

    import fitz  # pymupdf
    doc = fitz.open(a.pdf)
    n = len(doc)

    if a.pages and "-" in a.pages:
        start, end = a.pages.split("-", 1)
        idx = range(int(start) - 1 if start else 0, int(end) if end else n)
    elif a.pages:
        idx = [int(a.pages) - 1]
    else:
        idx = range(n)

    base = os.path.splitext(os.path.basename(a.pdf))[0]
    out = a.out or f"./{base}-images"
    os.makedirs(out, exist_ok=True)

    count = 0
    for pn in idx:
        page = doc[pn]
        for ii, info in enumerate(page.get_images(full=True)):
            xref = info[0]
            try:
                img = doc.extract_image(xref)
                ext = img["ext"]
                path = os.path.join(out, f"page{pn+1:03d}_img{ii+1:02d}.{ext}")
                with open(path, "wb") as f:
                    f.write(img["image"])
                count += 1
                print(f"saved: {path}")
            except Exception as e:
                print(f"  skip xref {xref}: {e}", file=sys.stderr)
        if a.render:
            pix = page.get_pixmap(dpi=144)
            rp = os.path.join(out, f"page{pn+1:03d}_render.png")
            pix.save(rp)
            print(f"rendered: {rp}")

    print(f"\nDone. {count} images extracted to {out}/")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr); sys.exit(2)
