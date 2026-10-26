# PH & US stock guide

Daily candles for every Philippine (PSE) and US stock and both markets'
indexes, a study of which candlestick patterns and indicators have actually
worked, and reports that rank stocks to buy or avoid and say whether to hold
or sell what you own.

> This is technical analysis of past prices, not licensed financial advice.
> Signals are probabilities, not certainties.

## What's in it

| Step | Where |
|---|---|
| All PSE stocks: daily candles from PSE Edge, back to about 2009 | `stockguide/sources/pse.py` |
| All US common stocks (Nasdaq, NYSE, NYSE American; ~5,900) from Yahoo Finance, 10 years | `stockguide/sources/us_universe.py`, `yahoo.py` |
| Indexes: PSEi, S&P 500, Nasdaq Composite, Dow, Russell 2000, VIX | `stockguide/fetch.py` |
| How to read candles and indicators | [docs/candlesticks.md](docs/candlesticks.md) |
| Which signals worked, per market | `reports/signals_ph.md`, `reports/signals_us.md` |
| Market direction, buy and avoid lists, score test | `reports/ph.md`, `reports/us.md` |
| Back-test of the buy and sell rules with real costs vs the index | `reports/backtest_ph.md`, `reports/backtest_us.md` |
| Hold or sell advice for your holdings | `reports/portfolio.md` (local only) |

Data notes:

- PSE Edge gives traded value but not share volume, so PH volume is
  estimated as value ÷ close.
- No free source offers PSEi history. Before the first real value recorded by
  the updater, the PSEi is rebuilt from the AETF fund (which tracks the PSEi)
  scaled to index points, back to December 2013.
- Delisted stocks are missing, which flatters long-run results a little.

## Use it

```bash
pip install -r requirements.txt

python -m stockguide update              # download new candles (both markets)
python -m stockguide update --market ph  # one market
python -m stockguide analyze             # study signals, score stocks, back-test, write reports/
python -m stockguide backtest            # only the back-test
python -m stockguide all                 # update, then analyze
```

The first `update` downloads everything (PH takes minutes, US much longer).
After that each run only fetches the missing days. `--max-minutes N` stops a
long download early; run it again to continue.

### Your holdings

Copy `portfolio.example.csv` to `portfolio.csv` and fill it in:

```
market,ticker,shares,buy_price,buy_date
ph,JFC,100,250.00,2025-03-14
us,AAPL,10,190.50,2025-06-02
ph,CASH,50000,,
```

A `CASH` row is money you have ready to invest in that market (put the amount
under `shares`). The report then lists which buy candidates to buy and how many
shares, splitting your money into equal parts (10 for PSE, 40 for US, as in
the back-test) and rounding PSE orders to whole board lots.

Then run `python -m stockguide portfolio`. `portfolio.csv` and
`reports/portfolio.md` are kept out of git, because this repository is public.

## Automatic daily update

`.github/workflows/update.yml` runs every weekday at 22:30 UTC (6:30 am
Manila): it downloads new candles, rebuilds the reports and commits them to
`reports/`. The candles are stored as `data.tar.gz` on the repository's
`data` release, so they are not in git history. You can also start it by
hand from the Actions tab (Daily update → Run workflow).

### Dashboard

The daily update also publishes a web dashboard to GitHub Pages, at
`https://lmm26beyond.github.io/ph-us-stock-guide/`: the market trend with the
index chart, the buy and avoid lists with six-month price lines, the latest
changes, and the back-test against the index. Turn Pages on once under
Settings → Pages → Source: **GitHub Actions**. To see it locally:
`python -m stockguide dashboard`, then `python -m http.server -d site` and open
http://localhost:8000.

### Alerts

After each daily update, changes since the last run are posted as a comment on
the open **Stock alerts** issue (label `alerts`), which GitHub e-mails to the
repository owner: the market trend changing (uptrend, mixed, downtrend), stocks
joining or leaving the buy list, and a reminder on the month's last weekday,
when the tested rules buy and sell. Days without changes post nothing. Close
the issue or unsubscribe from it to stop the e-mails; a new one is opened on
the next change if none is open.

To get the data locally: `gh release download data --pattern data.tar.gz && tar -xzf data.tar.gz`.

## Tests

```bash
python -m pytest
```
