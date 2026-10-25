import time

import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

_session = None


def session() -> requests.Session:
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers.update(HEADERS)
    return _session


def request(method: str, url: str, tries: int = 4, **kw) -> requests.Response:
    """HTTP with retries and growing waits (2, 4, 8 s) on errors and 429/5xx."""
    kw.setdefault("timeout", 30)
    for i in range(tries):
        try:
            r = session().request(method, url, **kw)
            if r.status_code not in (429, 500, 502, 503, 504):
                r.raise_for_status()
                return r
            err = requests.HTTPError(f"{r.status_code} for {url}")
        except requests.RequestException as e:
            err = e
        if i < tries - 1:
            time.sleep(2 ** (i + 1))
    raise err
