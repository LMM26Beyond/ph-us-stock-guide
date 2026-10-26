"""Write the Markdown reports under reports/."""
from datetime import date

import numpy as np
import pandas as pd

from . import alerts, analysis, backtest, fundamentals, patterns, score, storage, study
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
    today = fundamentals.latest(market, today)
    cols = ["symbol", "name", "date", "close", "score", "trend", "momentum", "macd", "rsi", "candles",
            "rsi14", "ret3m", "ret12m", "sma50", "sma200", "atr14", "value20", "liquid", "patterns",
            *fundamentals.MEASURES]
    today[cols].sort_values("score", ascending=False).to_csv(
        DATA_DIR / market / "scores.csv", index=False, float_format="%.4g")
    val = score.validate(snaps, bench)
    (REPORTS_DIR / f"{market}.md").write_text(market_report(market, bench, today, stats, val))
    for line in alerts.run(market, bench.index[-1], regime(bench, today)[0], today):
        print(f"  alert: {line}")
    bt = backtest.run(market, (events, snaps))
    (REPORTS_DIR / f"backtest_{market}.md").write_text(backtest.to_markdown(market, bt))
    print(f"  wrote reports/{market}.md, signals_{market}.md and backtest_{market}.md")


def regime(bench: pd.DataFrame, today: pd.DataFrame):
    b = bench.iloc[-1]
    liquid = today[today["liquid"] & today["sma200"].notna()]
    breadth = (liquid["close"] > liquid["sma200"]).mean() if len(liquid) else np.nan
    above200, above50 = b["close"] > b["sma200"], b["close"] > b["sma50"]
    if above200 and b["sma50"] > b["sma200"] and breadth >= 0.5:
        state = "Uptrend"
        advice = "Conditions favour buying strong stocks."
    elif not above200 and b["sma50"] < b["sma200"] and (np.isnan(breadth) or breadth < 0.5):
        state = "Downtrend"
        advice = ("Most stocks fall with the market in a downtrend. Expect bigger swings and "
                  "consider buying smaller amounts.")
    else:
        state = "Mixed"
        advice = "No clear direction."
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
    rules = backtest.Rules()
    buys = backtest.candidates(liq, rules).head(20)
    L += ["## Buy candidates", "",
          f"Liquid stocks with a score of {rules.min_score:.0f} or more, above their 200-day "
          "average, not overextended (RSI ≤ 75, at most 30% above the 50-day average) and not "
          f"too erratic (average daily range at most {100 * rules.max_atr_pct:.0f}% of the price). "
          f"Hold while the score stays at {rules.sell_below:.0f} or more; sell when it drops "
          f"below at a month-end. These are the rules tested in [the back-test](backtest_{market}.md).", ""]
    if state == "Downtrend":
        L += ["**The market is in a downtrend.** In the back-test, buying anyway did better than "
              "waiting (waiting missed the rebounds), but expect bigger swings: consider "
              "smaller amounts.", ""]
    L += table(buys, cur) if len(buys) else ["None today.", ""]
    example = 100_000 if market == "ph" else 10_000
    L += ["**How much to buy.** Split the money you set aside for "
          f"{'PSE' if market == 'ph' else 'US'} stocks into {backtest.SLOTS[market]} equal parts and put "
          f"one part in each pick, working down the list as you have free parts: with {cur}{example:,} "
          f"that is {cur}{example // backtest.SLOTS[market]:,} a stock. Holding fewer stocks made the swings "
          "bigger without raising the return in [the back-test](backtest_" + market + ".md)."
          + (" *Min. buy* is the cost of one PSE board lot, the smallest amount you can buy."
             if market == "ph" else "")
          + " Run the portfolio command with your cash in portfolio.csv to get share counts.", ""]
    L += ["P/E, P/B, ROE (return on equity), profit growth and dividend yield come from the companies' "
          "latest reports (" + ("PSE Edge; dividend yield is cash dividends with an ex-date in the last "
          "12 months divided by the price" if market == "ph" else "SEC filings") + "). They are "
          "shown for context and are not part of the score yet. A loss or a very high P/E is "
          "worth a closer look before buying.", ""]
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


def ratio(yld) -> str:
    """P/E or P/B from an earnings or book yield."""
    if pd.isna(yld):
        return "–"
    if yld <= 0:
        return "loss"
    return "n/m" if yld < 0.01 else f"{1 / yld:.1f}"   # above 100: not meaningful


def growth(g) -> str:
    return "n/m" if pd.notna(g) and abs(g) >= 5 else pct(g, 0)


