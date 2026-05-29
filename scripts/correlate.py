#!/usr/bin/env python3
"""Compute correlation between two series (Pearson + Spearman + lag correlations).

Usage:
    correlate.py --a 1,2,3,4,5 --b 2,4,6,8,10                            # perfect linear
    correlate.py --file data.csv --columns revenue,marketing_spend
    correlate.py --file data.csv --columns revenue,headcount --lags 3    # with lag analysis
    correlate.py --file data.csv                                          # all pairs (correlation matrix)
"""
import argparse
import json
import sys


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--a", help="series a (comma-separated)")
    ap.add_argument("--b", help="series b (comma-separated)")
    ap.add_argument("--file", help="CSV file")
    ap.add_argument("--columns", help="two columns from CSV: 'col1,col2'")
    ap.add_argument("--lags", type=int, default=0, help="examine lag correlations up to this many periods")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    import numpy as np
    from scipy.stats import pearsonr, spearmanr

    if a.file and not a.columns:
        import pandas as pd
        df = pd.read_csv(a.file).select_dtypes("number")
        if a.json:
            print(df.corr().to_json(indent=2))
        else:
            print("Correlation matrix (Pearson):\n")
            print(df.corr().round(3).to_markdown() if hasattr(df.corr(), "to_markdown") else df.corr().round(3).to_string())
        return

    if a.file:
        import pandas as pd
        c1, c2 = a.columns.split(",")
        df = pd.read_csv(a.file)[[c1.strip(), c2.strip()]].dropna()
        s1, s2 = df.iloc[:, 0].tolist(), df.iloc[:, 1].tolist()
        names = (c1.strip(), c2.strip())
    elif a.a and a.b:
        s1 = [float(x) for x in a.a.split(",")]
        s2 = [float(x) for x in a.b.split(",")]
        names = ("a", "b")
    else:
        ap.error("Need either (--a and --b) or --file with --columns")

    if len(s1) != len(s2):
        n = min(len(s1), len(s2)); s1, s2 = s1[:n], s2[:n]

    pr, pp = pearsonr(s1, s2)
    sr, sp = spearmanr(s1, s2)
    out = {
        "x": names[0], "y": names[1], "n": len(s1),
        "pearson_r": float(pr), "pearson_p": float(pp),
        "spearman_r": float(sr), "spearman_p": float(sp),
    }

    if a.lags:
        lag_results = []
        for k in range(-a.lags, a.lags + 1):
            if k == 0: continue
            if k > 0:
                a_, b_ = s1[:-k], s2[k:]
            else:
                a_, b_ = s1[-k:], s2[:k]
            if len(a_) > 2:
                r, _ = pearsonr(a_, b_)
                lag_results.append({"lag": k, "pearson_r": float(r), "n": len(a_)})
        out["lag_correlations"] = lag_results

    if a.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"N = {out['n']}")
        print(f"Pearson r  = {out['pearson_r']:+.4f}  (p = {out['pearson_p']:.4f})")
        print(f"Spearman r = {out['spearman_r']:+.4f}  (p = {out['spearman_p']:.4f})")
        strength = abs(out["pearson_r"])
        label = ("very strong" if strength > 0.8 else "strong" if strength > 0.6 else
                 "moderate" if strength > 0.4 else "weak" if strength > 0.2 else "negligible")
        print(f"Interpretation: {label} {'positive' if out['pearson_r'] >= 0 else 'negative'} relationship")
        if a.lags:
            print("\nLag correlations:")
            for r in out.get("lag_correlations", []):
                marker = " ←" if abs(r["pearson_r"]) > abs(out["pearson_r"]) else ""
                print(f"  lag {r['lag']:+d}: r = {r['pearson_r']:+.4f}  (n={r['n']}){marker}")


if __name__ == "__main__":
    main()
