# Philippines (PSE) — market guide

Data up to **Mon 09 Nov 2026**. Generated 09 Nov 2026.

> This is an automated technical analysis of past prices, not licensed financial advice. Signals are probabilities, not certainties. Check the company news and fundamentals and size every position so a stop-out is affordable.

## The market: Downtrend

Most stocks fall with the market in a downtrend. Expect bigger swings and consider buying smaller amounts.

| | |
|---|---|
| PSEi | 5,677.92 |
| vs 50-day average | -2.1% |
| vs 200-day average | -4.9% |
| 1 month / 3 months / 12 months | -0.4% / -8.0% / -1.9% |
| RSI (14) | 46 |
| Candles (last 3 days) | bullish marubozu, bullish marubozu |
| Stocks above their 200-day average | 24% |

PSEi before the first recorded real value is rebuilt from the AETF PSEi-tracker ETF, scaled to index points.

## Buy candidates

Liquid stocks with a score of 70 or more, above their 200-day average, not overextended (RSI ≤ 75, at most 30% above the 50-day average) and not too erratic (average daily range at most 5% of the price). Hold while the score stays at 60 or more; sell when it drops below at a month-end. These are the rules tested in [the back-test](backtest_ph.md).

**The market is in a downtrend.** In the back-test, buying anyway did better than waiting (waiting missed the rebounds), but expect bigger swings: consider smaller amounts.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| PNB | Philippine National Bank | ₱78.00 | ₱780 | 91 | +25% | +51% | 49 | 4.6 | 0.5 | +11% | +17% | 5.4% | bearish marubozu |
| MEG | Megaworld Corporation | ₱2.29 | ₱2,290 | 81 | +4% | +16% | 56 | 3.5 | 0.3 | +7% | +2% | 5.1% |  |
| APX | Apex Mining Co., Inc. | ₱17.44 | ₱1,744 | 79 | +18% | +92% | 57 | 10.7 | 3.7 | +35% | +68% | 3.7% | bullish marubozu, hanging man |
| WEB | PhilWeb Corporation | ₱12.68 | ₱1,268 | 73 | -4% | +195% | 21 | loss | loss | – | +246% | 0.0% | inverted hammer |
| AC | Ayala Corporation | ₱549.50 | ₱5,495 | 73 | +11% | +21% | 58 | 5.5 | 0.6 | +11% | -2% | 1.7% |  |
| AT | Atlas Consolidated Mining and De | ₱17.92 | ₱1,792 | 71 | +13% | +253% | 46 | 12.9 | 1.3 | +10% | n/m | 0.0% |  |
| PX | Philex Mining Corporation | ₱10.70 | ₱1,070 | 71 | +7% | +33% | 52 | n/m | 1.8 | +1% | -166% | 0.4% | gravestone doji |

**How much to buy.** Split the money you set aside for PSE stocks into 10 equal parts and put one part in each pick, working down the list as you have free parts: with ₱100,000 that is ₱10,000 a stock. Holding fewer stocks made the swings bigger without raising the return in [the back-test](backtest_ph.md). *Min. buy* is the cost of one PSE board lot, the smallest amount you can buy. Run the portfolio command with your cash in portfolio.csv to get share counts.

P/E, P/B, ROE (return on equity), profit growth and dividend yield come from the companies' latest reports (PSE Edge; dividend yield is cash dividends with an ex-date in the last 12 months divided by the price). They are shown for context and are not part of the score yet. A loss or a very high P/E is worth a closer look before buying.

## Avoid

