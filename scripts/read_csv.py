#!/usr/bin/env python3
"""Read a CSV/TSV with auto-detected delimiter and encoding. Prints summary + sample.

Usage:
    read_csv.py data.csv                       # summary + first 20 rows
    read_csv.py data.csv --rows 100            # first 100 rows
    read_csv.py data.csv --all                 # full table (markdown)
    read_csv.py data.csv --json                # JSON (records)
    read_csv.py data.csv --info                # schema + stats only
    read_csv.py data.csv --column "Revenue"    # one column's values
"""
import argparse
import csv
import json
import sys


def detect_encoding(path):
    import chardet
    with open(path, "rb") as f:
        raw = f.read(65536)
    return chardet.detect(raw)["encoding"] or "utf-8"


def detect_delimiter(path, encoding):
    with open(path, encoding=encoding, errors="replace") as f:
        sample = f.read(8192)
    try:
        return csv.Sniffer().sniff(sample).delimiter
    except csv.Error:
        return ","


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv")
    ap.add_argument("--rows", type=int, default=20, help="row limit for preview (default 20)")
    ap.add_argument("--all", action="store_true", help="print all rows")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--info", action="store_true")
    ap.add_argument("--column", help="print only this column")
    a = ap.parse_args()

    import pandas as pd
    enc = detect_encoding(a.csv)
    delim = detect_delimiter(a.csv, enc)
    df = pd.read_csv(a.csv, encoding=enc, sep=delim, on_bad_lines="skip", low_memory=False)

    if a.info:
        info = {
            "rows": len(df),
            "columns": list(df.columns),
            "encoding": enc,
            "delimiter": delim,
            "dtypes": {c: str(df[c].dtype) for c in df.columns},
            "null_counts": {c: int(df[c].isna().sum()) for c in df.columns},
        }
        if a.json:
            print(json.dumps(info, indent=2))
        else:
            print(f"Rows: {info['rows']}, Encoding: {enc}, Delimiter: {repr(delim)}")
            print(f"Columns ({len(info['columns'])}):")
            for c in info["columns"]:
                nulls = info["null_counts"][c]
                print(f"  - {c}  ({info['dtypes'][c]}, {nulls} null)")
        return

    if a.column:
        if a.column not in df.columns:
            print(f"ERROR: column '{a.column}' not found. Available: {list(df.columns)}", file=sys.stderr)
            sys.exit(2)
        if a.json:
            print(json.dumps(df[a.column].dropna().tolist(), default=str))
        else:
            for v in df[a.column].dropna():
                print(v)
        return

    if not a.all:
        df = df.head(a.rows)

    if a.json:
        print(df.fillna("").to_json(orient="records", indent=2))
    else:
        print(df.fillna("").to_markdown(index=False) if hasattr(df, "to_markdown") else df.to_string(index=False))


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr); sys.exit(2)
