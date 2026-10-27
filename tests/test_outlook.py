import numpy as np
import pandas as pd

from stockguide import outlook


def bench(days):
    idx = pd.bdate_range("2019-01-01", periods=days)
    close = pd.Series(np.linspace(100, 200, days), index=idx)   # steady rise: an uptrend throughout
    return pd.DataFrame({"close": close, "sma50": close.rolling(50).mean(), "sma200": close.rolling(200).mean()})


def test_calls_follow_the_market_record():
    b = bench(2000)
    dates = b.index[250:]
    rng = np.random.default_rng(0)
    rows = []
    for i, d in enumerate(dates):
        sym = f"S{i % 5}"
        rows.append((sym, d, "_all_days", rng.normal(0, 0.03)))           # rises about half the time
        if i % 2:
            rows.append((sym, d, "hammer", abs(rng.normal(0.01, 0.03))))      # always rises afterwards
        else:
            rows.append((sym, d, "shooting_star", -abs(rng.normal(0.01, 0.03))))
        rows.append((sym, d, "doji", 0.05))                               # not a directional pattern: ignored
    ev = outlook.records(pd.DataFrame(rows, columns=["symbol", "date", "event", "r10"]), b)
    assert set(ev["trend"]) == {"Uptrend"} and "doji" not in set(ev["event"])
    t = outlook.tables(ev)
    o = outlook.stock_outlook("S1", ["hammer"], "Uptrend", t)
    assert o["call"] == "Leans up" and o["chance"] == 1.0 and 0.4 < o["usual"] < 0.6
    assert o["patterns"][0]["n_stock"] > 0 and o["patterns"][0]["trend_used"] == "Uptrend"
    assert outlook.stock_outlook("S1", ["shooting_star"], "Uptrend", t)["call"] == "Leans down"
    # Opposite patterns on the same days cancel out.
    assert outlook.stock_outlook("S1", ["hammer", "shooting_star"], "Uptrend", t)["call"] == "No clear edge"
    # No cases in a downtrend: falls back to the record in every trend.
    assert outlook.stock_outlook("S1", ["hammer"], "Downtrend", t)["patterns"][0]["trend_used"] == "all"
    v = outlook.validate(ev)
    assert v["up"]["rose"] == 1.0 and v["down"]["rose"] == 0.0
