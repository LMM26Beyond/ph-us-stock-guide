"""Write the Markdown reports under reports/."""
from datetime import date

import numpy as np
import pandas as pd

from . import analysis, patterns, score, storage, study
from .config import BENCHMARK, DATA_DIR, REPORTS_DIR

LABEL = {"ph": "Philippines (PSE)", "us": "United States"}
CUR = {"ph": "₱", "us": "$"}
INDEX_NAME = {"PSEI": "PSEi", "SPX": "S&P 500"}


def names(market: str) -> dict:
    p = DATA_DIR / market / "universe.csv"
    if not p.exists():
        return {}
    u = pd.read_csv(p, dtype=str, keep_default_na=False)
    return dict(zip(u["symbol"], u["name"]))


def pct(x, digits=1):
    return "–" if pd.isna(x) else f"{100 * x:+.{digits}f}%"


def analyze(market: str) -> None:
    """Full pass: signal study, today's scores, score validation."""
    print(f"Analysing {market} ...")
    events, snaps = analysis.run(market)
    if snaps.empty:
        print(f"  no {market} data; run update first")
        return
    stats = study.summarize(events)
    REPORTS_DIR.mkdir(exist_ok=True)
    stats.to_csv(REPORTS_DIR / f"signals_{market}.csv", index=False, float_format="%.3f")
    (REPORTS_DIR / f"signals_{market}.md").write_text(study.to_markdown(stats, market, events))
    bench = analysis.benchmark(market)
    today = score.latest(snaps, bench, stats)
    today["name"] = today["symbol"].map(names(market)).fillna("")
    cols = ["symbol", "name", "date", "close", "score", "trend", "momentum", "macd", "rsi", "candles",
            "rsi14", "ret3m", "ret12m", "sma50", "sma200", "atr14", "value20", "liquid", "patterns"]
    today[cols].sort_values("score", ascending=False).to_csv(
        DATA_DIR / market / "scores.csv", index=False, float_format="%.4g")
    val = score.validate(snaps, bench)
    (REPORTS_DIR / f"{market}.md").write_text(market_report(market, bench, today, stats, val))
    print(f"  wrote reports/{market}.md and reports/signals_{market}.md")


def regime(bench: pd.DataFrame, today: pd.DataFrame):
    b = bench.iloc[-1]
    liquid = today[today["liquid"] & today["sma200"].notna()]
    breadth = (liquid["close"] > liquid["sma200"]).mean() if len(liquid) else np.nan
    above200, above50 = b["close"] > b["sma200"], b["close"] > b["sma50"]
    if above200 and b["sma50"] > b["sma200"] and breadth >= 0.5:
        state = "Uptrend"
        advice = "Conditions favour buying strong stocks. Use stops."
    elif not above200 and b["sma50"] < b["sma200"] and (np.isnan(breadth) or breadth < 0.5):
        state = "Downtrend"
        advice = ("Most stocks fall with the market in a downtrend. Buy less, keep more cash, "
                  "and only consider the very strongest names.")
    else:
        state = "Mixed"
        advice = "No clear direction. Buy smaller positions and only the strongest setups."
    return state, advice, breadth


def market_report(market, bench, today, stats, val) -> str:
    cur, bname = CUR[market], BENCHMARK[market]
    b = bench.iloc[-1]
    state, advice, breadth = regime(bench, today)
    idx_raw = storage.load(market, bname, "indexes")
    idx_pats = ", ".join(n.replace("_", " ") for n, _ in patterns.recent(idx_raw.tail(40), 3)) or "none"
    L = [f"# {LABEL[market]} — market guide", "",
         f"Data up to **{bench.index[-1]:%a %d %b %Y}**. Generated {date.today():%d %b %Y}.", "",
         "> This is an automated technical analysis of past prices, not licensed financial "
         "advice. Signals are probabilities, not certainties. Check the company news and "
         "fundamentals and size every position so a stop-out is affordable.", "",
         f"## The market: {state}", "",
         f"{advice}", "",
         "| | |", "|---|---|",
         f"| {INDEX_NAME.get(bname, bname)} | {b['close']:,.2f} |",
         f"| vs 50-day average | {pct(b['close'] / b['sma50'] - 1)} |",
         f"| vs 200-day average | {pct(b['close'] / b['sma200'] - 1)} |",
         f"| 1 month / 3 months / 12 months | {pct(b['ret1m'])} / {pct(b['ret3m'])} / {pct(b['ret12m'])} |",
         f"| RSI (14) | {b['rsi14']:.0f} |",
         f"| Candles (last 3 days) | {idx_pats} |",
         f"| Stocks above their 200-day average | {'–' if np.isnan(breadth) else f'{100 * breadth:.0f}%'} |", ""]
    if market == "ph":
        L += ["PSEi before the first recorded real value is rebuilt from the AETF "
              "PSEi-tracker ETF, scaled to index points.", ""]

    liq = today[today["liquid"]]
    buys = liq[(liq["score"] >= 70) & (liq["close"] > liq["sma200"]) & (liq["rsi14"] <= 75)
               & (liq["close"] <= 1.3 * liq["sma50"])].sort_values("score", ascending=False).head(20)
    L += ["## Buy candidates", "",
          "Liquid stocks with a score of 70 or more, above their 200-day average, and not "
          "overextended (RSI ≤ 75, at most 30% above the 50-day average). The stop is 3 × ATR "
          "below the close; sell if a close falls below it.", ""]
    if state == "Downtrend":
        L += ["**The market is in a downtrend: treat this list as a watchlist.**", ""]
    L += table(buys, cur, stop=True) if len(buys) else ["None today.", ""]
    avoid = liq[liq["score"] <= 25].sort_values("score").head(20)
    L += ["## Avoid", "",
          "Liquid stocks with the weakest scores: falling trend and lagging the market. "
          "If you own one, check it in the portfolio section.", ""]
    L += table(avoid, cur) if len(avoid) else ["None today.", ""]

    works = stats[stats["verdict"] != "no reliable edge"] if not stats.empty else stats
    L += ["## Signals that have worked here", "",
          f"From the history study ([full table](signals_{market}.md)). Only these count in the score.", ""]
    if works.empty:
        L += ["None passed the test.", ""]
    else:
        for r in works.itertuples():
            L.append(f"- **{r.signal.replace('_', ' ')}** ({r.expects}): {r[5]:+.2f}% vs the index "
                     f"over 10 days, right way {r[7]:.0f}% of {r.count:,} times — {r.verdict}")
        L.append("")
    L += validation_text(val)
    return "\n".join(L) + "\n"


