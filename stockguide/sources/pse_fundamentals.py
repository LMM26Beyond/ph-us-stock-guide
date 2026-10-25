"""Philippine company financials from PSE Edge company pages.

For now this saves each company's pages as raw HTML under
data/ph/fundamentals/raw/ so the parsers can be written against real pages.
"""
import time
from pathlib import Path

from .http import request
from .pse import BASE

PAGES = {
    "stock_data": "/companyPage/stockData.do?cmpy_id={c}&security_id={s}",
    "financials": "/companyPage/financial_reports_view.do?cmpy_id={c}",
    "dividends": "/companyPage/dividends_n_rights_view.do?cmpy_id={c}",
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
