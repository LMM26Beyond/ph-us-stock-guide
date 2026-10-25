"""Command line: python -m stockguide <command>

  update     download new daily candles (PH, US or both)
  analyze    study the signals, score the stocks, write reports/
  portfolio  hold or sell advice for portfolio.csv
  all        update, then analyze
"""
import argparse

from . import fetch, report
from .config import MARKETS, REPORTS_DIR


def main():
    ap = argparse.ArgumentParser(prog="stockguide", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["update", "analyze", "portfolio", "all"])
    ap.add_argument("--market", choices=[*MARKETS, "all"], default="all")
    ap.add_argument("--limit", type=int, help="only the first N symbols (for testing)")
    ap.add_argument("--max-minutes", type=float, help="stop downloading after this long; re-run to continue")
    ap.add_argument("--file", default="portfolio.csv", help="portfolio CSV (default portfolio.csv)")
    a = ap.parse_args()
    markets = MARKETS if a.market == "all" else (a.market,)

    if a.command in ("update", "all"):
        for m in markets:
            (fetch.update_ph if m == "ph" else fetch.update_us)(limit=a.limit, max_minutes=a.max_minutes)
    if a.command in ("analyze", "all"):
        for m in markets:
            report.analyze(m)
    if a.command in ("portfolio", "analyze", "all"):
        text = report.portfolio(a.file)
        if text:
            REPORTS_DIR.mkdir(exist_ok=True)
            (REPORTS_DIR / "portfolio.md").write_text(text)
            print(text)
        elif a.command == "portfolio":
            print(f"{a.file} not found. Copy portfolio.example.csv to portfolio.csv and fill it in.")


if __name__ == "__main__":
    main()
