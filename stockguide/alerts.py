"""What changed since the last run: market trend, buy list, month-end.

The previous run's state is kept in reports/alerts_state_<market>.json (committed
with the reports). The changes are written to data/alerts_<market>.md, which the
daily workflow posts to the "Stock alerts" GitHub issue.
"""
import json

import pandas as pd

from . import backtest
from .config import DATA_DIR, REPORTS_DIR

LIST_SIZE = 20   # the report's buy list


def buy_list(today: pd.DataFrame) -> list:
    liq = today[today["liquid"]]
    return backtest.candidates(liq, backtest.Rules()).head(LIST_SIZE)["symbol"].tolist()


def is_month_end(day: pd.Timestamp) -> bool:
    """Last weekday of the month (holidays aside)."""
    return (day + pd.offsets.BDay(1)).month != day.month


def changes(market: str, day: pd.Timestamp, state: str, today: pd.DataFrame, prev: dict | None) -> list:
    buys = buy_list(today)
    score = today.set_index("symbol")["score"]
    sell_below = backtest.Rules().sell_below
    fmt = lambda syms: ", ".join(f"{s} ({score.get(s, float('nan')):.0f})" for s in syms)
    L = []
    if prev is None:
        L.append(f"Alerts started. Market: {state}. Buy list: {fmt(buys) or 'empty'}.")
    else:
        if prev.get("regime") != state:
            L.append(f"**Market trend changed: {prev.get('regime')} → {state}.**")
        new = [s for s in buys if s not in prev.get("buys", [])]
        gone = [s for s in prev.get("buys", []) if s not in buys]
        if new:
            L.append(f"New on the buy list: {fmt(new)}.")
        weak = [s for s in gone if pd.isna(score.get(s)) or score.get(s) < sell_below]
        rest = [s for s in gone if s not in weak]
        if weak:
            L.append(f"Off the buy list, score below the {sell_below:.0f} hold line: {fmt(weak)}. "
                     "If you own one, the tested rule sells it at a month-end.")
        if rest:
            L.append(f"Off the buy list but still scoring {sell_below:.0f}+: {fmt(rest)}. "
                     "If you own one, keep holding.")
    if L and is_month_end(day):
        L.append("Today is the month's last weekday: the tested rules buy and sell at the next open.")
    return L


def run(market: str, day: pd.Timestamp, state: str, today: pd.DataFrame) -> list:
    """Compare with the last run, save today's state, and write the alert text if anything changed."""
    path = REPORTS_DIR / f"alerts_state_{market}.json"
    prev = json.loads(path.read_text()) if path.exists() else None
    out = DATA_DIR / f"alerts_{market}.md"
    if prev and prev.get("date") == f"{day:%Y-%m-%d}":
        # Already alerted on this day's data (a re-run): post nothing twice.
        out.unlink(missing_ok=True)
        return []
    L = changes(market, day, state, today, prev)
    REPORTS_DIR.mkdir(exist_ok=True)
    path.write_text(json.dumps({"date": f"{day:%Y-%m-%d}", "regime": state, "buys": buy_list(today)}, indent=1))
    if L:
        label = "PSE" if market == "ph" else "US"
        out.write_text(f"### {label}, data of {day:%a %d %b %Y}\n\n" + "\n".join(f"- {x}" for x in L) + "\n")
    elif out.exists():
        out.unlink()
    return L
