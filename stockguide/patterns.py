"""Candlestick patterns.

Each pattern is a boolean Series: True on the day the pattern completes.
Reversal patterns only count when the trend before them points the other way
(a hammer means something after a fall, not after a rise). See
docs/candlesticks.md for what each one looks like and why it matters.
"""
import pandas as pd

# name -> +1 (bullish) or -1 (bearish)
DIRECTION = {
    "hammer": 1, "inverted_hammer": 1, "bullish_engulfing": 1, "piercing_line": 1,
    "bullish_harami": 1, "morning_star": 1, "three_white_soldiers": 1,
    "bullish_marubozu": 1, "dragonfly_doji": 1,
    "hanging_man": -1, "shooting_star": -1, "bearish_engulfing": -1,
    "dark_cloud_cover": -1, "bearish_harami": -1, "evening_star": -1,
    "three_black_crows": -1, "bearish_marubozu": -1, "gravestone_doji": -1,
    "doji": 0,
}


def detect(df: pd.DataFrame) -> pd.DataFrame:
    o, h, l, c = df["open"], df["high"], df["low"], df["close"]
    body = (c - o).abs()
    rng = (h - l).where(h > l)
    upper = h - pd.concat([o, c], axis=1).max(axis=1)
    lower = pd.concat([o, c], axis=1).min(axis=1) - l
    green, red = c > o, c < o
    avg_body = body.rolling(20, min_periods=10).mean().shift()
    long_body = body > avg_body
    top, bot = pd.concat([o, c], axis=1).max(axis=1), pd.concat([o, c], axis=1).min(axis=1)
    mid = (o + c) / 2

    # Trend into the pattern: the close before it versus 5 days earlier and the 10-day average.
    sma10 = c.rolling(10, min_periods=10).mean()
    pc = c.shift()
    down = (pc < c.shift(6)) & (pc < sma10.shift())
    up = (pc > c.shift(6)) & (pc > sma10.shift())
    down3, up3 = down.shift(2, fill_value=False), up.shift(2, fill_value=False)

    p = lambda s, k=1: s.shift(k)
    small = body <= 0.35 * rng
    doji = body <= 0.1 * rng
    hammer_shape = small & (lower >= 2 * body) & (upper <= 0.15 * rng)
    star_shape = small & (upper >= 2 * body) & (lower <= 0.15 * rng)

    out = pd.DataFrame(index=df.index)
    out["doji"] = doji
    out["dragonfly_doji"] = doji & (upper <= 0.1 * rng) & (lower >= 0.6 * rng) & down
    out["gravestone_doji"] = doji & (lower <= 0.1 * rng) & (upper >= 0.6 * rng) & up
    out["hammer"] = hammer_shape & ~doji & down
    out["hanging_man"] = hammer_shape & ~doji & up
    out["inverted_hammer"] = star_shape & ~doji & down
    out["shooting_star"] = star_shape & ~doji & up
    out["bullish_engulfing"] = down & p(red) & green & (o <= p(c)) & (c >= p(o)) & (body > p(body))
    out["bearish_engulfing"] = up & p(green) & red & (o >= p(c)) & (c <= p(o)) & (body > p(body))
    out["piercing_line"] = (down & p(red) & p(long_body) & green & (o < p(c))
                            & (c > p(mid)) & (c < p(o)))
    out["dark_cloud_cover"] = (up & p(green) & p(long_body) & red & (o > p(c))
                               & (c < p(mid)) & (c > p(o)))
    out["bullish_harami"] = down & p(red) & p(long_body) & (top < p(o)) & (bot > p(c)) & (body < 0.6 * p(body))
    out["bearish_harami"] = up & p(green) & p(long_body) & (top < p(c)) & (bot > p(o)) & (body < 0.6 * p(body))
    out["morning_star"] = (down3 & p(red, 2) & p(long_body, 2) & (p(body) <= 0.3 * p(body, 2))
                           & (p(top) <= p(c, 2)) & green & (c > p(mid, 2)))
    out["evening_star"] = (up3 & p(green, 2) & p(long_body, 2) & (p(body) <= 0.3 * p(body, 2))
                           & (p(bot) >= p(c, 2)) & red & (c < p(mid, 2)))
    strong_g = green & long_body & (upper <= 0.3 * body)
    strong_r = red & long_body & (lower <= 0.3 * body)
    out["three_white_soldiers"] = (down3 & strong_g & p(strong_g) & p(strong_g, 2)
                                   & (c > p(c)) & (p(c) > p(c, 2))
                                   & (o >= p(o)) & (o <= p(c)) & (p(o) >= p(o, 2)) & (p(o) <= p(c, 2)))
    out["three_black_crows"] = (up3 & strong_r & p(strong_r) & p(strong_r, 2)
                                & (c < p(c)) & (p(c) < p(c, 2))
                                & (o <= p(o)) & (o >= p(c)) & (p(o) <= p(o, 2)) & (p(o) >= p(c, 2)))
    maru = (body >= 0.9 * rng) & (body > 1.5 * avg_body)
    out["bullish_marubozu"] = maru & green
    out["bearish_marubozu"] = maru & red
    return out.fillna(False).astype(bool)


def recent(df: pd.DataFrame, days: int = 3) -> list[tuple[str, pd.Timestamp]]:
    """Patterns seen in the last few candles, newest first."""
    pats = detect(df).tail(days)
    found = []
    for ts in reversed(pats.index):
        for name in pats.columns:
            if name != "doji" and pats.at[ts, name]:
                found.append((name, ts))
    return found