def table(df, cur, stop=False) -> list:
    head = "| Stock | Name | Close | Score | 3 mo | 12 mo | RSI | Recent candles |"
    sep = "|---|---|---:|---:|---:|---:|---:|---|"
    if stop:
        head += " Stop |"
        sep += "---:|"
    out = [head, sep]
    for r in df.itertuples():
        line = (f"| {r.symbol} | {r.name[:32]} | {cur}{r.close:,.2f} | {r.score:.0f} | {pct(r.ret3m, 0)} | "
                f"{pct(r.ret12m, 0)} | {r.rsi14:.0f} | {r.patterns.replace('_', ' ') or ''} |")
        if stop:
            line += f" {cur}{r.close - 3 * r.atr14:,.2f} |"
        out.append(line)
    return out + [""]


def validation_text(val: pd.DataFrame) -> list:
    if val is None or val.empty or val.shape[1] < 5:
        return ["## Has the score worked?", "", "Not enough history yet.", ""]
    mean = val.mean() * 100
    spread = (val[5] - val[1]).dropna()
    L = ["## Has the score worked?", "",
         f"Each past month-end ({len(val)} months), liquid stocks were split into five equal "
         "groups by score (without the candle part). Average return over the next month "
         "beyond the index:", "",
         "| Score group | 1 (weakest) | 2 | 3 | 4 | 5 (strongest) |", "|---|---:|---:|---:|---:|---:|",
         "| Next month vs index | " + " | ".join(f"{mean[g]:+.2f}%" for g in range(1, 6)) + " |", "",
         f"The strongest group beat the weakest in {100 * (spread > 0).mean():.0f}% of months "
         f"(average gap {spread.mean() * 100:+.2f}% a month).", ""]
    return L


def portfolio(path) -> str | None:
    """Hold or sell advice for each holding in a CSV: market,ticker,shares,buy_price,buy_date."""
    try:
        pf = pd.read_csv(path, dtype={"ticker": str, "market": str})
    except FileNotFoundError:
        return None
    L = ["# Your holdings", "", f"Generated {date.today():%d %b %Y}. Not financial advice.", "",
         "| Stock | Shares | Bought | Now | Gain | Score | Trailing stop | Action | Why |",
         "|---|---:|---:|---:|---:|---:|---:|---|---|"]
    for h in pf.itertuples():
        m, t = h.market.strip().lower(), h.ticker.strip().upper()
        f = analysis.stock_frame(m, t)
        if f is None:
            L.append(f"| {t} | {h.shares} | | | | | | ? | no price data for {m.upper()}:{t} |")
            continue
        last = f.iloc[-1]
        sc_path = DATA_DIR / m / "scores.csv"
        sc = pd.read_csv(sc_path).set_index("symbol")["score"] if sc_path.exists() else pd.Series(dtype=float)
        s = sc.get(t, np.nan)
        since = f[f.index >= pd.Timestamp(h.buy_date)] if isinstance(h.buy_date, str) and h.buy_date else f.tail(60)
        peak = since["close"].max() if len(since) else last["close"]
        stop = peak - 3 * last["atr14"]
        gain = last["close"] / h.buy_price - 1
        action, why = advise(last, s, stop)
        cur = CUR[m]
        L.append(f"| {m.upper()}:{t} | {h.shares:,} | {cur}{h.buy_price:,.2f} | {cur}{last['close']:,.2f} | "
                 f"{pct(gain)} | {'–' if np.isnan(s) else f'{s:.0f}'} | {cur}{stop:,.2f} | **{action}** | {why} |")
    L += ["", "The trailing stop is the highest close since you bought, minus 3 × ATR "
          "(average daily range). It rises with the price and never falls."]
    return "\n".join(L) + "\n"


def advise(last, s, stop):
    c = last["close"]
    if c < stop:
        return "SELL", "closed below the trailing stop: the uptrend has likely ended"
    if c < last["sma200"] and last["sma50"] < last["sma200"] and (np.isnan(s) or s < 35):
        return "SELL", "in a downtrend (below a falling 200-day average) and weak vs other stocks"
    if last["rsi14"] > 80:
        return "HOLD, tighten stop", "very overbought (RSI > 80); a pullback is common, so consider selling part"
    if not np.isnan(s) and s < 45:
        return "HOLD, watch", "weakening; sell if it closes below the stop"
    return "HOLD", "trend intact"
