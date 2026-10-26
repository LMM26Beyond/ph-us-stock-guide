import json

import pandas as pd
import pytest

from stockguide import alerts


def frame(scores: dict) -> pd.DataFrame:
    rows = [dict(symbol=s, score=v, close=10.0, liquid=True, sma200=9.0, sma50=10.0, rsi14=60,
                 value20=1e8, atr14=0.2) for s, v in scores.items()]
    return pd.DataFrame(rows)


@pytest.fixture
def dirs(tmp_path, monkeypatch):
    monkeypatch.setattr(alerts, "DATA_DIR", tmp_path / "data")
    monkeypatch.setattr(alerts, "REPORTS_DIR", tmp_path / "reports")
    (tmp_path / "data").mkdir()
    return tmp_path


def test_first_run_then_changes(dirs):
    day1, day2 = pd.Timestamp("2026-10-21"), pd.Timestamp("2026-10-22")
    first = alerts.run("ph", day1, "Mixed", frame({"A": 80, "B": 75, "C": 72}))
    assert first[0].startswith("Alerts started")
    # B falls below the hold line, C slips under 70 but stays above 60, D joins.
    out = alerts.run("ph", day2, "Downtrend", frame({"A": 80, "B": 55, "C": 65, "D": 90}))
    text = "\n".join(out)
    assert "Mixed → Downtrend" in text
    assert "New on the buy list: D (90)" in text
    assert "below the 60 hold line: B (55)" in text
    assert "still scoring 60+: C (65)" in text
    assert (dirs / "data" / "alerts_ph.md").exists()
    # Same data again: compares with the run before, so the alert repeats rather than vanishing.
    assert alerts.run("ph", day2, "Downtrend", frame({"A": 80, "B": 55, "C": 65, "D": 90})) == out
    # Next day with no change: no alert file.
    assert alerts.run("ph", pd.Timestamp("2026-10-23"), "Downtrend", frame({"A": 80, "B": 55, "C": 65, "D": 90})) == []
    assert not (dirs / "data" / "alerts_ph.md").exists()
    assert json.loads((dirs / "reports" / "alerts_state_ph.json").read_text())["buys"] == ["D", "A"]


def test_month_end():
    assert alerts.is_month_end(pd.Timestamp("2026-10-30"))       # Friday 30 Oct
    assert not alerts.is_month_end(pd.Timestamp("2026-10-29"))
    assert alerts.is_month_end(pd.Timestamp("2026-07-31"))
