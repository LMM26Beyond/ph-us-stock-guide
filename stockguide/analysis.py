"""One pass over every stock in a market.

For each stock it computes indicators and candlestick patterns, then keeps:
- events: every pattern or indicator signal, with what the stock did over the
  next 5, 10 and 20 trading days compared with the market index (excess return),
  plus its own 10-day return (r10, used by the candle outlook);
- snapshots: indicator values on each month-end and on the latest day, used to
  score stocks today and to test the score on past months.
"""
import numpy as np
import pandas as pd

from . import indicators, patterns, storage
from .config import BENCHMARK, MIN_DAILY_VALUE

HORIZONS = (5, 10, 20)

# Indicator signals studied next to the candle patterns: name -> direction.
SIGNAL_DIRECTION = {
    "golden_cross": 1, "death_cross": -1,
    "macd_cross_up": 1, "macd_cross_down": -1,
    "rsi_oversold_exit": 1, "rsi_overbought_exit": -1,
    "breakout_52w_high": 1, "breakdown_52w_low": -1,
    "volume_surge_up": 1, "volume_surge_down": -1,
}
DIRECTION = {**{k: v for k, v in patterns.DIRECTION.items() if v}, **SIGNAL_DIRECTION}

SNAPSHOT_COLS = ["close", "sma50", "sma200", "sma200_slope", "macd_hist", "rsi14",
                 "atr14", "value20", "ret1m", "ret3m", "ret6m", "ret12m", "mom12_1", "hi52", "lo52"]


def benchmark(market: str) -> pd.DataFrame:
    return indicators.add(storage.load(market, BENCHMARK[market], "indexes"))


def signals(f: pd.DataFrame) -> pd.DataFrame:
    """Indicator signals on a frame that already has indicator columns."""
    p = lambda s: s.shift()
    c = f["close"]
    s = pd.DataFrame(index=f.index)
    s["golden_cross"] = (f["sma50"] > f["sma200"]) & (p(f["sma50"]) <= p(f["sma200"]))
    s["death_cross"] = (f["sma50"] < f["sma200"]) & (p(f["sma50"]) >= p(f["sma200"]))
    s["macd_cross_up"] = (f["macd"] > f["macd_signal"]) & (p(f["macd"]) <= p(f["macd_signal"]))
    s["macd_cross_down"] = (f["macd"] < f["macd_signal"]) & (p(f["macd"]) >= p(f["macd_signal"]))
    s["rsi_oversold_exit"] = (f["rsi14"] > 30) & (p(f["rsi14"]) <= 30)
    s["rsi_overbought_exit"] = (f["rsi14"] < 70) & (p(f["rsi14"]) >= 70)
    s["breakout_52w_high"] = c > p(f["hi52"])
    s["breakdown_52w_low"] = c < p(f["lo52"])
    surge = f["volume"] > 2 * p(f["vol20"])
    s["volume_surge_up"] = surge & (c > p(c) * 1.02)
    s["volume_surge_down"] = surge & (c < p(c) * 0.98)
    return s.fillna(False).astype(bool)


def stock_frame(market: str, symbol: str) -> pd.DataFrame | None:
    df = storage.load(market, symbol)
    if len(df) < 60:
        return None
    f = indicators.add(df)
    return f.join(patterns.detect(df)).join(signals(f))


def run(market: str, symbols: list[str] | None = None, progress: bool = True):
    bench = benchmark(market)
    bfwd = {n: bench["close"].shift(-n) / bench["close"] - 1 for n in (*HORIZONS, 21)}
    min_value = MIN_DAILY_VALUE[market]
    symbols = symbols or storage.symbols(market)
    events, snaps = [], []
    for i, sym in enumerate(symbols, 1):
        if progress and i % 500 == 0:
            print(f"  {market}: analysed {i}/{len(symbols)}")
        f = stock_frame(market, sym)
        if f is None:
            continue
        c = f["close"]
        liquid = f["value20"] >= min_value
        if market == "us":
            liquid &= c >= 3
        ex = {}
        for n in HORIZONS:
            fwd = c.shift(-n) / c - 1
            # Clip absurd moves (bad ticks, reverse splits) so they cannot dominate averages.
            ex[n] = (fwd - bfwd[n].reindex(f.index)).clip(-0.5, 0.5)
        r10 = (c.shift(-10) / c - 1).clip(-0.5, 0.5)
        names = [k for k in DIRECTION]
        hits = f[names] & liquid.to_numpy()[:, None]
        rows, cols = np.nonzero(hits.to_numpy())
        if len(rows):
            e = pd.DataFrame({"symbol": sym, "date": f.index[rows], "event": np.array(names)[cols]})
            for n in HORIZONS:
                e[f"ex{n}"] = ex[n].to_numpy()[rows]
            e["r10"] = r10.to_numpy()[rows]
            events.append(e)
        # Baseline: every liquid day, for comparison.
        base = pd.DataFrame({"symbol": sym, "date": f.index[liquid.to_numpy()], "event": "_all_days"})
        for n in HORIZONS:
            base[f"ex{n}"] = ex[n][liquid].to_numpy()
        base["r10"] = r10[liquid].to_numpy()
        events.append(base.iloc[::5])  # every 5th day is plenty for a baseline
        month_end = f.index.to_series().groupby(f.index.to_period("M")).max()
        keep = f.loc[sorted(set(month_end) | {f.index[-1]}), SNAPSHOT_COLS].copy()
        fwd21 = c.shift(-21) / c - 1 - bfwd[21].reindex(f.index)
        keep["fwd21_ex"] = fwd21.reindex(keep.index).clip(-0.6, 0.6)
        keep["latest"] = keep.index == f.index[-1]
        keep["liquid"] = liquid.reindex(keep.index).to_numpy()
        keep["symbol"] = sym
        keep["patterns"] = ""
        recent = patterns.recent(storage.load(market, sym).tail(40), 3)
        keep.loc[keep.index[-1], "patterns"] = ", ".join(n for n, _ in recent)
        snaps.append(keep.reset_index())
    events = pd.concat(events, ignore_index=True) if events else pd.DataFrame()
    snaps = pd.concat(snaps, ignore_index=True) if snaps else pd.DataFrame()
    return events, snaps
