"""Would following the buy and sell rules have made money, after costs?

Replays the report's rules on history, one month-end at a time:

- On each month-end, score every stock with the data known that day (the
  candle part is left out: its verdicts come from the whole history).
- Sell holdings whose score fell below Rules.sell_below. Fill empty slots
  with the report's buy candidates, best score first, at the next day's open.
- Optionally (the old rules): sell at the next open when a close falls below
  a trailing stop, and buy nothing new in a market downtrend.

Positions are equal-weight, shares are rounded down to whole PSE board lots,
and every trade pays commission, fees and taxes (and a slippage allowance).
The result is compared with simply holding the market index, both over the
period the rules were tuned on and over the later years kept aside to check
them.
"""
from dataclasses import dataclass, replace

import numpy as np
import pandas as pd

from . import analysis, fundamentals, score, storage
from .config import BENCHMARK, DATA_DIR

SLOTS = {"ph": 10, "us": 40}
# The rules were chosen on data up to this date; later years test them.
TUNED_UNTIL = pd.Timestamp("2022-12-31")
CAPITAL = {"ph": 1_000_000, "us": 20_000}


@dataclass(frozen=True)
class Costs:
    commission: float      # share of trade value
    min_commission: float  # per trade, in local currency
    vat: float             # tax on the commission
    fees: float            # exchange and clearing fees, both sides
    sell_tax: float        # tax on sales only
    slippage: float        # spread and price impact allowance, both sides

    def buy(self, value: float) -> float:
        com = max(value * self.commission, self.min_commission) if value else 0.0
        return com * (1 + self.vat) + value * (self.fees + self.slippage)

    def sell(self, value: float) -> float:
        return self.buy(value) + value * self.sell_tax


# PSE: 0.25% broker commission (min P20) plus 12% VAT, PSE fee 0.005%,
# SCCP fee 0.01%, and 0.6% stock transaction tax on sales.
# US: no commission at most brokers; SEC/FINRA fees are tiny.
COSTS = {
    "ph": Costs(0.0025, 20.0, 0.12, 0.00015, 0.006, 0.002),
    "us": Costs(0.0, 0.0, 0.0, 0.00003, 0.0, 0.0005),
}


def board_lot(price: float) -> int:
    """PSE minimum trading unit for a share price."""
    for limit, lot in ((0.01, 1_000_000), (0.05, 100_000), (0.5, 10_000),
                       (5, 1_000), (50, 100), (1000, 10)):
        if price < limit:
            return lot
    return 5


@dataclass(frozen=True)
class Rules:
    """The report's rules. Defaults are the tuned ones (see TUNED_UNTIL)."""
    regime_filter: bool = False
    stops: bool = False
    slots: int = 10
    min_score: float = 70
    sell_below: float = 60
    atr_mult: float = 3.0
    min_value: float = 0.0     # extra liquidity floor (20-day traded value)
    min_price: float = 0.0
    max_atr_pct: float = 0.05  # skip stocks whose daily range (ATR / close) is above this
    # Fundamentals filters (US only: PSE Edge has no history). None = not used; a stock
    # without the figure is skipped when a filter is on.
    profitable: bool = False   # positive trailing net income
    min_roe: float | None = None
    min_growth: float | None = None
    max_pe: float | None = None


def monthly_scores(snaps: pd.DataFrame, bench: pd.DataFrame) -> pd.DataFrame:
    """Score every stock on every month-end, using only that day's data."""
    s = snaps[snaps["sma200"].notna() & snaps["mom12_1"].notna()]
    s = s[s.groupby([s["symbol"], s["date"].dt.to_period("M")])["date"].transform("max") == s["date"]]
    # Stocks trade on slightly different last days; line them up on the month.
    s = s.assign(month=s["date"].dt.to_period("M")).reset_index(drop=True)
    s["date"] = s.groupby("month")["date"].transform("max")
    comp = score.components(s, bench["ret6m"])
    s["score"] = score.total(comp, with_candles=False)
    return s


def regimes(scores: pd.DataFrame, bench: pd.DataFrame) -> pd.Series:
    """Market state on each month-end, as in the report."""
    out = {}
    for d, g in scores.groupby("date"):
        b = bench[bench.index <= d]
        if b.empty or pd.isna(b["sma200"].iloc[-1]):
            out[d] = "Mixed"
            continue
        b = b.iloc[-1]
        liq = g[g["liquid"]]
        breadth = (liq["close"] > liq["sma200"]).mean() if len(liq) else np.nan
        if b["close"] > b["sma200"] and b["sma50"] > b["sma200"] and breadth >= 0.5:
            out[d] = "Uptrend"
        elif b["close"] < b["sma200"] and b["sma50"] < b["sma200"] and (np.isnan(breadth) or breadth < 0.5):
            out[d] = "Downtrend"
        else:
            out[d] = "Mixed"
    return pd.Series(out)


