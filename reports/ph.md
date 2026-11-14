# Philippines (PSE) — market guide

Data up to **Fri 13 Nov 2026**. Generated 14 Nov 2026.

> This is an automated technical analysis of past prices, not licensed financial advice. Signals are probabilities, not certainties. Check the company news and fundamentals and size every position so a stop-out is affordable.

## The market: Downtrend

Most stocks fall with the market in a downtrend. Expect bigger swings and consider buying smaller amounts.

| | |
|---|---|
| PSEi | 5,593.49 |
| vs 50-day average | -3.3% |
| vs 200-day average | -6.2% |
| 1 month / 3 months / 12 months | -2.7% / -10.2% / -2.5% |
| RSI (14) | 41 |
| Candles (last 3 days) | none |
| Stocks above their 200-day average | 25% |

PSEi before the first recorded real value is rebuilt from the AETF PSEi-tracker ETF, scaled to index points.

## Buy candidates

Liquid stocks with a score of 70 or more, above their 200-day average, not overextended (RSI ≤ 75, at most 30% above the 50-day average) and not too erratic (average daily range at most 5% of the price). Hold while the score stays at 60 or more; sell when it drops below at a month-end. These are the rules tested in [the back-test](backtest_ph.md).

**The market is in a downtrend.** In the back-test, buying anyway did better than waiting (waiting missed the rebounds), but expect bigger swings: consider smaller amounts.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| AC | Ayala Corporation | ₱560.00 | ₱5,600 | 84 | +12% | +23% | 62 | 5.5 | 0.6 | +11% | -2% | 1.7% | shooting star |
| WEB | PhilWeb Corporation | ₱12.50 | ₱1,250 | 74 | -9% | +223% | 29 | loss | loss | – | +246% | 0.0% |  |
| MEG | Megaworld Corporation | ₱2.23 | ₱2,230 | 71 | -3% | +12% | 47 | 3.5 | 0.3 | +7% | +2% | 5.1% | inverted hammer |
| PNB | Philippine National Bank | ₱80.05 | ₱800 | 71 | +23% | +54% | 54 | 4.6 | 0.5 | +11% | +17% | 5.4% | hammer |
| PX | Philex Mining Corporation | ₱10.00 | ₱1,000 | 70 | -2% | +25% | 43 | n/m | 1.8 | +1% | -166% | 0.4% | bearish marubozu |

**How much to buy.** Split the money you set aside for PSE stocks into 10 equal parts and put one part in each pick, working down the list as you have free parts: with ₱100,000 that is ₱10,000 a stock. Holding fewer stocks made the swings bigger without raising the return in [the back-test](backtest_ph.md). *Min. buy* is the cost of one PSE board lot, the smallest amount you can buy. Run the portfolio command with your cash in portfolio.csv to get share counts.

P/E, P/B, ROE (return on equity), profit growth and dividend yield come from the companies' latest reports (PSE Edge; dividend yield is cash dividends with an ex-date in the last 12 months divided by the price). They are shown for context and are not part of the score yet. A loss or a very high P/E is worth a closer look before buying.

## Avoid

