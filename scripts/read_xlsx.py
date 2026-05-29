#!/usr/bin/env python3
"""Read an Excel file. Default: print every sheet as markdown table.

Usage:
    read_xlsx.py data.xlsx                       # all sheets, markdown
    read_xlsx.py data.xlsx --sheet "Revenue"     # one sheet
    read_xlsx.py data.xlsx --csv                 # CSV output (default: stdout)
    read_xlsx.py data.xlsx --json                # JSON output
    read_xlsx.py data.xlsx --info                # sheet names + dimensions only
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("xlsx")
    ap.add_argument("--sheet", help="single sheet name (default: all)")
    ap.add_argument("--csv", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--info", action="store_true")
    ap.add_argument("--max-rows", type=int, default=None)
    a = ap.parse_args()

    import pandas as pd
    xls = pd.ExcelFile(a.xlsx)
    sheets = [a.sheet] if a.sheet else xls.sheet_names

    if a.info:
        info = []
        for s in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=s, nrows=0)
            full = pd.read_excel(xls, sheet_name=s)
            info.append({"sheet": s, "rows": len(full), "columns": list(df.columns)})
        if a.json:
            print(json.dumps(info, indent=2, default=str))
        else:
            for i in info:
                print(f"Sheet: {i['sheet']} ({i['rows']} rows)")
                print(f"  Columns: {', '.join(map(str, i['columns']))}")
        return

    result = {}
    for s in sheets:
        df = pd.read_excel(xls, sheet_name=s, nrows=a.max_rows)
        result[s] = df

    if a.json:
        out = {s: df.fillna("").to_dict(orient="records") for s, df in result.items()}
        print(json.dumps(out, indent=2, default=str))
    elif a.csv:
        for s, df in result.items():
            print(f"# Sheet: {s}")
            print(df.to_csv(index=False))
    else:
        for s, df in result.items():
            print(f"\n## Sheet: {s}\n")
            print(df.fillna("").to_markdown(index=False) if hasattr(df, "to_markdown") else df.to_string(index=False))


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr); sys.exit(2)
