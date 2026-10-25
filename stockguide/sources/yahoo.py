"""Daily candles from Yahoo Finance through the yfinance library.

Close is adjusted for splits but not dividends, so recent prices match
what a broker shows.
"""
import time

import pandas as pd

MAP = {"Open": "open", "High": "high", "Low": "low", "Close": "close", "Volume": "volume"}


def download(symbols: list[str], start: str, batch: int = 50, pause: float = 1.0) -> dict:
    """Return {symbol: DataFrame} for the symbols Yahoo had data for."""
    import yfinance as yf

    out = {}
    for i in range(0, len(symbols), batch):
        chunk = symbols[i:i + batch]
        try:
            raw = yf.download(chunk, start=start, interval="1d", auto_adjust=False,
                              actions=False, group_by="ticker", threads=True,
                              progress=False, timeout=30)
        except Exception as e:  # one bad batch must not stop the run
            print(f"  yahoo batch failed ({chunk[0]}..): {e}")
            raw = None
        if raw is not None and not raw.empty:
            for s in chunk:
                df = _pick(raw, s)
                if df is not None and not df.dropna(subset=["close"]).empty:
                    out[s] = df
        if i + batch < len(symbols):
            time.sleep(pause)
    return out


def _pick(raw: pd.DataFrame, symbol: str):
    if isinstance(raw.columns, pd.MultiIndex):
        if symbol not in raw.columns.get_level_values(0):
            return None
        df = raw[symbol]
    else:
        df = raw
    df = df.rename(columns=MAP)
    if "close" not in df:
        return None
    return df[[c for c in MAP.values() if c in df]]
