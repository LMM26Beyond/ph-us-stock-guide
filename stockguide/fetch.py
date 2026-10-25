"""Download and update daily candles. Safe to re-run: each symbol only
fetches the days after its last stored candle (with a few days of overlap
so late corrections are picked up).
"""
import time
from datetime import date, timedelta

import pandas as pd

from . import storage
from .config import DATA_DIR, INDEXES, PH_START, US_START_YEARS
from .sources import pse, us_universe, yahoo

OVERLAP_DAYS = 7


def _start_for(market: str, symbol: str, default: str, kind: str = "stocks") -> str:
    last = storage.last_date(market, symbol, kind)
    if last is None:
        return default
    return (last - timedelta(days=OVERLAP_DAYS)).date().isoformat()


def _deadline(max_minutes):
    return time.time() + max_minutes * 60 if max_minutes else None


def universe(market: str, refresh: bool = True) -> pd.DataFrame:
    p = DATA_DIR / market / "universe.csv"
    if refresh or not p.exists():
        df = pse.directory() if market == "ph" else us_universe.fetch()
        p.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(p, index=False)
        return df
    return pd.read_csv(p, dtype=str, keep_default_na=False)


def update_ph(limit=None, max_minutes=None) -> None:
    uni = universe("ph")
    if limit:
        uni = uni.head(limit)
    stop = _deadline(max_minutes)
    added = failed = 0
    for n, r in enumerate(uni.itertuples(), 1):
        if stop and time.time() > stop:
            print(f"PH: time budget reached after {n - 1} symbols; re-run to continue")
            break
        start = _start_for("ph", r.symbol, PH_START)
        try:
            added += storage.merge_save("ph", r.symbol, pse.history(r.cmpy_id, r.security_id, start))
        except Exception as e:
            failed += 1
            print(f"  {r.symbol}: {e}")
        time.sleep(0.3)
    print(f"PH stocks: {len(uni)} symbols, {added} new candles, {failed} failed")
    update_psei()


def update_psei() -> None:
    """PSEi: real values from Yahoo (PSEI.PS) and the PSE Edge index page, kept in
    PSEI_actual.csv, spliced onto the AETF (PSEi tracker ETF) history scaled to
    index points for the years before real values were recorded."""
    got = yahoo.download([INDEXES["ph"]["PSEI"]], start=_start_for("ph", "PSEI_actual", "2000-01-01", "indexes"))
    actual = got.get(INDEXES["ph"]["PSEI"])
    storage.merge_save("ph", "PSEI_actual", actual, "indexes")
    if actual is None or actual.empty:
        # Fall back to today's close from PSE Edge (no open/high/low there).
        try:
            snap = pse.index_snapshot().set_index("index")
            if "PSEi" in snap.index:
                v = snap.loc["PSEi", "value"]
                today = pd.Timestamp(date.today())
                if today.dayofweek < 5:
                    storage.merge_save("ph", "PSEI_actual", pd.DataFrame(
                        {"open": v, "high": v, "low": v, "close": v, "volume": 0}, index=[today]), "indexes")
        except Exception as e:
            print(f"  PSEi snapshot failed: {e}")
    real = storage.load("ph", "PSEI_actual", "indexes")
    etf = storage.load("ph", "AETF")
    if real.empty:
        print("PSEi: no real values yet")
        return
    if not etf.empty:
        first = real.index[0]
        base = etf[etf.index <= first]
        if not base.empty:
            scale = real["close"].iloc[0] / base["close"].iloc[-1]
            proxy = etf[etf.index < first][storage.COLUMNS].copy()
            proxy[["open", "high", "low", "close"]] *= scale
            proxy["volume"] = 0
            real = pd.concat([proxy, real])
    p = storage.path_for("ph", "PSEI", "indexes")
    if p.exists():
        p.unlink()
    storage.merge_save("ph", "PSEI", real, "indexes")
    print(f"PSEi: {len(real)} days ({real.index[0].date()} to {real.index[-1].date()})")


def update_us(limit=None, max_minutes=None, batch: int = 50) -> None:
    uni = universe("us")
    if limit:
        uni = uni.head(limit)
    default = (date.today() - timedelta(days=365 * US_START_YEARS)).isoformat()
    starts = {r.yahoo: _start_for("us", r.symbol, default) for r in uni.itertuples()}
    to_sym = dict(zip(uni["yahoo"], uni["symbol"]))
    # Symbols sharing a start date go to Yahoo together; oldest gaps first.
    groups = {}
    for y, s in starts.items():
        groups.setdefault(s, []).append(y)
    stop = _deadline(max_minutes)
    added = done = 0
    missing = []
    for start in sorted(groups):
        syms = groups[start]
        for i in range(0, len(syms), batch):
            if stop and time.time() > stop:
                print(f"US: time budget reached after {done} symbols; re-run to continue")
                print(f"US stocks: {added} new candles")
                return update_us_indexes()
            chunk = syms[i:i + batch]
            got = yahoo.download(chunk, start=start, batch=batch)
            for y in chunk:
                if y in got:
                    added += storage.merge_save("us", to_sym[y], got[y])
                else:
                    missing.append(y)
            done += len(chunk)
            if done % 1000 < batch:
                print(f"  US: {done}/{len(starts)} symbols")
    print(f"US stocks: {len(uni)} symbols, {added} new candles, {len(missing)} with no data")
    update_us_indexes()


def update_us_indexes() -> None:
    idx = INDEXES["us"]
    for name, ysym in idx.items():
        got = yahoo.download([ysym], start=_start_for("us", name, "1990-01-01", "indexes"))
        n = storage.merge_save("us", name, got.get(ysym), "indexes")
        print(f"  {name} ({ysym}): {n} new days")


def update_fundamentals(markets=("ph", "us"), limit=None) -> None:
    """Company financials: PSE Edge pages for PH, SEC company facts for US."""
    from .sources import pse_fundamentals, sec
    if "us" in markets:
        try:
            _us_fundamentals(sec, limit)
        except Exception as e:  # keep going so the PH half still gets saved
            print(f"US fundamentals failed: {e!r}")
    if "ph" in markets:
        uni = universe("ph")
        pse_fundamentals.dump(uni.head(limit) if limit else uni, DATA_DIR / "ph" / "fundamentals" / "raw")


def _us_fundamentals(sec, limit) -> None:
    uni = universe("us")
    syms = uni["symbol"].tolist()[:limit] if limit else uni["symbol"].tolist()
    df = sec.download(syms)
    p = DATA_DIR / "us" / "fundamentals.csv.gz"
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False)
    print(f"US fundamentals: {len(df):,} facts for {df['symbol'].nunique() if len(df) else 0} companies")
