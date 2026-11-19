# Philippines (PSE) — market guide

Data up to **Thu 19 Nov 2026**. Generated 19 Nov 2026.

> This is an automated technical analysis of past prices, not licensed financial advice. Signals are probabilities, not certainties. Check the company news and fundamentals and size every position so a stop-out is affordable.

## The market: Downtrend

Most stocks fall with the market in a downtrend. Expect bigger swings and consider buying smaller amounts.

| | |
|---|---|
| PSEi | 5,465.15 |
| vs 50-day average | -5.0% |
| vs 200-day average | -8.2% |
| 1 month / 3 months / 12 months | -3.6% / -12.0% / -3.9% |
| RSI (14) | 34 |
| Candles (last 3 days) | none |
| Stocks above their 200-day average | 19% |

PSEi before the first recorded real value is rebuilt from the AETF PSEi-tracker ETF, scaled to index points.

## Buy candidates

Liquid stocks with a score of 70 or more, above their 200-day average, not overextended (RSI ≤ 75, at most 30% above the 50-day average) and not too erratic (average daily range at most 5% of the price). Hold while the score stays at 60 or more; sell when it drops below at a month-end. These are the rules tested in [the back-test](backtest_ph.md).

**The market is in a downtrend.** In the back-test, buying anyway did better than waiting (waiting missed the rebounds), but expect bigger swings: consider smaller amounts.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| AC | Ayala Corporation | ₱547.00 | ₱5,470 | 89 | +8% | +19% | 52 | 6.7 | 0.6 | +10% | -22% | 1.7% | bearish marubozu, dark cloud cover |
| PNB | Philippine National Bank | ₱80.90 | ₱809 | 76 | +21% | +54% | 56 | 4.4 | 0.5 | +11% | +15% | 5.5% |  |

**How much to buy.** Split the money you set aside for PSE stocks into 10 equal parts and put one part in each pick, working down the list as you have free parts: with ₱100,000 that is ₱10,000 a stock. Holding fewer stocks made the swings bigger without raising the return in [the back-test](backtest_ph.md). *Min. buy* is the cost of one PSE board lot, the smallest amount you can buy. Run the portfolio command with your cash in portfolio.csv to get share counts.

P/E, P/B, ROE (return on equity), profit growth and dividend yield come from the companies' latest reports (PSE Edge; dividend yield is cash dividends with an ex-date in the last 12 months divided by the price). They are shown for context and are not part of the score yet. A loss or a very high P/E is worth a closer look before buying.

## Avoid