def panels(market: str, symbols) -> dict:
    """Wide daily frames (date x symbol) of open, close and ATR."""
    from .indicators import atr
    o, c, a = {}, {}, {}
    for sym in symbols:
        df = storage.load(market, sym)
        o[sym], c[sym], a[sym] = df["open"], df["close"], atr(df)
    return {"open": pd.DataFrame(o), "close": pd.DataFrame(c), "atr": pd.DataFrame(a)}


def candidates(g: pd.DataFrame, rules: Rules) -> pd.DataFrame:
    """The report's buy-candidate filter on one month-end's scores."""
    return g[g["liquid"] & (g["score"] >= rules.min_score) & (g["close"] > g["sma200"])
             & (g["rsi14"] <= 75) & (g["close"] <= 1.3 * g["sma50"])
             & (g["value20"] >= rules.min_value) & (g["close"] >= rules.min_price)
             & (g["atr14"] <= rules.max_atr_pct * g["close"]) & _fundamentals_ok(g, rules)
             ].sort_values("score", ascending=False)


def _fundamentals_ok(g: pd.DataFrame, rules: Rules) -> pd.Series:
    ok = pd.Series(True, index=g.index)
    col = lambda c: g[c] if c in g else pd.Series(np.nan, index=g.index)
    if rules.profitable:
        ok &= col("earnings_yield") > 0
    if rules.min_roe is not None:
        ok &= col("roe") >= rules.min_roe
    if rules.min_growth is not None:
        ok &= col("growth") >= rules.min_growth
    if rules.max_pe is not None:
        ok &= col("earnings_yield") >= 1 / rules.max_pe
    return ok


def simulate(market: str, scores: pd.DataFrame, regime: pd.Series, px: dict,
             rules: Rules, capital: float, start=None) -> tuple[pd.Series, pd.DataFrame]:
    costs = COSTS[market]
    lots = market == "ph"
    opens, closes, atrs = px["open"], px["close"], px["atr"]
    days = closes.index
    month_ends = sorted(scores["date"].unique())
    if start is not None:
        month_ends = [d for d in month_ends if d >= start]
        days = days[days >= month_ends[0]] if month_ends else days[:0]
    by_date = {d: g.set_index("symbol") for d, g in scores.groupby("date")}
    last_close = closes.ffill()

    cash = capital
    pos = {}       # symbol -> {"shares", "entry", "cost", "date", "peak"}
    pending_sell, pending_buy = {}, []   # executed at the next open
    trades, equity = [], {}
    me_set = set(month_ends)

    for day in days:
        # 1. Orders from yesterday fill at today's open (if the stock trades today).
        for sym, why in list(pending_sell.items()):
            p = opens.at[day, sym] if sym in opens else np.nan
            if pd.isna(p):
                continue
            q = pos.pop(sym)
            value = q["shares"] * p
            fee = costs.sell(value)
            cash += value - fee
            trades.append({"symbol": sym, "bought": q["date"], "sold": day, "why": why,
                           "return": (value - fee) / q["cost"] - 1})
            del pending_sell[sym]
        if pending_buy:
            held_value = sum(q["shares"] * last_close.at[day, s] for s, q in pos.items()
                             if not pd.isna(last_close.at[day, s]))
            target = (cash + held_value) / rules.slots
            for sym in pending_buy:
                p = opens.at[day, sym] if sym in opens else np.nan
                if pd.isna(p) or sym in pos or len(pos) >= rules.slots:
                    continue
                budget = min(target, cash)
                lot = board_lot(p) if lots else 1
                shares = int(budget / (p * (1 + costs.commission * (1 + costs.vat) + costs.fees + costs.slippage)) / lot) * lot
                if shares <= 0:
                    continue
                value = shares * p
                fee = costs.buy(value)
                if value + fee > cash:
                    continue
                cash -= value + fee
                pos[sym] = {"shares": shares, "cost": value + fee, "date": day, "peak": p}
            pending_buy = []

        # 2. End of day: trailing stops.
        for sym, q in pos.items():
            c = closes.at[day, sym]
            if pd.isna(c):
                continue
            q["peak"] = max(q["peak"], c)
            a = atrs.at[day, sym]
            if rules.stops and not pd.isna(a) and c < q["peak"] - rules.atr_mult * a:
                pending_sell.setdefault(sym, "stop")

        # 3. Month-end: score-based sells and new buys.
        if day in me_set and day in by_date:
            g = by_date[day]
            for sym in pos:
                sc = g["score"].get(sym, np.nan)
                if sym not in pending_sell and (pd.isna(sc) or sc < rules.sell_below):
                    pending_sell[sym] = "score"
            if not (rules.regime_filter and regime.get(day) == "Downtrend"):
                free = rules.slots - (len(pos) - len(pending_sell))
                if free > 0:
                    cand = candidates(g.reset_index(), rules)
                    cand = cand[~cand["symbol"].isin(pos)]
                    pending_buy = cand["symbol"].head(free).tolist()

        equity[day] = cash + sum(q["shares"] * last_close.at[day, s] for s, q in pos.items()
                                 if not pd.isna(last_close.at[day, s]))
    return pd.Series(equity, dtype=float), pd.DataFrame(trades)


