#!/usr/bin/env python3
"""Compound Annual Growth Rate (CAGR) and related growth math.

Usage:
    cagr.py <start> <end> <years>                   # standard CAGR
    cagr.py 1000 1500 5                             # 5-year CAGR of 1000 -> 1500
    cagr.py --series 100,120,140,180,220            # CAGR from first to last in series
    cagr.py --series-file values.csv --column Revenue
    cagr.py 1000 ? 5 --rate 0.08                    # extrapolate end value
    cagr.py 1000 1500 ? --rate 0.085                # solve for years
"""
import argparse
import json
import math
import sys


def cagr(start, end, years):
    return (end / start) ** (1.0 / years) - 1.0


def end_value(start, rate, years):
    return start * (1.0 + rate) ** years


def years_for(start, end, rate):
    return math.log(end / start) / math.log(1 + rate)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("start", nargs="?")
    ap.add_argument("end", nargs="?")
    ap.add_argument("years", nargs="?")
    ap.add_argument("--rate", type=float, help="annual growth rate as decimal (e.g. 0.08 = 8%)")
    ap.add_argument("--series", help="comma-separated values")
    ap.add_argument("--series-file", help="CSV file with a numeric column")
    ap.add_argument("--column", help="column name when using --series-file")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.series_file:
        import pandas as pd
        df = pd.read_csv(a.series_file)
        col = a.column or df.select_dtypes("number").columns[0]
        values = df[col].dropna().tolist()
    elif a.series:
        values = [float(x) for x in a.series.split(",")]
    else:
        values = None

    if values:
        if len(values) < 2:
            print("ERROR: series needs ≥2 values", file=sys.stderr); sys.exit(2)
        s, e = values[0], values[-1]
        y = len(values) - 1
        r = cagr(s, e, y)
        out = {"start": s, "end": e, "periods": y, "cagr": r, "cagr_pct": r * 100, "values": values}
    else:
        if a.start in (None, "?") + (a.end,) and a.rate is None:
            ap.error("Need <start> <end> <years>, or --series, or use --rate to solve a missing value.")

        s = None if a.start == "?" else (float(a.start) if a.start is not None else None)
        e = None if a.end == "?" else (float(a.end) if a.end is not None else None)
        y = None if a.years == "?" else (float(a.years) if a.years is not None else None)

        if s is not None and e is not None and y is not None:
            r = cagr(s, e, y)
            out = {"start": s, "end": e, "years": y, "cagr": r, "cagr_pct": r * 100}
        elif s is not None and y is not None and a.rate is not None:
            ev = end_value(s, a.rate, y)
            out = {"start": s, "rate": a.rate, "years": y, "end_value": ev}
        elif s is not None and e is not None and a.rate is not None:
            yy = years_for(s, e, a.rate)
            out = {"start": s, "end": e, "rate": a.rate, "years_needed": yy}
        else:
            ap.error("Provide at least 3 of {start, end, years, rate}.")

    if a.json:
        print(json.dumps(out, indent=2))
    else:
        for k, v in out.items():
            if isinstance(v, float):
                if k.endswith("_pct"):
                    print(f"{k}: {v:.2f}%")
                else:
                    print(f"{k}: {v:,.4f}")
            else:
                print(f"{k}: {v}")


if __name__ == "__main__":
    main()
