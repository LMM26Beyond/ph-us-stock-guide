"""Philippine Stock Exchange data from PSE Edge (edge.pse.com.ph).

- Company directory: every listed company with its main (common) security.
- Price history: daily open/high/low/close and traded value (pesos).
  PSE Edge gives no share volume, so volume is estimated as value / close.
- Index page: today's PSEi and sector index values.
"""
import html
import re
from datetime import date

import pandas as pd

from .http import request

BASE = "https://edge.pse.com.ph"
ROW = re.compile(
    r"cmDetail\('(\d+)','(\d+)'\);return false;\">([^<]*)</a></td>\s*"
    r"<td[^>]*><a[^>]*>([^<]*)</a></td>\s*<td>([^<]*)</td>\s*<td>([^<]*)</td>\s*"
    r"<td[^>]*>([^<]*)</td>",
)


def directory() -> pd.DataFrame:
    """All listed companies: symbol, name, sector, subsector, listed, cmpy_id, security_id."""
    rows, page = [], 1
    while True:
        r = request("POST", f"{BASE}/companyDirectory/search.ax", data={
            "pageNo": page, "companyId": "", "keyword": "", "sortType": "",
            "dateSortType": "DESC", "cmpyNameSortType": "ASC", "symbolSortType": "ASC",
            "sector": "ALL", "subsector": "ALL",
        })
        found = ROW.findall(r.text)
        rows += found
        pages = [int(p) for p in re.findall(r"goPage\((\d+)\)", r.text)]
        if not found or page >= max(pages, default=page):
            break
        page += 1
    df = pd.DataFrame(rows, columns=["cmpy_id", "security_id", "name", "symbol",
                                     "sector", "subsector", "listed"])
    for c in ("name", "symbol", "sector", "subsector", "listed"):
        df[c] = df[c].map(lambda s: html.unescape(s).strip())
    return df.drop_duplicates("symbol").sort_values("symbol").reset_index(drop=True)


def history(cmpy_id: str, security_id: str, start: str = "2000-01-01", end: str | None = None) -> pd.DataFrame:
    end = end or date.today().isoformat()
    fmt = lambda d: pd.Timestamp(d).strftime("%m-%d-%Y")
    r = request("POST", f"{BASE}/common/DisclosureCht.ax", json={
        "cmpy_id": str(cmpy_id), "security_id": str(security_id),
        "startDate": fmt(start), "endDate": fmt(end),
    }, headers={"Referer": f"{BASE}/companyPage/stockData.do?cmpy_id={cmpy_id}"})
    data = r.json().get("chartData") or []
    if not data:
        return pd.DataFrame()
    df = pd.DataFrame(data)
    df.index = pd.to_datetime(df["CHART_DATE"], format="%b %d, %Y %H:%M:%S")
    out = pd.DataFrame({
        "open": df["OPEN"], "high": df["HIGH"], "low": df["LOW"], "close": df["CLOSE"],
    }, index=df.index).astype(float)
    out["volume"] = (df["VALUE"].astype(float) / out["close"]).round()
    return out


def index_snapshot() -> pd.DataFrame:
    """Today's index values from the PSE Edge index page (name, value, change, pct)."""
    text = request("GET", f"{BASE}/index/form.do").text
    rows = re.findall(
        r'<td class="label">([^<]+)</td>\s*<td class="alignR">([\d,.]+)</td>\s*'
        r'<td class="alignR" style="color:(\w+)">\s*([\d,.]+)</td>', text)
    out = []
    for name, value, color, chg in rows:
        sign = -1 if color == "red" else 1
        out.append({"index": name.strip(), "value": float(value.replace(",", "")),
                    "change": sign * float(chg.replace(",", ""))})
    return pd.DataFrame(out)
