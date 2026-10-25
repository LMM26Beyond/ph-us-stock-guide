"""Every stock listed on US exchanges, from Nasdaq Trader's symbol directory.

nasdaqlisted.txt covers Nasdaq; otherlisted.txt covers NYSE, NYSE American,
NYSE Arca, Cboe and IEX. Both are refreshed by Nasdaq every trading day.
"""
import io
import re

import pandas as pd

from .http import request

NASDAQ = "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"
OTHER = "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"
EXCHANGES = {"A": "NYSE American", "N": "NYSE", "P": "NYSE Arca", "Z": "Cboe BZX", "V": "IEX"}

# Instruments that are not common shares.
NOT_STOCK = re.compile(
    r"\b(?:warrants?|units?|rights?|preferred|preference|notes? due|debentures?|"
    r"subordinated|% ?(?:series|fixed|senior)|trust preferred|when issued)\b",
    re.I,
)


def _read(url: str) -> pd.DataFrame:
    text = request("GET", url).text
    lines = [l for l in text.splitlines() if l and not l.startswith("File Creation Time")]
    return pd.read_csv(io.StringIO("\n".join(lines)), sep="|", dtype=str, keep_default_na=False)


def fetch(include_etfs: bool = False) -> pd.DataFrame:
    nq = _read(NASDAQ)
    nq = pd.DataFrame({
        "symbol": nq["Symbol"], "name": nq["Security Name"], "exchange": "Nasdaq",
        "etf": nq["ETF"], "test": nq["Test Issue"],
    })
    ot = _read(OTHER)
    ot = pd.DataFrame({
        "symbol": ot["ACT Symbol"], "name": ot["Security Name"],
        "exchange": ot["Exchange"].map(EXCHANGES).fillna(ot["Exchange"]),
        "etf": ot["ETF"], "test": ot["Test Issue"],
    })
    df = pd.concat([nq, ot], ignore_index=True)
    df = df[(df["test"] == "N") & (df["symbol"] != "")]
    df = df[~df["name"].str.contains(NOT_STOCK)]
    df = df[~df["symbol"].str.contains(r"[$^~=]")]
    if not include_etfs:
        df = df[df["etf"] != "Y"]
    # Yahoo writes share classes with a dash: BRK.B -> BRK-B.
    df["yahoo"] = df["symbol"].str.replace(".", "-", regex=False)
    df["type"] = df["etf"].map({"Y": "ETF"}).fillna("Stock")
    return (df.drop_duplicates("symbol")[["symbol", "yahoo", "name", "exchange", "type"]]
              .sort_values("symbol").reset_index(drop=True))
