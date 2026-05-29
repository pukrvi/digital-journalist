#!/usr/bin/env python3
"""Financial calculators: % change, YoY, YTD, NPV, IRR, ROI, Rule of 72.

Usage:
    financial_calc.py pct-change <old> <new>
    financial_calc.py yoy --series 100,110,115,120        # YoY for each step
    financial_calc.py ytd --series 5,8,11,9,12             # cumulative YTD
    financial_calc.py npv --rate 0.10 --cashflows=-1000,200,300,400,500
    financial_calc.py irr --cashflows=-1000,200,300,400,500

    Note: when a value starts with '-', use '--flag=value' (with the '=') so argparse
    doesn't mistake it for a new flag.
    financial_calc.py roi --gain 5000 --cost 3000
    financial_calc.py rule72 --rate 0.07                   # years to double
"""
import argparse
import json
import math
import sys


def pct_change(old, new):
    return (new - old) / old


def yoy(values):
    return [None if i == 0 else pct_change(values[i-1], values[i]) for i in range(len(values))]


def ytd(values):
    out, total = [], 0
    for v in values:
        total += v
        out.append(total)
    return out


def npv(rate, cashflows):
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cashflows))


def irr(cashflows, guess=0.1, tol=1e-9, max_iter=1000):
    """Newton's method on NPV(r) = 0."""
    r = guess
    for _ in range(max_iter):
        f = sum(cf / (1 + r) ** t for t, cf in enumerate(cashflows))
        fp = sum(-t * cf / (1 + r) ** (t + 1) for t, cf in enumerate(cashflows))
        if abs(fp) < 1e-12:
            break
        new_r = r - f / fp
        if abs(new_r - r) < tol:
            return new_r
        r = new_r
    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("pct-change"); p.add_argument("old", type=float); p.add_argument("new", type=float)
    p = sub.add_parser("yoy"); p.add_argument("--series", required=True)
    p = sub.add_parser("ytd"); p.add_argument("--series", required=True)
    p = sub.add_parser("npv"); p.add_argument("--rate", type=float, required=True); p.add_argument("--cashflows", required=True)
    p = sub.add_parser("irr"); p.add_argument("--cashflows", required=True); p.add_argument("--guess", type=float, default=0.1)
    p = sub.add_parser("roi"); p.add_argument("--gain", type=float, required=True); p.add_argument("--cost", type=float, required=True)
    p = sub.add_parser("rule72"); p.add_argument("--rate", type=float, required=True)

    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.cmd == "pct-change":
        r = pct_change(a.old, a.new)
        out = {"old": a.old, "new": a.new, "change_pct": r * 100, "change": a.new - a.old}
    elif a.cmd == "yoy":
        vals = [float(x) for x in a.series.split(",")]
        out = {"series": vals, "yoy_pct": [None if r is None else r * 100 for r in yoy(vals)]}
    elif a.cmd == "ytd":
        vals = [float(x) for x in a.series.split(",")]
        out = {"series": vals, "ytd": ytd(vals)}
    elif a.cmd == "npv":
        cfs = [float(x) for x in a.cashflows.split(",")]
        out = {"rate": a.rate, "cashflows": cfs, "npv": npv(a.rate, cfs)}
    elif a.cmd == "irr":
        cfs = [float(x) for x in a.cashflows.split(",")]
        r = irr(cfs, guess=a.guess)
        out = {"cashflows": cfs, "irr": r, "irr_pct": r * 100}
    elif a.cmd == "roi":
        roi_v = (a.gain - a.cost) / a.cost
        out = {"gain": a.gain, "cost": a.cost, "roi": roi_v, "roi_pct": roi_v * 100}
    elif a.cmd == "rule72":
        out = {"rate": a.rate, "years_to_double": 72.0 / (a.rate * 100), "exact_years_to_double": math.log(2) / math.log(1 + a.rate)}

    if a.json:
        print(json.dumps(out, indent=2))
    else:
        for k, v in out.items():
            if isinstance(v, float):
                fmt = ",.2f" if k.endswith("_pct") else ",.4f"
                print(f"{k}: {v:{fmt}}{'%' if k.endswith('_pct') else ''}")
            elif isinstance(v, list):
                print(f"{k}: {v}")
            else:
                print(f"{k}: {v}")


if __name__ == "__main__":
    main()