def stats(eq: pd.Series, trades: pd.DataFrame | None = None) -> dict:
    eq = eq.dropna()
    if len(eq) < 2:
        return {}
    years = (eq.index[-1] - eq.index[0]).days / 365.25
    r = eq.pct_change().dropna()
    out = {
        "cagr": (eq.iloc[-1] / eq.iloc[0]) ** (1 / years) - 1,
        "total": eq.iloc[-1] / eq.iloc[0] - 1,
        "max_dd": (eq / eq.cummax() - 1).min(),
        "vol": r.std() * np.sqrt(252),
        "sharpe": r.mean() / r.std() * np.sqrt(252) if r.std() > 0 else np.nan,
    }
    if trades is not None and len(trades):
        out |= {"trades": len(trades), "win_rate": (trades["return"] > 0).mean(),
                "avg_trade": trades["return"].mean(),
                "stops_share": (trades["why"] == "stop").mean()}
    return out


VARIANTS = {
    "Current rules": {},
    "Old rules (3 × ATR trailing stop, no buys in a downtrend, sell below 50, no range limit)":
        {"stops": True, "regime_filter": True, "sell_below": 50, "max_atr_pct": 1.0},
}
# Tried in the US only, where SEC filings give the figures known on each past date.
FUNDAMENTAL_VARIANTS = {
    "Current rules + only profitable companies": {"profitable": True},
    "Current rules + only ROE of 15% or more": {"min_roe": 0.15},
    "Current rules + only P/E of 25 or less": {"max_pe": 25},
}


def run(market: str, events_snaps=None) -> dict:
    """Back-test the current rules and the old ones against the index."""
    _, snaps = events_snaps or analysis.run(market, progress=False)
    bench = analysis.benchmark(market)
    scores = monthly_scores(snaps, bench)
    variants = dict(VARIANTS)
    if market == "us" and (DATA_DIR / "us" / "fundamentals.csv.gz").exists():
        scores = fundamentals.attach(scores, "us")
        variants |= FUNDAMENTAL_VARIANTS
    regime = regimes(scores, bench)
    held = scores.loc[scores["liquid"], "symbol"].unique()
    px = panels(market, held)
    start = max(scores["date"].min(), bench["sma200"].first_valid_index())
    cap = CAPITAL[market]
    results = {}
    for name, kw in variants.items():
        rules = replace(Rules(slots=SLOTS[market]), **kw)
        eq, tr = simulate(market, scores, regime, px, rules, cap, start)
        results[name] = (eq, tr)
    eq0 = results["Current rules"][0]
    b = bench["close"].reindex(eq0.index).ffill()
    results["Hold the index"] = (cap * b / b.iloc[0], None)
    return {"results": results, "regime": regime}


