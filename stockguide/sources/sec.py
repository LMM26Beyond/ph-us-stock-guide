"""US company financials from SEC EDGAR (XBRL "company facts").

Free, official, and every value carries the date it was filed, so the
back-test can use only what was public at the time. SEC asks for a
User-Agent with contact details and at most 10 requests a second.
"""
import time

import pandas as pd

from .http import request

TICKERS = "https://www.sec.gov/files/company_tickers.json"
FACTS = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
HEADERS = {"User-Agent": "ph-us-stock-guide research (github.com/LMM26Beyond/ph-us-stock-guide)"}

# Our name -> XBRL concepts to try, first found wins per filing.
CONCEPTS = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet"],
    "net_income": ["NetIncomeLoss", "ProfitLoss"],
    "operating_income": ["OperatingIncomeLoss"],
    "eps": ["EarningsPerShareDiluted", "EarningsPerShareBasic"],
    "equity": ["StockholdersEquity",
               "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
    "assets": ["Assets"],
    "liabilities": ["Liabilities"],
    "debt": ["LongTermDebt", "LongTermDebtNoncurrent"],
    "cash_from_ops": ["NetCashProvidedByUsedInOperatingActivities"],
    "dividends_per_share": ["CommonStockDividendsPerShareDeclared", "CommonStockDividendsPerShareCashPaid"],
    "shares": ["EntityCommonStockSharesOutstanding"],   # dei taxonomy
}


def ciks() -> dict:
    """Ticker -> CIK for every company with SEC filings."""
    data = request("GET", TICKERS, headers=HEADERS).json()
    return {v["ticker"].upper(): int(v["cik_str"]) for v in data.values()}


def facts(cik: int) -> pd.DataFrame:
    """Selected facts for one company as rows: item, concept, start, end, value, form, fp, filed."""
    j = request("GET", FACTS.format(cik=cik), headers=HEADERS).json().get("facts", {})
    rows = []
    for item, names in CONCEPTS.items():
        for name in names:
            node = j.get("us-gaap", {}).get(name) or j.get("dei", {}).get(name)
            if not node:
                continue
            for unit, vals in node.get("units", {}).items():
                for v in vals:
                    if v.get("form") not in ("10-K", "10-Q", "10-K/A", "10-Q/A", "20-F", "40-F", "6-K"):
                        continue
                    rows.append({"item": item, "concept": name, "unit": unit, "start": v.get("start"),
                                 "end": v["end"], "value": v["val"], "form": v["form"],
                                 "fp": v.get("fp"), "filed": v["filed"]})
            break  # first concept that exists for this item
    return pd.DataFrame(rows)


def download(symbols: list[str], pause: float = 0.12) -> pd.DataFrame:
    """Facts for every symbol that files with the SEC (others are skipped)."""
    m = ciks()
    out, missing = [], 0
    for i, sym in enumerate(symbols, 1):
        cik = m.get(sym.upper()) or m.get(sym.upper().replace(".", "-"))
        if cik is None:
            missing += 1
            continue
        try:
            df = facts(cik)
        except Exception as e:  # one company must not stop the run
            print(f"  {sym}: {e}")
            continue
        if not df.empty:
            df.insert(0, "symbol", sym)
            out.append(df)
        if i % 500 == 0:
            print(f"  SEC: {i}/{len(symbols)}")
        time.sleep(pause)
    print(f"SEC: {len(out)} companies with facts, {missing} tickers without a CIK")
    return pd.concat(out, ignore_index=True) if out else pd.DataFrame()