Liquid stocks with the weakest scores: falling trend and lagging the market. If you own one, check it in the portfolio section.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| PLUS | DigiPlus Interactive Corp. | ₱6.03 | ₱603 | 6 | -38% | -74% | 32 | 2.5 | 0.6 | +24% | -12% | 13.0% | bullish engulfing |
| DITO | DITO CME Holdings Corp. | ₱0.54 | ₱540 | 14 | -27% | -32% | 37 | – | – | – | – | 0.0% |  |
| CNVRG | Converge Information and Communi | ₱9.00 | ₱900 | 17 | -10% | -27% | 46 | 5.8 | 1.0 | +17% | -8% | 5.4% |  |
| GSMI | Ginebra San Miguel,  Inc. | ₱211.00 | ₱2,110 | 18 | -14% | -24% | 42 | 6.8 | 2.2 | +33% | +4% | 8.1% |  |
| MWC | Manila Water Company, Inc. | ₱29.00 | ₱2,900 | 18 | -13% | -17% | 32 | 4.8 | 0.8 | +17% | +6% | 6.8% |  |
| MRC | MRC Allied, Inc. | ₱0.57 | ₱570 | 20 | -20% | -40% | 22 | – | 0.5 | – | n/m | 0.0% | bearish marubozu |
| MER | Manila Electric Company | ₱415.00 | ₱4,150 | 20 | -16% | -28% | 42 | 9.4 | 2.8 | +30% | +11% | 6.4% | bearish marubozu |
| SCC | Semirara Mining and Power Corpor | ₱10.40 | ₱1,040 | 21 | -44% | -67% | 33 | 3.3 | 0.7 | +21% | +11% | 0.0% | shooting star, bearish engulfing |
| DMC | DMCI Holdings, Inc. | ₱6.64 | ₱664 | 23 | -17% | -40% | 40 | 4.7 | 0.7 | +14% | +27% | 4.5% | bearish engulfing, shooting star |
| JGS | JG Summit Holdings, Inc. | ₱17.62 | ₱1,762 | 23 | -21% | -28% | 54 | loss | 0.5 | -32% | -29% | 2.6% |  |
| SMPH | SM Prime Holdings, Inc. | ₱17.22 | ₱1,722 | 24 | -5% | -20% | 50 | 10.4 | 1.1 | +10% | +0% | 2.4% | bullish engulfing |
| ALI | Ayala Land, Inc. | ₱15.06 | ₱1,506 | 25 | +1% | -25% | 45 | 6.1 | 0.7 | +11% | -19% | 4.6% |  |
| GLO | Globe Telecom, Inc. | ₱1,445.00 | ₱7,225 | 25 | -17% | -2% | 29 | 9.9 | 1.2 | +12% | -11% | 6.8% | bullish harami, inverted hammer |
| WLCON | Wilcon Depot, Inc. | ₱5.10 | ₱510 | 25 | -13% | -30% | 36 | loss | loss | – | – | 7.6% | bearish marubozu |

## Signals that have worked here

From the history study ([full table](signals_ph.md)). Only these count in the score.

- **breakout 52w high** (up): +0.84% vs the index over 10 days, right way 48% of 3,576 times — works as expected
- **bullish marubozu** (up): -0.22% vs the index over 10 days, right way 43% of 7,957 times — works in reverse
- **bullish engulfing** (up): -0.27% vs the index over 10 days, right way 44% of 5,345 times — works in reverse
- **macd cross up** (up): -0.28% vs the index over 10 days, right way 44% of 8,663 times — works in reverse
- **hammer** (up): -0.62% vs the index over 10 days, right way 44% of 4,768 times — works in reverse
- **dragonfly doji** (up): -0.68% vs the index over 10 days, right way 42% of 2,500 times — works in reverse
- **morning star** (up): -1.21% vs the index over 10 days, right way 36% of 453 times — works in reverse
- **three white soldiers** (up): -1.65% vs the index over 10 days, right way 30% of 77 times — works in reverse
- **gravestone doji** (down): +0.71% vs the index over 10 days, right way 52% of 1,405 times — works in reverse
- **bearish marubozu** (down): +0.33% vs the index over 10 days, right way 49% of 9,943 times — works in reverse
- **hanging man** (down): -0.24% vs the index over 10 days, right way 56% of 5,981 times — works as expected

## Has the score worked?

Each past month-end (154 months), liquid stocks were split into five equal groups by score (without the candle part). Average return over the next month beyond the index:

| Score group | 1 (weakest) | 2 | 3 | 4 | 5 (strongest) |
|---|---:|---:|---:|---:|---:|
| Next month vs index | -0.32% | -0.40% | -0.68% | -0.30% | +0.66% |

The strongest group beat the weakest in 55% of months (average gap +0.98% a month).

