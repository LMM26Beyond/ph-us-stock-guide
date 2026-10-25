import numpy as np
import pandas as pd

from stockguide import indicators, patterns


def frame(rows):
    idx = pd.bdate_range("2024-01-01", periods=len(rows))
    return pd.DataFrame(rows, columns=["open", "high", "low", "close"], index=idx).assign(volume=1000)


def falling(n=12, start=100.0):
    rows, p = [], start
    for _ in range(n):
        rows.append((p, p + 0.3, p - 1.3, p - 1.0))
        p -= 1.0
    return rows, p


def rising(n=12, start=100.0):
    rows, p = [], start
    for _ in range(n):
        rows.append((p, p + 1.3, p - 0.3, p + 1.0))
        p += 1.0
    return rows, p


def last(df, name):
    return bool(patterns.detect(df)[name].iloc[-1])


def test_hammer_after_fall_only():
    rows, p = falling()
    hammer = (p, p + 0.05, p - 3.0, p + 0.5)
    assert last(frame(rows + [hammer]), "hammer")
    rows, p = rising()
    assert not last(frame(rows + [(p, p + 0.05, p - 3.0, p + 0.5)]), "hammer")
    assert last(frame(rows + [(p, p + 0.05, p - 3.0, p + 0.5)]), "hanging_man")


def test_engulfing():
    rows, p = falling()
    rows[-1] = (p + 1.0, p + 1.1, p - 0.1, p)          # red day
    assert last(frame(rows + [(p - 0.2, p + 1.6, p - 0.3, p + 1.5)]), "bullish_engulfing")
    rows, p = rising()
    rows[-1] = (p - 1.0, p + 0.1, p - 1.1, p)          # green day
    assert last(frame(rows + [(p + 0.2, p + 0.3, p - 1.6, p - 1.5)]), "bearish_engulfing")


def test_morning_and_evening_star():
    rows, p = falling(14)
    rows += [(p, p + 0.1, p - 3.1, p - 3.0), (p - 3.4, p - 3.1, p - 3.8, p - 3.3), (p - 3.2, p - 0.5, p - 3.3, p - 0.8)]
    assert last(frame(rows), "morning_star")
    rows, p = rising(14)
    rows += [(p, p + 3.1, p - 0.1, p + 3.0), (p + 3.4, p + 3.8, p + 3.1, p + 3.3), (p + 3.2, p + 3.3, p + 0.5, p + 0.8)]
    assert last(frame(rows), "evening_star")


def test_rsi_bounds_and_trend():
    up = pd.Series(np.arange(1, 100, dtype=float))
    assert indicators.rsi(up).iloc[-1] == 100
    zig = pd.Series([10.0, 11.0] * 50)
    assert 40 < indicators.rsi(zig).iloc[-1] < 60
