"""Does each candle pattern or indicator signal actually predict anything?

For every signal: how often it appeared on liquid stocks, the average return
over the next 5/10/20 trading days beyond the market index, how often it went
the expected way, and whether the result holds in both halves of the history.
"""
import numpy as np
import pandas as pd

from .analysis import DIRECTION, HORIZONS


def summarize(events: pd.DataFrame) -> pd.DataFrame:
    ev = events.dropna(subset=[f"ex{n}" for n in HORIZONS])
    if ev.empty:
        return pd.DataFrame()
    mid = ev["date"].min() + (ev["date"].max() - ev["date"].min()) / 2
    base = ev[ev["event"] == "_all_days"]
    base10 = base["ex10"].mean()
    rows = []
    for name, g in ev[ev["event"] != "_all_days"].groupby("event"):
        d = DIRECTION[name]
        x = g["ex10"] - base10            # relative to an ordinary day
        n = len(g)
        # Signals cluster on the same days, so count each date once for the error estimate.
        daily = x.groupby(g["date"]).mean()
        t = daily.mean() / (daily.std(ddof=1) / np.sqrt(len(daily))) if len(daily) > 2 else np.nan
        first, second = x[g["date"] < mid].mean(), x[g["date"] >= mid].mean()
        rows.append({
            "signal": name, "expects": "up" if d > 0 else "down", "count": n,
            "excess_5d_%": 100 * (g["ex5"].mean() - base["ex5"].mean()),
            "excess_10d_%": 100 * x.mean(),
            "excess_20d_%": 100 * (g["ex20"].mean() - base["ex20"].mean()),
            "right_way_10d_%": 100 * ((g["ex10"] * d) > 0).mean(),
            "t_stat": t,
            "same_both_halves": bool(np.sign(first) == np.sign(second) and not np.isnan(first + second)),
        })
    df = pd.DataFrame(rows)
    df["verdict"] = df.apply(verdict, axis=1)
    df["edge"] = df.apply(lambda r: r["excess_10d_%"] if r["verdict"] != "no reliable edge" else 0.0, axis=1)
    return df.sort_values(["expects", "excess_10d_%"], ascending=[False, False]).reset_index(drop=True)


def verdict(r) -> str:
    d = 1 if r["expects"] == "up" else -1
    if r["count"] < 30 or np.isnan(r["t_stat"]) or abs(r["t_stat"]) < 2 or not r["same_both_halves"]:
        return "no reliable edge"
    if np.sign(r["excess_10d_%"]) == d:
        return "works as expected"
    return "works in reverse"


def to_markdown(stats: pd.DataFrame, market: str, events: pd.DataFrame) -> str:
    label = {"ph": "Philippine", "us": "US"}[market]
    ev = events[events["event"] != "_all_days"]
    lines = [
        f"# Which signals work: {label} stocks", "",
        f"Tested on {ev['symbol'].nunique():,} stocks, {ev['date'].min():%b %Y} to {ev['date'].max():%b %Y}, "
        "liquid stocks only. **Excess** is the stock's return minus the market index's "
        "over the same days, compared with an ordinary day. **Right way** is how often the "
        "stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; "
        "a coin flip is 50%.",
        "",
        "A signal is called *working* only if it appeared at least 30 times, its result is "
        "statistically clear (|t| ≥ 2, counting each day once), and it points the same way "
        "in both halves of the history.", "",
        "| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |",
        "|---|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in stats.itertuples():
        lines.append(
            f"| {r.signal.replace('_', ' ')} | {r.expects} | {r.count:,} | {r[4]:+.2f}% | {r[5]:+.2f}% | "
            f"{r[6]:+.2f}% | {r[7]:.0f}% | {r.t_stat:+.1f} | {r.verdict} |")
    lines += ["", "Past results do not guarantee future ones. Survivorship: stocks that were "
              "delisted are missing from the data, which flatters long-run returns a little."]
    return "\n".join(lines) + "\n"
