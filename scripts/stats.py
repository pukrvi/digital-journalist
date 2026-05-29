#!/usr/bin/env python3
"""Descriptive statistics: mean, median, std, percentiles, outliers, distribution shape.

Usage:
    stats.py --series 12,15,19,22,28,31,45,67,89
    stats.py --series-file data.csv --column revenue
    stats.py --series-file data.csv                    # all numeric columns
    stats.py --series 1,2,3,99 --outliers              # flag outliers (IQR rule)
    stats.py --series 1,2,3,4 --json
"""
import argparse
import json
import math
import statistics as stats
import sys


def describe(values, name="series"):
    import numpy as np
    arr = np.array(values, dtype=float)
    q1, med, q3 = np.percentile(arr, [25, 50, 75])
    iqr = q3 - q1
    out = {
        "name": name,
        "count": len(arr),
        "min": float(arr.min()),
        "max": float(arr.max()),
        "range": float(arr.max() - arr.min()),
        "mean": float(arr.mean()),
        "median": float(med),
        "stdev": float(arr.std(ddof=1)) if len(arr) > 1 else 0.0,
        "variance": float(arr.var(ddof=1)) if len(arr) > 1 else 0.0,
        "q1": float(q1),
        "q3": float(q3),
        "iqr": float(iqr),
        "p10": float(np.percentile(arr, 10)),
        "p90": float(np.percentile(arr, 90)),
        "skewness": float(((arr - arr.mean()) ** 3).mean() / arr.std() ** 3) if arr.std() else 0,
        "kurtosis": float(((arr - arr.mean()) ** 4).mean() / arr.var() ** 2 - 3) if arr.var() else 0,
        "sum": float(arr.sum()),
    }
    return out


def outliers_iqr(values):
    import numpy as np
    arr = np.array(values, dtype=float)
    q1, q3 = np.percentile(arr, [25, 75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return [v for v in values if v < lo or v > hi], lo, hi


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--series", help="comma-separated values")
    ap.add_argument("--series-file", help="CSV")
    ap.add_argument("--column", help="single column from CSV")
    ap.add_argument("--outliers", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.series:
        series = {"series": [float(x) for x in a.series.split(",")]}
    elif a.series_file:
        import pandas as pd
        df = pd.read_csv(a.series_file)
        if a.column:
            series = {a.column: df[a.column].dropna().tolist()}
        else:
            series = {c: df[c].dropna().tolist() for c in df.select_dtypes("number").columns}
    else:
        ap.error("Need --series or --series-file")

    results = []
    for name, values in series.items():
        if not values:
            continue
        d = describe(values, name)
        if a.outliers:
            outs, lo, hi = outliers_iqr(values)
            d["outliers"] = outs
            d["outlier_bounds"] = [lo, hi]
        results.append(d)

    if a.json:
        print(json.dumps(results if len(results) > 1 else results[0], indent=2))
    else:
        for d in results:
            print(f"\n=== {d['name']} ===")
            for k, v in d.items():
                if k == "name": continue
                if isinstance(v, float):
                    print(f"  {k:<12} {v:>12,.4f}")
                else:
                    print(f"  {k:<12} {v}")


if __name__ == "__main__":
    main()