Liquid stocks with the weakest scores: falling trend and lagging the market. If you own one, check it in the portfolio section.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| MRC | MRC Allied, Inc. | ₱0.55 | ₱550 | 8 | -21% | -44% | 18 | – | 0.5 | – | n/m | 0.0% | dragonfly doji, dragonfly doji |
| PLUS | DigiPlus Interactive Corp. | ₱5.35 | ₱535 | 11 | -46% | -78% | 28 | 2.4 | 0.6 | +24% | -12% | 13.8% | bullish harami |
| DITO | DITO CME Holdings Corp. | ₱0.52 | ₱520 | 14 | -31% | -35% | 31 | – | – | – | – | 0.0% |  |
| MER | Manila Electric Company | ₱400.00 | ₱4,000 | 16 | -20% | -28% | 37 | 9.0 | 2.7 | +30% | +11% | 6.9% |  |
| MWC | Manila Water Company, Inc. | ₱27.70 | ₱2,770 | 19 | -24% | -18% | 25 | 5.0 | 0.8 | +16% | -5% | 7.0% |  |
| GSMI | Ginebra San Miguel,  Inc. | ₱208.00 | ₱2,080 | 19 | -10% | -26% | 37 | 6.8 | 2.2 | +32% | +4% | 9.2% |  |
| CNVRG | Converge Information and Communi | ₱8.38 | ₱838 | 20 | -14% | -35% | 33 | 5.7 | 0.9 | +16% | -9% | 5.4% | bearish marubozu |
| ALI | Ayala Land, Inc. | ₱15.00 | ₱1,500 | 21 | -4% | -27% | 44 | 6.2 | 0.6 | +10% | -18% | 4.7% | hammer |
| SCC | Semirara Mining and Power Corpor | ₱9.15 | ₱915 | 21 | -51% | -70% | 24 | 3.1 | 0.7 | +21% | +11% | 0.0% |  |
| MYNLD | Maynilad Water Services, Inc. | ₱16.00 | ₱1,600 | 21 | -15% | – | 35 | 7.6 | 1.1 | +14% | +11% | 6.8% |  |
| BLOOM | Bloomberry Resorts Corporation | ₱1.70 | ₱1,700 | 22 | -29% | -47% | 27 | loss | 0.4 | -8% | -125% | 0.0% |  |
| JGS | JG Summit Holdings, Inc. | ₱17.02 | ₱1,702 | 23 | -24% | -26% | 45 | loss | 0.5 | -32% | -29% | 2.6% | bearish engulfing |
| DMC | DMCI Holdings, Inc. | ₱6.39 | ₱639 | 24 | -20% | -37% | 34 | 4.9 | 0.7 | +14% | +27% | 4.5% |  |
| SHLPH | Shell Pilipinas Corporation | ₱7.20 | ₱720 | 24 | -14% | +16% | 27 | loss | 0.4 | -0% | -171% | 3.9% | hammer |
| WLCON | Wilcon Depot, Inc. | ₱4.90 | ₱4,900 | 24 | -20% | -33% | 27 | loss | loss | – | – | 7.8% | bearish marubozu |
| ACEN | ACEN CORPORATION | ₱2.28 | ₱2,280 | 25 | -23% | -5% | 29 | 18.2 | 0.6 | +3% | +84% | 2.1% | inverted hammer |
| SECB | Security Bank Corporation | ₱61.50 | ₱615 | 25 | -7% | -15% | 43 | 4.0 | 0.3 | +8% | +1% | 4.8% |  |
| GLO | Globe Telecom, Inc. | ₱1,350.00 | ₱6,750 | 25 | -22% | -7% | 18 | 9.4 | 1.2 | +13% | -7% | 6.9% |  |

## Signals that have worked here

From the history study ([full table](signals_ph.md)). Only these count in the score.

- **breakout 52w high** (up): +0.84% vs the index over 10 days, right way 48% of 3,580 times — works as expected
- **bullish marubozu** (up): -0.22% vs the index over 10 days, right way 43% of 8,000 times — works in reverse
- **bullish engulfing** (up): -0.27% vs the index over 10 days, right way 44% of 5,363 times — works in reverse
- **macd cross up** (up): -0.27% vs the index over 10 days, right way 44% of 8,701 times — works in reverse
- **hammer** (up): -0.61% vs the index over 10 days, right way 44% of 4,802 times — works in reverse
- **dragonfly doji** (up): -0.66% vs the index over 10 days, right way 42% of 2,547 times — works in reverse
- **morning star** (up): -1.21% vs the index over 10 days, right way 36% of 457 times — works in reverse
- **three white soldiers** (up): -1.66% vs the index over 10 days, right way 30% of 77 times — works in reverse
- **gravestone doji** (down): +0.71% vs the index over 10 days, right way 52% of 1,410 times — works in reverse
- **bearish marubozu** (down): +0.32% vs the index over 10 days, right way 49% of 9,970 times — works in reverse
- **hanging man** (down): -0.25% vs the index over 10 days, right way 56% of 6,006 times — works as expected

## Has the score worked?

Each past month-end (154 months), liquid stocks were split into five equal groups by score (without the candle part). Average return over the next month beyond the index:

| Score group | 1 (weakest) | 2 | 3 | 4 | 5 (strongest) |
|---|---:|---:|---:|---:|---:|
| Next month vs index | -0.31% | -0.40% | -0.65% | -0.35% | +0.67% |

The strongest group beat the weakest in 56% of months (average gap +0.98% a month).

