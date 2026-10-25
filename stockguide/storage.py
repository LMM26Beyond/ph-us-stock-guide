"""Daily candles on disk: one CSV per symbol under data/<market>/<kind>/.

Columns: date, open, high, low, close, volume. Dates are trading days.
"""
from pathlib import Path

import pandas as pd

from .config import DATA_DIR

COLUMNS = ["open", "high", "low", "close", "volume"]


def path_for(market: str, symbol: str, kind: str = "stocks") -> Path:
    safe = symbol.replace("/", "_").replace("^", "_")
    return DATA_DIR / market / kind / f"{safe}.csv"


def load(market: str, symbol: str, kind: str = "stocks") -> pd.DataFrame:
    p = path_for(market, symbol, kind)
    if not p.exists():
        return pd.DataFrame(columns=COLUMNS, index=pd.DatetimeIndex([], name="date"))
    df = pd.read_csv(p, parse_dates=["date"], index_col="date")
    return df[COLUMNS]


def last_date(market: str, symbol: str, kind: str = "stocks"):
    p = path_for(market, symbol, kind)
    if not p.exists():
        return None
    # Read only the tail; files are sorted by date.
    with p.open("rb") as f:
        f.seek(0, 2)
        size = f.tell()
        f.seek(max(0, size - 512))
        tail = f.read().decode().strip().splitlines()
    if len(tail) < 2 and size <= 512:
        return None
    return pd.Timestamp(tail[-1].split(",")[0])


def merge_save(market: str, symbol: str, new: pd.DataFrame, kind: str = "stocks") -> int:
    """Add new candles to the stored ones. Newer rows win. Returns rows added."""
    if new is None or new.empty:
        return 0
    new = clean(new)
    if new.empty:
        return 0
    old = load(market, symbol, kind)
    before = len(old)
    df = pd.concat([old, new]) if before else new
    df = df[~df.index.duplicated(keep="last")].sort_index()
    p = path_for(market, symbol, kind)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index_label="date", float_format="%.6g")
    return len(df) - before


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.index = pd.to_datetime(df.index).tz_localize(None).normalize()
    df.index.name = "date"
    for c in COLUMNS:
        if c not in df:
            df[c] = float("nan")
    df = df[COLUMNS].apply(pd.to_numeric, errors="coerce")
    df = df.dropna(subset=["close"])
    df = df[df["close"] > 0]
    # Fill a missing open/high/low with the close so a candle is never broken.
    for c in ("open", "high", "low"):
        df[c] = df[c].fillna(df["close"])
    df["high"] = df[["open", "high", "low", "close"]].max(axis=1)
    df["low"] = df[["open", "high", "low", "close"]].min(axis=1)
    df["volume"] = df["volume"].fillna(0)
    return df


def symbols(market: str, kind: str = "stocks") -> list[str]:
    d = DATA_DIR / market / kind
    return sorted(p.stem for p in d.glob("*.csv")) if d.exists() else []
