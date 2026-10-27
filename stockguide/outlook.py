"""Candle outlook: what tended to happen after the candle patterns a stock just formed.

For each pattern seen in a stock's last few candles there are two track records
over the next HORIZON trading days:
- the market's: every stock that formed the pattern while the market was in the
  same trend as today (uptrend, downtrend or mixed, from the index's 50- and
  200-day averages). This gives the chance the stock closes higher HORIZON days
  later, compared with the usual chance on any day in that trend. A gap of LEAN
  or more is called "Leans up" or "Leans down"; anything smaller is "No clear edge".
- the stock's own: every earlier time this stock formed the pattern. It is shown
  for reference but does not move the call: blending it in made the calls worse
  on data they were not built from (a single stock has too few cases).

validate() checks the method honestly: track records built only from data up
to SPLIT, judged on what happened after it.
"""
import json

import numpy as np
import pandas as pd

from . import patterns, storage
from .config import DATA_DIR

HORIZON = 10      # trading days, about two weeks
MIN_MARKET = 100  # fewer cases in today's trend: use the market's record in all trends
LEAN = 0.03       # 3 percentage points away from the usual chance
RECENT = 3        # patterns formed in the last 3 candles
CANDLES = 120     # candles shown on the stock page
SPLIT = pd.Timestamp("2022-12-31")
PATTERNS = [k for k, v in patterns.DIRECTION.items() if v]


def trend(bench: pd.DataFrame) -> pd.Series:
    """Market trend on each day, from the index alone (so it can be known for past days)."""
    c, s50, s200 = bench["close"], bench["sma50"], bench["sma200"]
    out = pd.Series("Mixed", index=bench.index)
    out[(c > s200) & (s50 > s200)] = "Uptrend"
    out[(c < s200) & (s50 < s200)] = "Downtrend"
    return out


def records(events: pd.DataFrame, bench: pd.DataFrame) -> pd.DataFrame:
    """Candle-pattern events and the every-5th-day baseline, with the market trend and outcome."""
    ev = events[events["event"].isin([*PATTERNS, "_all_days"])].dropna(subset=["r10"])
    ev = ev[["symbol", "date", "event", "r10"]].copy()
    ev["trend"] = trend(bench).reindex(ev["date"]).to_numpy()
    ev["up"] = ev["r10"] > 0
    return ev.dropna(subset=["trend"])


def tables(ev: pd.DataFrame) -> dict:
    agg = lambda keys: ev.groupby(keys).agg(n=("up", "size"), up=("up", "mean"), avg=("r10", "mean")).reset_index()
    return {"mkt": agg(["event", "trend"]), "mkt_all": agg(["event"]), "stk": agg(["symbol", "event"])}


def chances(q: pd.DataFrame, t: dict) -> pd.DataFrame:
    """q has symbol, event (a pattern) and trend. Adds both track records and the usual chance."""
    q = q[["symbol", "event", "trend"]].reset_index(drop=True)
    m = q.merge(t["mkt"], on=["event", "trend"], how="left")
    a = q.merge(t["mkt_all"], on="event", how="left")
    few = m["n"].fillna(0) < MIN_MARKET
    s = q.merge(t["stk"], on=["symbol", "event"], how="left")
    usual = q[["trend"]].merge(t["mkt"].query("event == '_all_days'"), on="trend", how="left")["up"]
    return q.assign(n_stock=s["n"].fillna(0).astype(int), up_stock=s["up"], avg_stock=s["avg"],
                    n_mkt=m["n"].where(~few, a["n"]).fillna(0).astype(int),
                    chance=m["up"].where(~few, a["up"]), avg=m["avg"].where(~few, a["avg"]),
                    trend_used=np.where(few, "all", q["trend"]), usual=usual)


def call(edge: float) -> str:
    if pd.isna(edge):
        return "No clear edge"
    return "Leans up" if edge >= LEAN else "Leans down" if edge <= -LEAN else "No clear edge"


def validate(ev: pd.DataFrame) -> dict:
    """Records from data up to SPLIT, calls judged on pattern days after it."""
    gap = pd.offsets.BDay(HORIZON + 5)   # outcomes of the training cases end before SPLIT
    t = tables(ev[ev["date"] <= SPLIT - gap])
    test = ev[(ev["date"] > SPLIT) & (ev["event"] != "_all_days")]
    if test.empty:
        return {}
    c = chances(test, t).assign(date=test["date"].to_numpy(), up=test["up"].to_numpy())
    day = c.groupby(["symbol", "date"]).agg(chance=("chance", "mean"), usual=("usual", "first"), up=("up", "first"))
    day["call"] = (day["chance"] - day["usual"]).map(call)
    res = {"from": f"{test['date'].min():%Y-%m-%d}", "to": f"{test['date'].max():%Y-%m-%d}",
           "cases": int(len(day)), "all_up": float(day["up"].mean())}
    for k, name in (("up", "Leans up"), ("down", "Leans down"), ("none", "No clear edge")):
        g = day[day["call"] == name]
        res[k] = {"cases": int(len(g)), "rose": None if g.empty else float(g["up"].mean()),
                  "expected": None if g.empty else float(g["chance"].mean())}
    return res


def _num(x, d=4):
    return None if x is None or pd.isna(x) else round(float(x), d)


