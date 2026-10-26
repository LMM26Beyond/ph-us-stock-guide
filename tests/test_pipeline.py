"""End-to-end run of analyze and portfolio on made-up random-walk prices.

This only checks that the pipeline runs and writes its reports; the prices
are synthetic, so the numbers in the reports mean nothing.
"""
import numpy as np
import pandas as pd
import pytest

from stockguide import backtest, fundamentals, report, storage


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
    for mod in (storage, report, fundamentals, backtest):
        monkeypatch.setattr(mod, "DATA_DIR", tmp_path / "data")
    monkeypatch.setattr(report, "REPORTS_DIR", tmp_path / "reports")
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
    assert "## Verdict" in (data_dir / "reports" / f"backtest_{market}.md").read_text()
    scores = pd.read_csv(data_dir / "data" / market / "scores.csv")
    assert len(scores) == len(syms) and scores["score"].between(0, 100).all()

    pf = data_dir / "portfolio.csv"
    pf.write_text(f"market,ticker,shares,buy_price,buy_date\n{market},S01,100,50,2018-03-01\n{market},NOPE,5,10,\n")
    out = report.portfolio(pf)
    assert "S01" in out and "no price data" in out
