"""Technical indicators on a daily candle frame (open, high, low, close, volume)."""
import numpy as np
import pandas as pd


def rsi(close: pd.Series, n: int = 14) -> pd.Series:
    d = close.diff()
    up = d.clip(lower=0).ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1 / n, adjust=False, min_periods=n).mean()
    rs = up / dn.replace(0, np.nan)
    return (100 - 100 / (1 + rs)).where(dn > 0, 100.0).where(up.notna())


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    prev = df["close"].shift()
    tr = pd.concat([df["high"] - df["low"], (df["high"] - prev).abs(), (df["low"] - prev).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False, min_periods=n).mean()


def add(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with indicator columns added."""
    df = df.copy()
    c = df["close"]
    for n in (10, 20, 50, 200):
        df[f"sma{n}"] = c.rolling(n, min_periods=n).mean()
    ema12, ema26 = c.ewm(span=12, adjust=False).mean(), c.ewm(span=26, adjust=False).mean()
    df["macd"] = ema12 - ema26
    df["macd_signal"] = df["macd"].ewm(span=9, adjust=False).mean()
    df["macd_hist"] = df["macd"] - df["macd_signal"]
    df["rsi14"] = rsi(c)
    df["atr14"] = atr(df)
    sd = c.rolling(20, min_periods=20).std()
    df["bb_upper"], df["bb_lower"] = df["sma20"] + 2 * sd, df["sma20"] - 2 * sd
    df["vol20"] = df["volume"].rolling(20, min_periods=20).mean()
    df["value20"] = (c * df["volume"]).rolling(20, min_periods=20).mean()
    df["hi52"] = df["high"].rolling(252, min_periods=120).max()
    df["lo52"] = df["low"].rolling(252, min_periods=120).min()
    for n, name in ((21, "ret1m"), (63, "ret3m"), (126, "ret6m"), (252, "ret12m")):
        df[name] = c / c.shift(n) - 1
    # 12-month return skipping the latest month (classic momentum measure).
    df["mom12_1"] = c.shift(21) / c.shift(252) - 1
    df["sma200_slope"] = df["sma200"] / df["sma200"].shift(20) - 1
    return df