Liquid stocks with the weakest scores: falling trend and lagging the market. If you own one, check it in the portfolio section.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| MRC | MRC Allied, Inc. | ₱0.62 | ₱620 | 10 | -13% | -36% | 35 | – | 0.5 | – | n/m | 0.0% | dragonfly doji |
| PLUS | DigiPlus Interactive Corp. | ₱6.30 | ₱630 | 11 | -38% | -69% | 31 | 2.5 | 0.6 | +24% | -12% | 13.0% | bullish harami |
| WLCON | Wilcon Depot, Inc. | ₱5.10 | ₱510 | 11 | -14% | -40% | 31 | loss | loss | – | – | 7.6% | bearish harami, hammer, morning star |
| DITO | DITO CME Holdings Corp. | ₱0.54 | ₱540 | 13 | -27% | -34% | 36 | – | – | – | – | 0.0% |  |
| GSMI | Ginebra San Miguel,  Inc. | ₱210.00 | ₱2,100 | 13 | -16% | -25% | 40 | 6.8 | 2.2 | +33% | +4% | 8.1% | hammer, bullish harami |
| DMC | DMCI Holdings, Inc. | ₱6.64 | ₱664 | 14 | -9% | -40% | 39 | 4.7 | 0.7 | +14% | +27% | 4.5% | bullish harami |
| CNVRG | Converge Information and Communi | ₱9.05 | ₱905 | 15 | -17% | -29% | 45 | 5.8 | 1.0 | +17% | -8% | 5.4% |  |
| MWC | Manila Water Company, Inc. | ₱29.10 | ₱2,910 | 20 | -14% | -14% | 32 | 4.8 | 0.8 | +17% | +6% | 6.8% |  |
| SCC | Semirara Mining and Power Corpor | ₱11.00 | ₱1,100 | 21 | -45% | -67% | 36 | 3.3 | 0.7 | +21% | +11% | 0.0% | bearish engulfing |
| JFC | Jollibee Foods Corporation | ₱144.00 | ₱1,440 | 22 | -4% | -34% | 50 | – | 2.1 | – | -13% | 2.3% | hanging man, bearish harami |
| JGS | JG Summit Holdings, Inc. | ₱17.16 | ₱1,716 | 23 | -24% | -30% | 47 | loss | 0.5 | -32% | -29% | 2.6% | bearish harami |
| CREIT | Citicore Energy REIT Corp. | ₱2.77 | ₱2,770 | 24 | -18% | -19% | 42 | 12.5 | 3.8 | +30% | -0% | 7.5% | bullish harami, bearish marubozu |
| ALI | Ayala Land, Inc. | ₱14.84 | ₱1,484 | 24 | -9% | -29% | 41 | 6.1 | 0.7 | +11% | -19% | 6.6% |  |
| MER | Manila Electric Company | ₱424.00 | ₱4,240 | 25 | -14% | -26% | 44 | 9.4 | 2.8 | +30% | +11% | 6.4% | bearish marubozu, hanging man |

## Signals that have worked here

From the history study ([full table](signals_ph.md)). Only these count in the score.

- **breakout 52w high** (up): +0.84% vs the index over 10 days, right way 48% of 3,575 times — works as expected
- **bullish marubozu** (up): -0.22% vs the index over 10 days, right way 43% of 7,943 times — works in reverse
- **bullish engulfing** (up): -0.27% vs the index over 10 days, right way 44% of 5,335 times — works in reverse
- **macd cross up** (up): -0.27% vs the index over 10 days, right way 44% of 8,649 times — works in reverse
- **hammer** (up): -0.62% vs the index over 10 days, right way 44% of 4,767 times — works in reverse
- **dragonfly doji** (up): -0.68% vs the index over 10 days, right way 42% of 2,499 times — works in reverse
- **morning star** (up): -1.22% vs the index over 10 days, right way 36% of 452 times — works in reverse
- **three white soldiers** (up): -1.66% vs the index over 10 days, right way 30% of 77 times — works in reverse
- **gravestone doji** (down): +0.71% vs the index over 10 days, right way 52% of 1,403 times — works in reverse
- **bearish marubozu** (down): +0.33% vs the index over 10 days, right way 49% of 9,931 times — works in reverse
- **hanging man** (down): -0.24% vs the index over 10 days, right way 56% of 5,978 times — works as expected

## Has the score worked?

Each past month-end (154 months), liquid stocks were split into five equal groups by score (without the candle part). Average return over the next month beyond the index:

| Score group | 1 (weakest) | 2 | 3 | 4 | 5 (strongest) |
|---|---:|---:|---:|---:|---:|
| Next month vs index | -0.32% | -0.40% | -0.68% | -0.30% | +0.66% |

The strongest group beat the weakest in 55% of months (average gap +0.98% a month).

