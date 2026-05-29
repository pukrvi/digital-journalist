#!/usr/bin/env python3
"""Extrapolate a series: linear, exponential, logistic, polynomial. Output future points.

Usage:
    extrapolate.py --series 10,12,15,19,24 --periods 5         # linear (default)
    extrapolate.py --series 100,140,196,274 --model exponential --periods 5
    extrapolate.py --series 5,10,30,80,180,250 --model logistic --periods 10 --carrying 300
    extrapolate.py --series-file data.csv --column revenue --periods 3 --model polynomial --degree 2
    extrapolate.py --series 1,2,3,4 --json
"""
import argparse
import json
import math
import sys


def linear(values, periods):
    import numpy as np
    n = len(values)
    x = np.arange(n)
    y = np.array(values, dtype=float)
    slope, intercept = np.polyfit(x, y, 1)
    future_x = np.arange(n, n + periods)
    return [intercept + slope * xi for xi in future_x], {"slope": slope, "intercept": intercept}


def exponential(values, periods):
    """Fit y = a * exp(b*x). Requires positive values."""
    import numpy as np
    if any(v <= 0 for v in values):
        raise ValueError("exponential model requires all positive values")
    n = len(values)
    x = np.arange(n)
    logy = np.log(np.array(values, dtype=float))
    b, log_a = np.polyfit(x, logy, 1)
    a = math.exp(log_a)
    future = [a * math.exp(b * xi) for xi in range(n, n + periods)]
    return future, {"a": a, "b": b, "annual_growth_pct": (math.exp(b) - 1) * 100}


def logistic(values, periods, carrying):
    """Fit y = L / (1 + e^{-k(x-x0)}). Returns future values projected toward L."""
    import numpy as np
    from scipy.optimize import curve_fit
    L = carrying or 2.0 * max(values)
    n = len(values)
    x = np.arange(n, dtype=float)
    y = np.array(values, dtype=float)

    def f(x, k, x0):
        return L / (1.0 + np.exp(-k * (x - x0)))

    try:
        (k, x0), _ = curve_fit(f, x, y, p0=[0.5, n / 2.0], maxfev=10000)
    except Exception:
        k, x0 = 0.5, n / 2.0
    future = [float(f(xi, k, x0)) for xi in range(n, n + periods)]
    return future, {"L": L, "k": k, "x0": x0}


def polynomial(values, periods, degree=2):
    import numpy as np
    n = len(values)
    x = np.arange(n)
    coeffs = np.polyfit(x, np.array(values, dtype=float), degree)
    poly = np.poly1d(coeffs)
    future = [float(poly(xi)) for xi in range(n, n + periods)]
    return future, {"coefficients": coeffs.tolist(), "degree": degree}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--series", help="comma-separated values")
    ap.add_argument("--series-file", help="CSV file")
    ap.add_argument("--column", help="column when using --series-file")
    ap.add_argument("--model", choices=["linear", "exponential", "logistic", "polynomial"], default="linear")
    ap.add_argument("--degree", type=int, default=2, help="for polynomial")
    ap.add_argument("--carrying", type=float, help="L for logistic (default: 2 * max)")
    ap.add_argument("--periods", type=int, default=5)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.series:
        values = [float(x) for x in a.series.split(",")]
    elif a.series_file:
        import pandas as pd
        df = pd.read_csv(a.series_file)
        col = a.column or df.select_dtypes("number").columns[0]
        values = df[col].dropna().tolist()
    else:
        ap.error("Need --series or --series-file")

    if a.model == "linear":
        future, params = linear(values, a.periods)
    elif a.model == "exponential":
        future, params = exponential(values, a.periods)
    elif a.model == "logistic":
        future, params = logistic(values, a.periods, a.carrying)
    elif a.model == "polynomial":
        future, params = polynomial(values, a.periods, a.degree)

    out = {"model": a.model, "input_series": values, "future_periods": future, "parameters": params}

    if a.json:
        print(json.dumps(out, indent=2, default=str))
    else:
        print(f"Model: {a.model}")
        print(f"Input ({len(values)} points): {values}")
        print(f"\nForecast ({a.periods} periods):")
        for i, v in enumerate(future, start=len(values) + 1):
            print(f"  t={i:3d}  {v:,.2f}")
        print(f"\nParameters: {params}")


if __name__ == "__main__":
    main()
