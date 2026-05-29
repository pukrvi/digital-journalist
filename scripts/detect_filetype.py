#!/usr/bin/env python3
"""Detect file type by magic bytes (not extension). Outputs MIME + suggested reader script.

Usage:
    detect_filetype.py <file>
    detect_filetype.py <file> --json
"""
import argparse
import json
import os
import sys

EXT_TO_READER = {
    ".pdf":  "read_pdf.py",
    ".docx": "read_docx.py",
    ".doc":  "read_docx.py",
    ".xlsx": "read_xlsx.py",
    ".xls":  "read_xlsx.py",
    ".csv":  "read_csv.py",
    ".tsv":  "read_csv.py",
    ".html": "read_html.py",
    ".htm":  "read_html.py",
    ".pptx": "read_pptx.py",
    ".epub": "read_epub.py",
    ".txt":  "cat",
    ".md":   "cat",
    ".json": "jq .",
    ".mp3":  "transcribe.py",
    ".wav":  "transcribe.py",
    ".m4a":  "transcribe.py",
    ".mp4":  "transcribe.py (or extract_audio.py first)",
    ".mov":  "transcribe.py (or extract_audio.py first)",
    ".mkv":  "transcribe.py (or extract_audio.py first)",
}

MIME_HINTS = {
    "application/pdf": "read_pdf.py",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": "read_docx.py",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "read_xlsx.py",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": "read_pptx.py",
    "application/epub+zip": "read_epub.py",
    "text/html": "read_html.py",
    "text/csv": "read_csv.py",
    "application/json": "jq .",
}


def detect(path):
    try:
        import magic
        mime = magic.from_file(path, mime=True)
    except Exception:
        mime = None
    ext = os.path.splitext(path)[1].lower()
    reader = MIME_HINTS.get(mime) or EXT_TO_READER.get(ext) or "unknown"
    return {"path": path, "mime": mime, "extension": ext, "suggested_reader": reader, "size_bytes": os.path.getsize(path)}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file")
    ap.add_argument("--json", action="store_true", help="JSON output")
    a = ap.parse_args()
    if not os.path.isfile(a.file):
        print(f"ERROR: not a file: {a.file}", file=sys.stderr); sys.exit(2)
    info = detect(a.file)
    if a.json:
        print(json.dumps(info, indent=2))
    else:
        print(f"File:       {info['path']}")
        print(f"Size:       {info['size_bytes']:,} bytes")
        print(f"MIME:       {info['mime'] or '(unknown)'}")
        print(f"Extension:  {info['extension']}")
        print(f"Reader:     {info['suggested_reader']}")


if __name__ == "__main__":
    main()
