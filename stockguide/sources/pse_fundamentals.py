"""Philippine company financials from PSE Edge company pages.

For now this saves each company's pages as raw HTML under
data/ph/fundamentals/raw/ so the parsers can be written against real pages.
"""
import html
import re
import time
from pathlib import Path

import pandas as pd

from .http import request
from .pse import BASE

PAGES = {
    "stock_data": "/companyPage/stockData.do?cmpy_id={c}&security_id={s}",
    "financials": "/companyPage/financial_reports_view.do?cmpy_id={c}",
    "dividends": "/companyPage/dividends_and_rights_form.do?cmpy_id={c}",
}


def dump(universe, out_dir: Path, pause: float = 0.2) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    ok = failed = 0
    for r in universe.itertuples():
        for name, path in PAGES.items():
            url = BASE + path.format(c=r.cmpy_id, s=r.security_id)
            try:
                text = request("GET", url, tries=2).text
                (out_dir / f"{r.symbol}_{name}.html").write_text(text)
                ok += 1
            except Exception as e:
                (out_dir / f"{r.symbol}_{name}.error").write_text(f"{url}\n{e}")
                failed += 1
            time.sleep(pause)
    print(f"PSE fundamentals: {ok} pages saved, {failed} failed")


UNITS = {"thousand": 1e3, "million": 1e6, "billion": 1e9}


def _num(s: str):
    s = re.sub(r"<[^>]+>|&nbsp;", "", s).strip().replace(",", "")
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()")
    try:
        v = float(s)
    except ValueError:
        return None
    return -v if neg else v


def _section(text: str, name: str) -> dict | None:
    m = re.search(rf"<h3>{name}</h3>(.*?)(?=<h3>|<div id=\"footer\"|$)", text, re.S)
    if not m:
        return None
    body = m.group(1)
    period = re.search(r"(?:fiscal year ended|period ended)\s*:\s*([A-Za-z]{3} \d{1,2}, \d{4})", body)
    if not period:
        return None
    unit = re.search(r"Currency\(and units, if applicable\)\s*:\s*([^<]*)", body)
    unit = html.unescape(unit.group(1)).lower() if unit else ""
    mult = next((v for k, v in UNITS.items() if k in unit), None)
    if mult is None:
        mult = 1e3 if re.search(r"'000|\b000\b|1,000", unit) else 1.0
    rows = {}
    for label, cells in re.findall(r"<tr>\s*<th>([^<]+)</th>((?:\s*<td[^>]*>.*?</td>)+)", body, re.S):
        vals = [_num(c) for c in re.findall(r"<td[^>]*>(.*?)</td>", cells, re.S)]
        rows[html.unescape(label).strip()] = vals
    foreign = bool(re.search(r"us\$|usd|dollar|c\$|csm", unit))
    return {"period": pd.Timestamp(period.group(1)), "mult": mult, "rows": rows, "foreign": foreign}


def parse_financials(text: str) -> dict:
    """Latest annual and quarterly figures from a PSE Edge Financial Reports page, in pesos.

    annual:    {"end", "<item>": (current year, previous year)}
    quarterly: {"end", "<item>": (balance-sheet value,) or (3 months, previous 3 months,
                year to date, previous year to date)}
    """
    out = {}
    for key, name in (("annual", "Annual"), ("quarterly", "Quarterly")):
        sec = _section(text, name)
        if not sec:
            continue
        d = {"end": sec["period"], "foreign": sec["foreign"]}
        for label, vals in sec["rows"].items():
            per_share = "Per Share" in label
            d[label] = tuple(None if v is None else v * (1 if per_share else sec["mult"]) for v in vals)
        out[key] = d
    return out


def parse_stock_data(text: str) -> dict:
    def field(name):
        m = re.search(rf"<th>{re.escape(name)}</th>\s*<td[^>]*>\s*([\d,.]+)\s*</td>", text)
        return float(m.group(1).replace(",", "")) if m else None
    return {"market_cap": field("Market Capitalization"), "shares": field("Outstanding Shares"),
            "price": field("Last Traded Price")}
