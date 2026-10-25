import pandas as pd
import pytest

from stockguide import backtest as b


@pytest.mark.parametrize("price,lot", [(0.005, 1_000_000), (0.03, 100_000), (0.2, 10_000),
                                       (2.5, 1_000), (24.65, 100), (143.5, 10), (852.0, 10), (1200.0, 5)])
def test_board_lot(price, lot):
    assert b.board_lot(price) == lot


def test_ph_costs():
    c = b.COSTS["ph"]
    # P100,000 buy: 0.25% commission + 12% VAT = 280, fees 15, slippage 200.
    assert c.buy(100_000) == pytest.approx(280 + 15 + 200)
    # Sells add the 0.6% stock transaction tax.
    assert c.sell(100_000) == pytest.approx(280 + 15 + 200 + 600)
    # Minimum commission of P20 applies to small trades.
    assert c.buy(1_000) == pytest.approx(20 * 1.12 + 1_000 * (0.00015 + 0.002))


def test_simulate_buys_in_lots_and_sells_on_score():
    days = pd.bdate_range("2020-01-01", periods=60)
    px = {k: pd.DataFrame({"AAA": 10.0, "BBB": 20.0}, index=days) for k in ("open", "close", "atr")}
    me1, me2 = days[10], days[40]
    row = dict(liquid=True, sma200=5.0, sma50=9.5, rsi14=55.0, value20=1e8, atr14=0.2)
    scores = pd.DataFrame([
        {"date": me1, "symbol": "AAA", "score": 80, "close": 10.0, **row},
        {"date": me1, "symbol": "BBB", "score": 75, "close": 20.0, **row},
        {"date": me2, "symbol": "AAA", "score": 40, "close": 10.0, **row},   # drops below 60: sell
        {"date": me2, "symbol": "BBB", "score": 75, "close": 20.0, **row},
    ])
    regime = pd.Series({me1: "Downtrend", me2: "Downtrend"})
    eq, trades = b.simulate("ph", scores, regime, px, b.Rules(slots=2), 100_000, me1)
    assert list(trades["symbol"]) == ["AAA"] and trades["why"].iloc[0] == "score"
    # Flat prices: the only change in equity is trading costs.
    assert 97_000 < eq.iloc[-1] < 100_000