def stock_outlook(sym: str, pats: list, state: str, t: dict) -> dict:
    if not pats:
        return {"call": None, "patterns": []}
    c = chances(pd.DataFrame({"symbol": sym, "event": pats, "trend": state}), t)
    chance, usual = c["chance"].mean(), c["usual"].iloc[0]
    return {
        "call": call(chance - usual), "chance": _num(chance), "usual": _num(usual), "avg": _num(c["avg"].mean()),
        "patterns": [{"name": r.event, "dir": patterns.DIRECTION[r.event], "n_stock": r.n_stock,
                      "up_stock": _num(r.up_stock), "avg_stock": _num(r.avg_stock), "n_mkt": r.n_mkt,
                      "trend_used": r.trend_used, "chance": _num(r.chance), "avg": _num(r.avg)}
                     for r in c.itertuples()],
    }


def write(market: str, events: pd.DataFrame, bench: pd.DataFrame, today: pd.DataFrame) -> dict:
    """Per-stock pages (candles, patterns, outlook) and a list of every stock's call, in data/web/."""
    ev = records(events, bench)
    t = tables(ev)
    state = trend(bench).iloc[-1]
    val = validate(ev)
    out = DATA_DIR / "web"
    (out / "stocks" / market).mkdir(parents=True, exist_ok=True)
    # Every PSE stock; US stocks only when liquid (thousands of thinly traded ones otherwise).
    shown = today if market == "ph" else today[today["liquid"]]
    rows = []
    for r in shown.itertuples():
        df = storage.load(market, r.symbol)
        if len(df) < 30:
            continue
        found = patterns.detect(df.tail(CANDLES + 40)).tail(CANDLES)
        found = found[[p for p in PATTERNS if p in found.columns]]
        recent = list(dict.fromkeys(p for _, row in found.tail(RECENT)[::-1].iterrows() for p in row.index[row]))
        o = stock_outlook(r.symbol, recent, state, t)
        tail = df.tail(CANDLES)
        idx, cols = np.nonzero(found.to_numpy())
        page = {
            "symbol": r.symbol, "name": r.name, "market": market, "date": f"{tail.index[-1]:%Y-%m-%d}",
            "trend": state, "horizon": HORIZON, "score": _num(r.score, 0), "liquid": bool(r.liquid),
            "candles": {"d": [f"{d:%Y-%m-%d}" for d in tail.index],
                        **{k[0]: [_num(x, 4) for x in tail[k]] for k in ("open", "high", "low", "close")}},
            "marks": [{"i": int(i), "name": found.columns[j], "dir": patterns.DIRECTION[found.columns[j]]}
                      for i, j in zip(idx, cols)],
            "outlook": o,
        }
        (out / "stocks" / market / f"{r.symbol}.json").write_text(json.dumps(page, separators=(",", ":")))
        rows.append([r.symbol, r.name, _num(r.close), o["call"], o.get("chance"), o.get("usual"),
                     [p["name"] for p in o["patterns"]], bool(r.liquid)])
    summary = {"market": market, "date": f"{bench.index[-1]:%Y-%m-%d}", "trend": state, "horizon": HORIZON,
               "lean": LEAN, "validation": val, "stocks": rows}
    (out / f"outlook_{market}.json").write_text(json.dumps(summary, separators=(",", ":")))
    return summary


def to_markdown(market: str, s: dict) -> str:
    label = {"ph": "Philippine", "us": "US"}[market]
    v = s["validation"]
    rose = lambda x: "–" if x is None else f"{100 * x:.0f}%"
    L = [f"# Candle outlook: {label} stocks", "",
         f"Market trend used: **{s['trend']}** (the index against its 50- and 200-day averages), "
         f"data up to {s['date']}.", "",
         f"For each stock with a candle pattern in its last {RECENT} candles, the chance it closes higher "
         f"{HORIZON} trading days later is what happened after the same pattern on all stocks when the "
         "market was in the same trend, compared with the usual chance on any day in that trend. A gap of "
         f"{100 * LEAN:.0f} points or more is called *Leans up* or *Leans down*. The app also shows each "
         "stock's own record with the pattern, for reference: mixing it into the call made the calls worse "
         "on new data, because one stock has too few cases.", ""]
    if v:
        L += [f"## Did it work on new data?", "",
              f"Track records built from data up to {SPLIT:%b %Y} only, then tested on {v['cases']:,} "
              f"stock-days with a pattern from {v['from']} to {v['to']}. On all of them, the stock was higher "
              f"{HORIZON} days later {rose(v['all_up'])} of the time.", "",
              "| Call | Cases | Expected to rise | Actually rose |", "|---|---:|---:|---:|"]
        for k, name in (("up", "Leans up"), ("down", "Leans down"), ("none", "No clear edge")):
            L.append(f"| {name} | {v[k]['cases']:,} | {rose(v[k]['expected'])} | {rose(v[k]['rose'])} |")
        L.append("")
    counts = pd.Series([r[3] for r in s["stocks"] if r[3]]).value_counts()
    L += ["## Today", "", ", ".join(f"{name}: {counts.get(name, 0)}" for name in
                                    ("Leans up", "Leans down", "No clear edge")) + " stocks.", "",
          "Candle patterns are a weak signal on their own: most of them barely move the odds, and several "
          "work the opposite way from the textbook (see the signals report). Use the outlook as one input "
          "next to the trend score, not as a forecast."]
    return "\n".join(L) + "\n"