def to_markdown(market: str, out: dict) -> str:
    from .report import LABEL, INDEX_NAME
    res = out["results"]
    rules = Rules(slots=SLOTS[market])
    eq0 = res["Current rules"][0]
    bench_eq = res["Hold the index"][0]
    bname = INDEX_NAME.get(BENCHMARK[market], BENCHMARK[market])
    cur = "₱" if market == "ph" else "$"
    pct = lambda x: "–" if x is None or pd.isna(x) else f"{100 * x:+.1f}%"
    L = [f"# Back-test: {LABEL[market]}", "",
         f"{eq0.index[0]:%b %Y} to {eq0.index[-1]:%b %Y}, starting with {cur}{CAPITAL[market]:,} "
         f"and up to {rules.slots} stocks.", "",
         "**Current rules.** Each month-end the stocks are scored with only the data known "
         f"that day. Holdings scoring below {rules.sell_below:.0f} are sold. Free slots are "
         f"filled with the report's buy candidates (score {rules.min_score:.0f}+, above the "
         "200-day average, RSI ≤ 75, at most 30% above the 50-day average, average daily "
         f"range at most {100 * rules.max_atr_pct:.0f}% of the price) at the next day's open, "
         "in equal amounts.", "",
         "Costs per trade: " + (
             "0.25% commission (min ₱20) + 12% VAT, 0.015% PSE and SCCP fees, 0.6% sales tax "
             "on sells, and 0.2% slippage each way, about 1.3% for a round trip. Shares are "
             "bought in whole board lots."
             if market == "ph" else
             "no commission, 0.003% regulatory fees and 0.05% slippage each way."), "",
         "| Strategy | Yearly return | Total | Worst drop | Sharpe | Trades | Wins | Avg trade |",
         "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for name, (eq, tr) in res.items():
        s = stats(eq, tr)
        wins = f"{100 * s['win_rate']:.0f}%" if "win_rate" in s else "–"
        L.append(f"| {name} | {pct(s.get('cagr'))} | {pct(s.get('total'))} | {pct(s.get('max_dd'))} | "
                 f"{s.get('sharpe', np.nan):.2f} | {s.get('trades', '–')} | {wins} | {pct(s.get('avg_trade'))} |")
    L += ["", f"\"Hold the index\" is the {bname} with no costs and no dividends; the stock "
          "prices also exclude dividends, so the comparison is like for like.", ""]

    # Tuned period versus the years kept aside.
    L += ["## Tuned period and test period", "",
          f"The rule settings were the best of those tried on data up to {TUNED_UNTIL:%b %Y}, "
          "and the same settings came out on top in both markets. The later years were not "
          "used to pick them, so they are a fairer test, though not a perfectly blind one.", "",
          f"| Period | Current rules | {bname} |", "|---|---:|---:|"]
    for label, sel in ((f"To {TUNED_UNTIL:%b %Y} (tuned)", eq0.index <= TUNED_UNTIL),
                       (f"From {TUNED_UNTIL + pd.Timedelta(days=1):%b %Y} (test)", eq0.index > TUNED_UNTIL)):
        a, b = stats(eq0[sel]).get("cagr"), stats(bench_eq[sel]).get("cagr")
        L.append(f"| {label} | {pct(a)} a year | {pct(b)} a year |")

    fund = [n for n in res if n in FUNDAMENTAL_VARIANTS]
    if fund:
        L += ["", "## Fundamentals filters", "",
              "The same rules, but buying only companies that pass a test on their latest SEC "
              "filings as of each month-end (a company without the figure is skipped).", "",
              "| Strategy | Tuned period | Test period |", "|---|---:|---:|"]
        period = {}
        for name in ["Current rules", *fund]:
            eq = res[name][0]
            period[name] = (stats(eq[eq.index <= TUNED_UNTIL]).get("cagr", np.nan),
                            stats(eq[eq.index > TUNED_UNTIL]).get("cagr", np.nan))
            L.append(f"| {name} | {pct(period[name][0])} a year | {pct(period[name][1])} a year |")
        base = period["Current rules"]
        better = [n for n in fund if period[n][0] > base[0] and period[n][1] > base[1]]
        if better:
            L += ["", "Beat the current rules in both periods: " + ", ".join(better) + ". "
                  "Worth considering as an extra check before buying."]
        else:
            L += ["", "No filter beat the current rules in both periods. Strong momentum stocks are "
                  "often young or fast-growing companies with losses or high P/Es, and the filters "
                  "screen out exactly those. So the report shows P/E, P/B, ROE and growth as "
                  "context only."]

    L += ["", "## Year by year", "", f"| Year | Current rules | {bname} | Difference |", "|---|---:|---:|---:|"]
    for y in sorted(set(eq0.index.year)):
        ra, rb = _year(eq0, y), _year(bench_eq, y)
        L.append(f"| {y} | {pct(ra)} | {pct(rb)} | {pct(ra - rb)} |")

    s_rules, s_idx = stats(eq0, res["Current rules"][1]), stats(bench_eq)
    gap = s_rules.get("cagr", 0) - s_idx.get("cagr", 0)
    if gap > 0.01:
        call = "The rules beat the index."
    elif gap > -0.01:
        call = "The rules did about as well as the index; an index fund is simpler."
    else:
        call = "The rules did **not** beat the index; until they do, an index fund is the better default."
    L += ["", "## Verdict", "",
          f"Following the current rules returned {pct(s_rules['cagr'])} a year against "
          f"{pct(s_idx['cagr'])} for the {bname}, after costs. {call} The worst drop along the "
          f"way was {pct(s_rules['max_dd'])}, so expect deep falls and size your money "
          "accordingly.", "",
          "What the tuning found: tight trailing stops (3 × ATR) sold good stocks on normal dips "
          "and were the biggest drag; sitting out market downtrends missed the rebounds; and "
          "the most erratic stocks (daily range above 5% of the price) hurt more than they helped.", "",
          "Limits: delisted stocks are missing (which flatters the rules, more so in the US), "
          "dividends are ignored on both sides, and a past result does not promise a future one."]
    return "\n".join(L) + "\n"


def _year(eq: pd.Series, y: int) -> float:
    prev, cur = eq[eq.index.year < y], eq[eq.index.year == y]
    start = prev.iloc[-1] if len(prev) else cur.iloc[0]
    return cur.iloc[-1] / start - 1
