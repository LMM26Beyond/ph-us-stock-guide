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
```

Then run `python -m stockguide portfolio`. `portfolio.csv` and
`reports/portfolio.md` are kept out of git, because this repository is public.

## Automatic daily update

`.github/workflows/update.yml` runs every weekday at 22:30 UTC (6:30 am
Manila): it downloads new candles, rebuilds the reports and commits them to
`reports/`. The candles are stored as `data.tar.gz` on the repository's
`data` release, so they are not in git history. You can also start it by
hand from the Actions tab (Daily update → Run workflow).

To get the data locally: `gh release download data --pattern data.tar.gz && tar -xzf data.tar.gz`.

## Tests

```bash
python -m pytest
```
