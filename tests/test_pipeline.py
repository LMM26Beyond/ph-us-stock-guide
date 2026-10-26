"""End-to-end run of analyze and portfolio on made-up random-walk prices.

This only checks that the pipeline runs and writes its reports; the prices
are synthetic, so the numbers in the reports mean nothing.
"""
import numpy as np
import pandas as pd
import pytest

from stockguide import alerts, backtest, fundamentals, report, storage


def walk(rng, days, start=100.0, drift=0.0003, vol=0.02):
    idx = pd.bdate_range("2016-01-01", periods=days)
    close = start * np.exp(np.cumsum(rng.normal(drift, vol, days)))
    open_ = close * np.exp(rng.normal(0, vol / 2, days))
    high = np.maximum(open_, close) * (1 + rng.uniform(0, vol, days))
    low = np.minimum(open_, close) * (1 - rng.uniform(0, vol, days))
    volume = rng.integers(200_000, 2_000_000, days).astype(float)
    return pd.DataFrame({"open": open_, "high": high, "low": low, "close": close, "volume": volume}, index=idx)


@pytest.fixture
def data_dir(tmp_path, monkeypatch):
    for mod in (storage, report, fundamentals, backtest, alerts):
        monkeypatch.setattr(mod, "DATA_DIR", tmp_path / "data")
    for mod in (report, alerts):
        monkeypatch.setattr(mod, "REPORTS_DIR", tmp_path / "reports")
    return tmp_path


@pytest.mark.parametrize("market,bench", [("ph", "PSEI"), ("us", "SPX")])
def test_analyze_and_portfolio(data_dir, market, bench):
    rng = np.random.default_rng(1)
    days = 252 * 4
    storage.merge_save(market, bench, walk(rng, days, 5000, vol=0.01), "indexes")
    syms = [f"S{i:02d}" for i in range(30)]
    for s in syms:
        storage.merge_save(market, s, walk(rng, days, rng.uniform(5, 200), drift=rng.normal(0, 0.0005)))
    pd.DataFrame({"symbol": syms, "name": [f"Company {s}" for s in syms]}).to_csv(
        data_dir / "data" / market / "universe.csv", index=False)

    report.analyze(market)

    text = (data_dir / "reports" / f"{market}.md").read_text()
    assert "## The market:" in text and "## Has the score worked?" in text
    assert (data_dir / "reports" / f"signals_{market}.md").exists()
    bt_text = (data_dir / "reports" / f"backtest_{market}.md").read_text()
    assert (data_dir / "reports" / f"alerts_state_{market}.json").exists()
    assert "## Verdict" in bt_text and "## Position size" in bt_text
    scores = pd.read_csv(data_dir / "data" / market / "scores.csv")
    assert len(scores) == len(syms) and scores["score"].between(0, 100).all()

    pf = data_dir / "portfolio.csv"
    pf.write_text(f"market,ticker,shares,buy_price,buy_date\n{market},S01,100,50,2018-03-01\n{market},NOPE,5,10,\n"
                  f"{market},CASH,100000,,\n")
    out = report.portfolio(pf)
    assert "S01" in out and "no price data" in out and "CASH" not in out
    assert f"## What to buy with your {market.upper()} cash" in out


def test_buy_plan_board_lots(data_dir):
    (data_dir / "data" / "ph").mkdir(parents=True)
    row = lambda sym, close: dict(symbol=sym, close=close, liquid=True, score=90, rsi14=60, value20=1e8,
                                  sma200=0.9 * close, sma50=close, atr14=0.02 * close)
    pd.DataFrame([row("A", 1.2), row("B", 1200.0), row("C", 30.0)]).to_csv(data_dir / "data" / "ph" / "scores.csv", index=False)
    out = "\n".join(report.buy_plan("ph", 100_000, 0.0, {"C"}))
    # 10 parts of P10,000: A at P1.20 trades in lots of 1,000; B at P1,200 in lots of 5; C is held.
    assert "| A | ₱1.20 | 90 | 8,000 |" in out
    assert "| B | ₱1,200.00 | 90 | 5 |" in out
    assert "| C |" not in out
