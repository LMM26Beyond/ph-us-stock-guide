"""Score every stock 0-100 from trend, momentum and recent signals.

  trend     35%  price vs 50/200-day averages, 50 vs 200, slope of the 200-day
  momentum  35%  12-month return (skipping the last month) and 6-month return
                 vs the index, ranked against the other liquid stocks that day
  MACD      10%  MACD histogram above or below zero
  RSI       10%  very overbought (>80) counts against; oversold in an uptrend for
  candles   10%  patterns and signals from the last 3 days, but only the ones the
                 history study found to work (see reports/signals_<market>.md)

50 is neutral. The same formula without the candle part is tested on past
month-ends in validate().
"""
import numpy as np
import pandas as pd

from .analysis import DIRECTION

WEIGHTS = {"trend": 0.35, "momentum": 0.35, "macd": 0.10, "rsi": 0.10, "candles": 0.10}


def components(s: pd.DataFrame, bench_ret6m: pd.Series) -> pd.DataFrame:
    """Score parts in -1..+1. Ranks compare stocks on the same date."""
    sg = lambda x: np.sign(x).fillna(0)
    out = pd.DataFrame(index=s.index)
    out["trend"] = (sg(s["close"] - s["sma200"]) + sg(s["sma50"] - s["sma200"])
                    + sg(s["sma200_slope"]) + sg(s["close"] - s["sma50"])) / 4
    s = s.assign(rel6=s["ret6m"] - s["date"].map(bench_ret6m).fillna(0))
    liquid = s[s["liquid"]]

    def rank(col):
        return (2 * liquid.groupby("date")[col].rank(pct=True) - 1).reindex(s.index).fillna(0)

    out["momentum"] = (rank("mom12_1") + rank("rel6")) / 2
    out["macd"] = sg(s["macd_hist"])
    rsi = s["rsi14"]
    out["rsi"] = np.where(rsi > 80, -1.0, np.where((rsi < 30) & (out["trend"] > 0), 1.0, 0.0))
    return out


def candle_points(pats: str, stats: pd.DataFrame | None) -> float:
    if not pats or stats is None or stats.empty:
        return 0.0
    edge = stats.set_index("signal")["verdict"]
    pts = 0.0
    for name in pats.split(", "):
        v = edge.get(name)
        if v == "works as expected":
            pts += DIRECTION[name]
        elif v == "works in reverse":
            pts -= DIRECTION[name]
    return float(np.clip(pts, -1, 1))


def total(comp: pd.DataFrame, with_candles: bool = True) -> pd.Series:
    w = dict(WEIGHTS)
    if not with_candles:
        w.pop("candles")
    norm = sum(w.values())
    return 50 + 50 * sum(comp[k] * v for k, v in w.items()) / norm


def latest(snaps: pd.DataFrame, bench: pd.DataFrame, stats: pd.DataFrame | None) -> pd.DataFrame:
    """Today's score for every stock that traded in the last week."""
    s = snaps[snaps["latest"]].copy()
    newest = s["date"].max()
    s = s[s["date"] >= newest - pd.Timedelta(days=7)].reset_index(drop=True)
    last_traded = s["date"]
    s["date"] = newest  # rank all current stocks together
    comp = components(s, pd.Series({newest: bench["ret6m"].iloc[-1]}))
    comp["candles"] = s["patterns"].map(lambda p: candle_points(p, stats))
    s = s.join(comp)
    s["score"] = total(comp).round(0)
    s["date"] = last_traded
    return s


def validate(snaps: pd.DataFrame, bench: pd.DataFrame) -> pd.DataFrame:
    """Past month-ends: split liquid stocks into five score groups and measure the
    next month's return beyond the index for each group."""
    s = snaps[~snaps["latest"] | snaps["fwd21_ex"].notna()]
    s = s[s["liquid"] & s["fwd21_ex"].notna() & s["sma200"].notna() & s["mom12_1"].notna()].reset_index(drop=True)
    if s.empty:
        return pd.DataFrame()
    # Month-end rows only (one per stock per month).
    s = s[s.groupby([s["symbol"], s["date"].dt.to_period("M")])["date"].transform("max") == s["date"]]
    s = s.reset_index(drop=True)
    comp = components(s, bench["ret6m"])
    s["score"] = total(comp, with_candles=False)
    s["month"] = s["date"].dt.to_period("M")
    counts = s.groupby("month")["symbol"].transform("count")
    s = s[counts >= 20]
    s["group"] = s.groupby("month")["score"].transform(lambda x: pd.qcut(x.rank(method="first"), 5, labels=False)) + 1
    by = s.groupby(["month", "group"])["fwd21_ex"].mean().unstack()
    return by
