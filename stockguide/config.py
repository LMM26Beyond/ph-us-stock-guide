"""Settings shared by the fetchers and the analysis."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
REPORTS_DIR = ROOT / "reports"

MARKETS = ("ph", "us")

# Market indexes kept alongside the stocks (Yahoo Finance symbols).
INDEXES = {
    "ph": {"PSEI": "PSEI.PS"},
    "us": {"SPX": "^GSPC", "NDX": "^IXIC", "DJI": "^DJI", "RUT": "^RUT", "VIX": "^VIX"},
}
# The index each market's stocks are compared against.
BENCHMARK = {"ph": "PSEI", "us": "SPX"}

# How far back the first download goes.
PH_START = "2000-01-01"
US_START_YEARS = 10

# Stocks trading less than this on average per day (in local currency,
# 20-day average of price x volume) are left out of buy recommendations.
MIN_DAILY_VALUE = {"ph": 5_000_000, "us": 5_000_000}
