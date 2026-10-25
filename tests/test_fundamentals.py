import numpy as np
import pandas as pd
import pytest

from stockguide import fundamentals as f
from stockguide.sources import pse_fundamentals as pf

PAGE = """
<h3>Annual</h3>
<p class="textCont">For the fiscal year ended : Dec 31, 2025<br>
Currency(and units, if applicable) : PHP</p>
<table class="view"><caption>Balance Sheet</caption>
<tr><th>Item</th><th>Current Year</th><th>Previous Year</th></tr>
<tr><th>Total Assets</th><td class="alignR">2,000</td><td class="alignR">1,800</td></tr>
<tr><th>Total Liabilities</th><td class="alignR">1,000</td><td class="alignR">900</td></tr>
<tr><th>Stockholders' Equity - Parent</th><td class="alignR">1,000</td><td class="alignR">900</td></tr>
<tr><th>Book Value Per Share</th><td class="alignR">10.00</td><td class="alignR">9.00</td></tr>
</table>
<table class="view"><caption>Income Statement</caption>
<tr><th>Item</th><th>Current Year</th><th>Previous Year</th></tr>
<tr><th>Net Income/(Loss) Attributable to Parent</th><td class="alignR">100</td><td class="alignR">(20)</td></tr>
<tr><th>Earnings/(Loss) Per Share (Basic)</th><td class="alignR">1.00</td><td class="alignR">(0.20)</td></tr>
</table>
<h3>Quarterly</h3>
<p class="textCont">For the period ended : Jun 30, 2026<br>
Currency(and units, if applicable) : PHP</p>
<table class="view"><caption>Balance Sheet</caption>
<tr><th>Total Assets</th><td>2,100</td><td>2,000</td></tr>
<tr><th>Total Liabilities</th><td>1,050</td><td>1,000</td></tr>
<tr><th>Stockholders' Equity - Parent</th><td>1,050</td><td>1,000</td></tr>
<tr><th>Book Value Per Share</th><td>10.50</td><td>10.00</td></tr>
</table>
<table class="view"><caption>Income Statement</caption>
<tr><th>Net Income/(Loss) Attributable to Parent</th><td>30</td><td>20</td><td>60</td><td>40</td></tr>
</table>
"""


def test_parse_financials_reads_negatives_and_sections():
    d = pf.parse_financials(PAGE)
    assert d["annual"]["end"] == pd.Timestamp("2025-12-31")
    assert d["annual"]["Net Income/(Loss) Attributable to Parent"] == (100, -20)
    assert d["quarterly"]["Net Income/(Loss) Attributable to Parent"] == (30, 20, 60, 40)


def test_scale_fixed_from_book_value_per_share():
    # The page says "PHP" but 100 shares x P10 book value = P1,000,000: figures are in thousands.
    fin = f.check_scale(pf.parse_financials(PAGE), shares=100_000)
    assert fin["annual"]["Stockholders' Equity - Parent"][0] == pytest.approx(1_000_000)


def test_ph_measures():
    fin = f.check_scale(pf.parse_financials(PAGE), shares=100_000)
    m = f.ph_measures(fin, mcap=2_000_000)
    # Trailing 12 months = 100 + 60 - 40 = 120 (thousands).
    assert m["earnings_yield"] == pytest.approx(120_000 / 2_000_000)
    assert m["book_yield"] == pytest.approx(1_050_000 / 2_000_000)
    assert m["growth"] == pytest.approx(0.5)          # year to date 60 vs 40
    assert m["debt_ratio"] == pytest.approx(0.5)


def test_us_attach_uses_only_filed_figures():
    facts = pd.DataFrame([
        # FY2020 net income, filed Feb 2021; FY2021 filed Feb 2022.
        {"item": "net_income", "unit": "USD", "start": "2020-01-01", "end": "2020-12-31", "value": 100, "filed": "2021-02-15"},
        {"item": "net_income", "unit": "USD", "start": "2021-01-01", "end": "2021-12-31", "value": 150, "filed": "2022-02-15"},
        {"item": "equity", "unit": "USD", "start": None, "end": "2020-12-31", "value": 1000, "filed": "2021-02-15"},
        {"item": "shares", "unit": "shares", "start": None, "end": "2021-02-01", "value": 10, "filed": "2021-02-15"},
    ])
    for c in ("start", "end", "filed"):
        facts[c] = pd.to_datetime(facts[c])
    t = f.us_timeline(facts)
    rows = pd.DataFrame({"symbol": "X", "date": pd.to_datetime(["2021-01-29", "2021-06-30", "2022-06-30"]),
                         "close": [20.0, 20.0, 20.0]})
    f_load = f.load_us
    f.load_us = lambda: {"X": t}
    try:
        out = f.attach(rows, "us").sort_values("date")
    finally:
        f.load_us = f_load
    assert np.isnan(out["earnings_yield"].iloc[0])                 # nothing filed yet
    assert out["earnings_yield"].iloc[1] == pytest.approx(100 / 200)
    assert out["earnings_yield"].iloc[2] == pytest.approx(150 / 200)
    assert out["growth"].iloc[2] == pytest.approx(0.5)
