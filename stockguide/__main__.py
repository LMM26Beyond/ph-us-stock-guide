"""Command line: python -m stockguide <command>

  update     download new daily candles (PH, US or both)
  analyze    study the signals, score the stocks, back-test the rules, write reports/
  fundamentals  download company financials (PSE Edge, SEC)
  backtest   only the back-test (reports/backtest_<market>.md)
  portfolio  hold or sell advice for portfolio.csv
  dashboard  put the web dashboard and its data together in site/
  all        update, then analyze
"""
import argparse

from . import backtest, dashboard, fetch, report
from .config import MARKETS, REPORTS_DIR


def main():
    ap = argparse.ArgumentParser(prog="stockguide", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["update", "fundamentals", "analyze", "backtest", "portfolio", "dashboard", "all"])
    ap.add_argument("--market", choices=[*MARKETS, "all"], default="all")
    ap.add_argument("--limit", type=int, help="only the first N symbols (for testing)")
    ap.add_argument("--max-minutes", type=float, help="stop downloading after this long; re-run to continue")
    ap.add_argument("--file", default="portfolio.csv", help="portfolio CSV (default portfolio.csv)")
    a = ap.parse_args()
    markets = MARKETS if a.market == "all" else (a.market,)

    if a.command in ("update", "all"):
        for m in markets:
            (fetch.update_ph if m == "ph" else fetch.update_us)(limit=a.limit, max_minutes=a.max_minutes)
    if a.command == "fundamentals":
        fetch.update_fundamentals(markets, limit=a.limit)
    if a.command in ("analyze", "all"):
        for m in markets:
            report.analyze(m)
    if a.command == "backtest":
        REPORTS_DIR.mkdir(exist_ok=True)
        for m in markets:
            (REPORTS_DIR / f"backtest_{m}.md").write_text(backtest.to_markdown(m, backtest.run(m)))
            print(f"wrote reports/backtest_{m}.md")
    if a.command == "dashboard":
        print(f"wrote {dashboard.build()}")
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
