"""Company financials turned into value and quality measures, point in time.

Each measure on a date uses only figures filed on or before that date, so the
back-test never sees a number before the market did.

  earnings_yield   last fiscal year's net income / market value (E/P)
  book_yield       latest equity / market value (B/P)
  roe              net income / equity
  debt_ratio       liabilities / assets
  growth           net income growth over the previous fiscal year
  div_yield        dividends per share over the last year / price
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
    """PSE Edge only shows each company's latest figures, so there is no history to
    attach to past dates; see ph_snapshot() for today's measures."""
    return {}


def ph_snapshot(raw_dir=None, asof=None) -> pd.DataFrame:
    """Today's measures for every PSE company from its saved PSE Edge pages."""
    from .sources.pse_fundamentals import parse_dividends, parse_financials, parse_stock_data
    raw_dir = raw_dir or DATA_DIR / "ph" / "fundamentals" / "raw"
    asof = pd.Timestamp(asof) if asof is not None else pd.Timestamp.today().normalize()
    rows = []
    for f in sorted(raw_dir.glob("*_financials.html")):
        sym = f.name[: -len("_financials.html")]
        fin = parse_financials(f.read_text(errors="replace"))
        sd = raw_dir / f"{sym}_stock_data.html"
        mk = parse_stock_data(sd.read_text(errors="replace")) if sd.exists() else {}
        fin = check_scale(fin, mk.get("shares"))
        row = {"symbol": sym, **ph_measures(fin, mk.get("market_cap"))}
        dv = raw_dir / f"{sym}_dividends.html"
        dps = parse_dividends(dv.read_text(errors="replace"), asof) if dv.exists() else None
        price = mk.get("price") or (mk["market_cap"] / mk["shares"] if mk.get("market_cap") and mk.get("shares") else None)
        if dps is not None and price:
            row["div_yield"] = dps / price
        rows.append(row)
    return pd.DataFrame(rows)


def check_scale(fin: dict, shares) -> dict:
    """Companies describe their units loosely ("PHP" may mean thousands). Book value per
    share (or EPS) times shares outstanding tells the real scale; figures in another
    currency, or that cannot be checked against either, are dropped."""
    out = {}
    for key, d in fin.items():
        if d.get("foreign"):
            continue   # e.g. ICT reports in US dollars; prices are in pesos
        ref = None
        for per_share, total in (("Book Value Per Share", "Stockholders' Equity - Parent"),
                                 ("Earnings/(Loss) Per Share (Basic)", "Net Income/(Loss) Attributable to Parent")):
            ps, tot = (d.get(per_share) or (None,))[0], (d.get(total) or (None,))[0]
            if shares and ps and tot and ps * tot > 0:
                ref = ps * shares / tot
                break
        k = None
        if ref:
            p = round(np.log10(ref) / 3) * 3
            if abs(np.log10(ref) - p) < 0.35 and p in (0, 3, 6):   # within ~2x of 1, 1,000 or 1,000,000
                k = 10.0 ** p
        if k is None and ref:
            continue   # another currency, or totals that don't match the per-share figures
        k = k or 1.0
        out[key] = {n: (tuple(None if v is None else v * k for v in vals)
                        if isinstance(vals, tuple) and "Per Share" not in n else vals)
                    for n, vals in d.items()}
    return out


def ph_measures(fin: dict, mcap) -> dict:
    a, q = fin.get("annual", {}), fin.get("quarterly", {})
    get = lambda d, k, i: (d.get(k) or (None,) * 4)[i] if d else None
    ni = "Net Income/(Loss) Attributable to Parent"
    # Trailing 12 months: last full year, plus this year to date, minus last year to date.
    ttm = get(a, ni, 0)
    if a and q and q["end"] > a["end"]:
        fresh = (q["end"] - a["end"]).days <= 370
        ytd, ytd_prev = get(q, ni, 2), get(q, ni, 3)
        ttm = ttm + ytd - ytd_prev if fresh and None not in (ttm, ytd, ytd_prev) else None
    if q and None not in (get(q, ni, 2), get(q, ni, 3)) and (q["end"] > a.get("end", q["end"]) if a else True):
        cur, prev = get(q, ni, 2), get(q, ni, 3)
    else:
        cur, prev = get(a, ni, 0), get(a, ni, 1)
    growth = (cur - prev) / abs(prev) if None not in (cur, prev) and prev else None
    bal = q if q and q.get("Total Assets") else a
    equity = get(bal, "Stockholders' Equity - Parent", 0)
    assets, liab = get(bal, "Total Assets", 0), get(bal, "Total Liabilities", 0)
    ok = lambda x: x is not None and x > 0
    return {
        "earnings_yield": ttm / mcap if ok(mcap) and ttm is not None else np.nan,
        "book_yield": equity / mcap if ok(mcap) and equity is not None else np.nan,
        "roe": ttm / equity if ok(equity) and ttm is not None else np.nan,
        "debt_ratio": liab / assets if ok(assets) and liab is not None else np.nan,
        "growth": float(np.clip(growth, -5, 5)) if growth is not None else np.nan,
        "div_yield": np.nan,
        "fin_period": (q or a).get("end") if (q or a) else None,
    }


def latest(market: str, today: pd.DataFrame) -> pd.DataFrame:
    """Add today's measures to the latest-score rows (symbol, date, close)."""
    if market == "ph":
        snap = ph_snapshot(asof=today["date"].max()) if (DATA_DIR / "ph" / "fundamentals" / "raw").exists() else pd.DataFrame()
        if snap.empty:
            return today.assign(**{m: np.nan for m in MEASURES})
        return today.drop(columns=[m for m in MEASURES if m in today]).merge(
            snap[["symbol", *MEASURES]], on="symbol", how="left")
    return attach(today, market)