def table(df, cur) -> list:
    lots = cur == CUR["ph"]   # PSE shares trade in board lots
    out = ["| Stock | Name | Close |" + (" Min. buy |" if lots else "") + " Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |",
           "|---|---|---:|" + ("---:|" if lots else "") + "---:|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
    for r in df.itertuples():
        min_buy = f" {cur}{backtest.board_lot(r.close) * r.close:,.0f} |" if lots else ""
        line = (f"| {r.symbol} | {r.name[:32]} | {cur}{r.close:,.2f} |{min_buy} {r.score:.0f} | {pct(r.ret3m, 0)} | "
                f"{pct(r.ret12m, 0)} | {r.rsi14:.0f} | {ratio(r.earnings_yield)} | {ratio(r.book_yield)} | "
                f"{pct(r.roe, 0)} | {growth(r.growth)} | {"–" if pd.isna(r.div_yield) else f"{100 * r.div_yield:.1f}%"} | {r.patterns.replace('_', ' ') or ''} |")
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
    sell_below = backtest.Rules().sell_below
    is_cash = pf["ticker"].str.strip().str.upper() == "CASH"
    cash = pf[is_cash].groupby(pf["market"].str.strip().str.lower())["shares"].sum()
    pf = pf[~is_cash]
    held_value, held = {}, {}
    L = ["# Your holdings", "", f"Generated {date.today():%d %b %Y}. Not financial advice.", "",
         "| Stock | Shares | Bought | Now | Gain | Score | Action | Why |",
         "|---|---:|---:|---:|---:|---:|---|---|"]
    for h in pf.itertuples():
        m, t = h.market.strip().lower(), h.ticker.strip().upper()
        f = analysis.stock_frame(m, t)
        if f is None:
            L.append(f"| {t} | {h.shares} | | | | | ? | no price data for {m.upper()}:{t} |")
            continue
        last = f.iloc[-1]
        sc_path = DATA_DIR / m / "scores.csv"
        sc = pd.read_csv(sc_path).set_index("symbol")["score"] if sc_path.exists() else pd.Series(dtype=float)
        s = sc.get(t, np.nan)
        gain = last["close"] / h.buy_price - 1
        action, why = advise(last, s, sell_below)
        held_value[m] = held_value.get(m, 0) + h.shares * last["close"]
        held.setdefault(m, set()).add(t)
        cur = CUR[m]
        L.append(f"| {m.upper()}:{t} | {h.shares:,} | {cur}{h.buy_price:,.2f} | {cur}{last['close']:,.2f} | "
                 f"{pct(gain)} | {'–' if np.isnan(s) else f'{s:.0f}'} | **{action}** | {why} |")
    L += ["", f"The rule tested in the back-test: hold while the score is {sell_below:.0f} or more, "
          "sell when it is lower at a month-end. Tight stop-losses did worse in the back-test, "
          "because they sold good stocks on normal dips."]
    for m, c in cash.items():
        L += buy_plan(m, float(c), held_value.get(m, 0.0), held.get(m, set()))
    return "\n".join(L) + "\n"


def buy_plan(market: str, cash: float, held_value: float, held: set) -> list:
    """Today's buy candidates sized to the user's money: equal parts, whole board lots."""
    cur, slots = CUR[market], backtest.SLOTS[market]
    part = (cash + held_value) / slots
    free = slots - len(held)
    L = ["", f"## What to buy with your {market.upper()} cash", "",
         f"Cash {cur}{cash:,.0f} plus holdings {cur}{held_value:,.0f}, split into {slots} equal "
         f"parts of {cur}{part:,.0f}. You hold {len(held)}, so {max(free, 0)} parts are free.", ""]
    sc_path = DATA_DIR / market / "scores.csv"
    if free <= 0 or not sc_path.exists():
        return L + ["Nothing to buy: all parts are used, or there are no scores yet (run analyze)."]
    sc = pd.read_csv(sc_path)
    cand = backtest.candidates(sc[sc["liquid"]], backtest.Rules())
    cand = cand[~cand["symbol"].isin(held)]
    costs = backtest.COSTS[market]
    rows, left = [], cash
    for r in cand.itertuples():
        if len(rows) >= free:
            break
        lot = backtest.board_lot(r.close) if market == "ph" else 1
        budget = min(part, left)
        shares = int(budget / (r.close * (1 + costs.commission * (1 + costs.vat) + costs.fees)) / lot) * lot
        if shares <= 0:
            continue   # one board lot costs more than a part
        value = shares * r.close
        cost = value + max(value * costs.commission, costs.min_commission) * (1 + costs.vat) + value * costs.fees
        left -= cost
        rows.append(f"| {r.symbol} | {cur}{r.close:,.2f} | {r.score:.0f} | {shares:,} | {cur}{cost:,.0f} |")
    if not rows:
        return L + ["No buy candidate fits a part today."]
    return L + ["| Stock | Price | Score | Shares | Cost with fees |", "|---|---:|---:|---:|---:|", *rows, "",
                f"Cash left: {cur}{left:,.0f}. Prices are the last close; the next open will differ a little."]


def advise(last, s, sell_below):
    if np.isnan(s):
        return "?", "no score (too little recent trading); check it yourself"
    if s < sell_below:
        why = "score below the hold line: trend and momentum have weakened"
        if last["close"] < last["sma200"]:
            why += "; below its 200-day average"
        return "SELL", why
    if s < sell_below + 10:
        return "HOLD, watch", "close to the hold line; sell if it drops below at the month-end"
    if last["rsi14"] > 80:
        return "HOLD", "strong but very overbought (RSI > 80); a pullback is common"
    return "HOLD", "trend and momentum intact"
