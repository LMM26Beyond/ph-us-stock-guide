"""Data for the web dashboard (site/index.html, published to GitHub Pages).

analyze() writes reports/dashboard_<market>.json; build() copies the page and
the JSON files into site/ for the Pages deploy.
"""
import json
import shutil
from pathlib import Path

import pandas as pd

from . import backtest, storage
from .config import BENCHMARK, REPORTS_DIR, ROOT

PAGE = Path(__file__).with_name("dashboard.html")
SPARK_DAYS = 126   # about six months


def _num(x, digits=4):
    return None if x is None or pd.isna(x) else round(float(x), digits)


def _rows(market: str, df: pd.DataFrame) -> list:
    out = []
    for r in df.itertuples():
        closes = storage.load(market, r.symbol)["close"].tail(SPARK_DAYS)
        out.append({
            "symbol": r.symbol, "name": r.name, "close": _num(r.close), "score": _num(r.score, 0),
            "ret3m": _num(r.ret3m), "ret12m": _num(r.ret12m), "rsi": _num(r.rsi14, 0),
            "pe": _num(1 / r.earnings_yield, 1) if r.earnings_yield and r.earnings_yield > 0 else None,
            "loss": bool(pd.notna(r.earnings_yield) and r.earnings_yield <= 0),
            "roe": _num(r.roe), "div_yield": _num(r.div_yield),
            "min_buy": _num(backtest.board_lot(r.close) * r.close, 0) if market == "ph" else None,
            "spark": [_num(c, 4) for c in closes],
        })
    return out


def _weekly(s: pd.Series) -> pd.Series:
    return s.resample("W-FRI").last().dropna()


def write(market: str, bench: pd.DataFrame, today: pd.DataFrame, regime: tuple, buys: pd.DataFrame,
          avoid: pd.DataFrame, bt: dict, alerts: list) -> None:
    state, advice, breadth = regime
    b = bench.iloc[-1]
    idx = bench[bench.index >= bench.index[-1] - pd.DateOffset(years=3)]
    res = bt["results"]
    rules, index = res["Current rules"][0], res["Hold the index"][0]
    eq = pd.DataFrame({"rules": _weekly(rules / rules.iloc[0]), "index": _weekly(index / index.iloc[0])})
    data = {
        "market": market, "date": f"{bench.index[-1]:%Y-%m-%d}", "index_name": BENCHMARK[market],
        "state": state, "advice": advice, "breadth": _num(breadth),
        "index": {"close": _num(b["close"], 2), "vs50": _num(b["close"] / b["sma50"] - 1),
                  "vs200": _num(b["close"] / b["sma200"] - 1), "ret1m": _num(b["ret1m"]),
                  "ret3m": _num(b["ret3m"]), "ret12m": _num(b["ret12m"])},
        "index_chart": {"dates": [f"{d:%Y-%m-%d}" for d in idx.index],
                        "close": [_num(x, 2) for x in idx["close"]],
                        "sma200": [_num(x, 2) for x in idx["sma200"]]},
        "buys": _rows(market, buys), "avoid": _rows(market, avoid),
        "slots": backtest.SLOTS[market],
        "backtest": {"dates": [f"{d:%Y-%m-%d}" for d in eq.index],
                     "rules": [_num(x) for x in eq["rules"]], "index": [_num(x) for x in eq["index"]],
                     "rules_stats": {k: _num(v) for k, v in backtest.stats(rules).items()},
                     "index_stats": {k: _num(v) for k, v in backtest.stats(index).items()}},
        "alerts": alerts,
    }
    REPORTS_DIR.mkdir(exist_ok=True)
    (REPORTS_DIR / f"dashboard_{market}.json").write_text(json.dumps(data, separators=(",", ":")))


def build(out_dir: Path | None = None) -> Path:
    """Put the page and the latest data together for publishing."""
    out = out_dir or ROOT / "site"
    out.mkdir(parents=True, exist_ok=True)
    shutil.copy(PAGE, out / "index.html")
    for p in REPORTS_DIR.glob("dashboard_*.json"):
        shutil.copy(p, out / p.name)
    return out
