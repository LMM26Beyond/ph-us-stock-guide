"""Company financials turned into value and quality measures, point in time.

Each measure on a date uses only figures filed on or before that date, so the
back-test never sees a number before the market did.

  earnings_yield   last fiscal year's net income / market value (E/P)
  book_yield       latest equity / market value (B/P)
  roe              net income / equity
  debt_ratio       liabilities / assets
  growth           net income growth over the previous fiscal year
  div_yield        last fiscal year's dividends per share / price
"""
import numpy as np
import pandas as pd

from .config import DATA_DIR

MEASURES = ["earnings_yield", "book_yield", "roe", "debt_ratio", "growth", "div_yield"]


def _annual(f: pd.DataFrame, item: str) -> pd.DataFrame:
    """Full-year values of a flow item (about 12 months long), first filing of each year."""
    x = f[(f["item"] == item) & f["start"].notna()].copy()
    if x.empty:
        return x
    days = (x["end"] - x["start"]).dt.days
    x = x[(days > 340) & (days < 380)]
    return x.sort_values("filed").drop_duplicates("end")[["end", "filed", "value"]]


def _instant(f: pd.DataFrame, item: str) -> pd.DataFrame:
    x = f[f["item"] == item]
    return x.sort_values("filed").drop_duplicates("end")[["end", "filed", "value"]]


def us_timeline(f: pd.DataFrame) -> pd.DataFrame:
    """One company's figures as of each filing date: a row per filing, columns per item."""
    # Figures in other currencies (some foreign filers) would not match US dollar prices.
    f = f[f["unit"].isin(["USD", "shares", "USD/shares"])]
    parts = {}
    ni = _annual(f, "net_income")
    if not ni.empty:
        ni = ni.sort_values("end")
        ni["prev"] = ni["value"].shift()
        parts["net_income"] = ni[["filed", "value"]]
        g = ni.dropna(subset=["prev"])
        parts["growth"] = g.assign(value=(g["value"] - g["prev"]) / g["prev"].abs().replace(0, np.nan))[["filed", "value"]]
    dps = _annual(f, "dividends_per_share")
    if not dps.empty:
        parts["dps"] = dps[["filed", "value"]]
    for item in ("equity", "assets", "liabilities", "shares"):
        x = _instant(f, item)
        if not x.empty:
            parts[item] = x[["filed", "value"]]
    if not parts:
        return pd.DataFrame()
    frames = [p.sort_values("filed").set_index("filed")["value"].rename(k).groupby(level=0).last()
              for k, p in parts.items()]
    return pd.concat(frames, axis=1).sort_index().ffill()


def load_us() -> dict:
    p = DATA_DIR / "us" / "fundamentals.csv.gz"
    if not p.exists():
        return {}
    df = pd.read_csv(p, parse_dates=["start", "end", "filed"])
    return {sym: us_timeline(g) for sym, g in df.groupby("symbol")}


def attach(rows: pd.DataFrame, market: str) -> pd.DataFrame:
    """Add the measures to rows of (symbol, date, close), using figures filed by each date."""
    timelines = load_us() if market == "us" else load_ph()
    out = []
    for sym, g in rows.groupby("symbol", sort=False):
        t = timelines.get(sym)
        g = g.sort_values("date")
        if t is None or t.empty:
            out.append(g.assign(**{m: np.nan for m in MEASURES}))
            continue
        m = pd.merge_asof(g[["date"]].reset_index(), t.reset_index().rename(columns={"filed": "date"}),
                          on="date", direction="backward").set_index("index")
        g = g.join(m.drop(columns="date"))
        out.append(g.assign(**measures(g)))
    res = pd.concat(out) if out else rows
    return res.drop(columns=[c for c in ("net_income", "dps", "equity", "assets", "liabilities", "shares")
                             if c in res.columns])


def measures(g: pd.DataFrame) -> dict:
    col = lambda c: g[c] if c in g else pd.Series(np.nan, index=g.index)
    mcap = g["close"] * col("shares")
    mcap = mcap.where(mcap > 0)
    eq = col("equity").where(col("equity") > 0)
    return {
        "earnings_yield": col("net_income") / mcap,
        "book_yield": col("equity") / mcap,
        "roe": col("net_income") / eq,
        "debt_ratio": col("liabilities") / col("assets").where(col("assets") > 0),
        "growth": col("growth").clip(-5, 5),
        "div_yield": col("dps") / g["close"],
    }


def load_ph() -> dict:
    """Parsed PSE Edge financials (not available yet)."""
    return {}
