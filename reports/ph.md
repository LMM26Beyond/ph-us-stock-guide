# Philippines (PSE) — market guide

Data up to **Fri 27 Nov 2026**. Generated 27 Nov 2026.

> This is an automated technical analysis of past prices, not licensed financial advice. Signals are probabilities, not certainties. Check the company news and fundamentals and size every position so a stop-out is affordable.

## The market: Downtrend

Most stocks fall with the market in a downtrend. Expect bigger swings and consider buying smaller amounts.

| | |
|---|---|
| PSEi | 5,505.26 |
| vs 50-day average | -3.3% |
| vs 200-day average | -7.2% |
| 1 month / 3 months / 12 months | -3.4% / -10.1% / -0.9% |
| RSI (14) | 44 |
| Candles (last 3 days) | inverted hammer |
| Stocks above their 200-day average | 16% |

PSEi before the first recorded real value is rebuilt from the AETF PSEi-tracker ETF, scaled to index points.

## Buy candidates

Liquid stocks with a score of 70 or more, above their 200-day average, not overextended (RSI ≤ 75, at most 30% above the 50-day average) and not too erratic (average daily range at most 5% of the price). Hold while the score stays at 60 or more; sell when it drops below at a month-end. These are the rules tested in [the back-test](backtest_ph.md).

**The market is in a downtrend.** In the back-test, buying anyway did better than waiting (waiting missed the rebounds), but expect bigger swings: consider smaller amounts.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| AEV | Aboitiz Equity Ventures, Inc. | ₱34.50 | ₱3,450 | 72 | -9% | +42% | 28 | 10.7 | 0.7 | +6% | +2% | 4.2% |  |
| LTG | LT Group, Inc. | ₱15.80 | ₱1,580 | 72 | +4% | +10% | 63 | 4.8 | 0.6 | +13% | +14% | 8.3% |  |
| PNB | Philippine National Bank | ₱81.35 | ₱814 | 71 | +25% | +61% | 57 | 4.4 | 0.5 | +11% | +15% | 5.6% | dragonfly doji |
| AC | Ayala Corporation | ₱544.00 | ₱5,440 | 70 | +11% | +35% | 53 | 6.5 | 0.6 | +10% | -22% | 1.8% | bullish engulfing |

**How much to buy.** Split the money you set aside for PSE stocks into 10 equal parts and put one part in each pick, working down the list as you have free parts: with ₱100,000 that is ₱10,000 a stock. Holding fewer stocks made the swings bigger without raising the return in [the back-test](backtest_ph.md). *Min. buy* is the cost of one PSE board lot, the smallest amount you can buy. Run the portfolio command with your cash in portfolio.csv to get share counts.

P/E, P/B, ROE (return on equity), profit growth and dividend yield come from the companies' latest reports (PSE Edge; dividend yield is cash dividends with an ex-date in the last 12 months divided by the price). They are shown for context and are not part of the score yet. A loss or a very high P/E is worth a closer look before buying.

## Avoid

Liquid stocks with the weakest scores: falling trend and lagging the market. If you own one, check it in the portfolio section.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| MRC | MRC Allied, Inc. | ₱0.55 | ₱550 | 10 | -21% | -41% | 36 | – | 0.4 | – | n/m | 0.0% | bearish harami, bullish engulfing |
| CNVRG | Converge Information and Communi | ₱7.95 | ₱795 | 11 | -15% | -35% | 26 | 5.4 | 0.9 | +16% | -9% | 6.0% | hammer |
| SCC | Semirara Mining and Power Corpor | ₱8.92 | ₱892 | 11 | -52% | -67% | 30 | 2.6 | 0.6 | +21% | +11% | 0.0% | inverted hammer |
| PLUS | DigiPlus Interactive Corp. | ₱4.80 | ₱4,800 | 11 | -50% | -80% | 26 | 2.1 | 0.5 | +24% | -12% | 16.6% |  |
| MER | Manila Electric Company | ₱395.20 | ₱3,952 | 13 | -16% | -32% | 44 | 7.6 | 2.4 | +32% | +21% | 7.5% |  |
| DMC | DMCI Holdings, Inc. | ₱6.10 | ₱610 | 13 | -22% | -38% | 32 | 4.5 | 0.6 | +14% | +27% | 4.8% | bearish marubozu, bullish engulfing |
| JGS | JG Summit Holdings, Inc. | ₱16.22 | ₱1,622 | 15 | -25% | -22% | 35 | loss | 0.4 | -33% | -33% | 2.7% | inverted hammer |
| MWC | Manila Water Company, Inc. | ₱27.05 | ₱2,705 | 18 | -23% | -23% | 33 | 4.6 | 0.7 | +16% | -5% | 7.8% |  |
| ALI | Ayala Land, Inc. | ₱13.22 | ₱1,322 | 21 | -15% | -30% | 23 | 6.0 | 0.6 | +10% | -18% | 4.9% |  |
| BLOOM | Bloomberry Resorts Corporation | ₱1.68 | ₱1,680 | 21 | -30% | -38% | 27 | loss | 0.3 | -6% | n/m | 0.0% | inverted hammer, inverted hammer |
| FB | San Miguel Food and Beverage, In | ₱44.00 | ₱4,400 | 21 | -7% | -15% | 44 | 9.2 | 1.9 | +21% | -9% | 11.0% |  |
| GSMI | Ginebra San Miguel,  Inc. | ₱207.60 | ₱2,076 | 21 | -5% | -26% | 39 | 6.7 | 2.1 | +32% | +4% | 7.5% | hammer |
| TEL | PLDT Inc. | ₱953.00 | ₱9,530 | 22 | -16% | -24% | 29 | 7.5 | 1.6 | +22% | -8% | 9.7% | bullish harami |
| SMC | San Miguel Corporation | ₱62.00 | ₱620 | 22 | -4% | -9% | 43 | 18.2 | 0.5 | +3% | -84% | 2.2% | bearish marubozu, bullish engulfing, bullish marubozu |
| GTCAP | GT Capital Holdings, Inc. | ₱431.00 | ₱4,310 | 23 | -12% | -15% | 44 | 3.1 | 0.3 | +10% | -10% | 3.1% |  |
| GLO | Globe Telecom, Inc. | ₱1,307.00 | ₱6,535 | 23 | -21% | -18% | 29 | 8.9 | 1.2 | +13% | -7% | 7.7% |  |
| NIKL | Nickel Asia Corporation | ₱3.35 | ₱3,350 | 24 | -18% | -6% | 28 | 6.8 | 1.1 | +17% | +19% | 6.2% |  |
| AREIT | AREIT, Inc. | ₱34.50 | ₱3,450 | 24 | -7% | -16% | 33 | – | 0.9 | – | +31% | 7.3% | hammer, bearish marubozu |

## Signals that have worked here

From the history study ([full table](signals_ph.md)). Only these count in the score.

- **breakout 52w high** (up): +0.84% vs the index over 10 days, right way 48% of 3,582 times — works as expected
- **bullish marubozu** (up): -0.22% vs the index over 10 days, right way 43% of 8,007 times — works in reverse
- **bullish engulfing** (up): -0.27% vs the index over 10 days, right way 44% of 5,369 times — works in reverse
- **macd cross up** (up): -0.27% vs the index over 10 days, right way 44% of 8,714 times — works in reverse
- **hammer** (up): -0.61% vs the index over 10 days, right way 44% of 4,806 times — works in reverse
- **dragonfly doji** (up): -0.66% vs the index over 10 days, right way 42% of 2,550 times — works in reverse
- **morning star** (up): -1.21% vs the index over 10 days, right way 36% of 457 times — works in reverse
- **three white soldiers** (up): -1.66% vs the index over 10 days, right way 30% of 77 times — works in reverse
- **gravestone doji** (down): +0.71% vs the index over 10 days, right way 52% of 1,413 times — works in reverse
- **bearish marubozu** (down): +0.32% vs the index over 10 days, right way 49% of 9,980 times — works in reverse
- **hanging man** (down): -0.25% vs the index over 10 days, right way 56% of 6,015 times — works as expected

## Has the score worked?

Each past month-end (154 months), liquid stocks were split into five equal groups by score (without the candle part). Average return over the next month beyond the index:

| Score group | 1 (weakest) | 2 | 3 | 4 | 5 (strongest) |
|---|---:|---:|---:|---:|---:|
| Next month vs index | -0.31% | -0.40% | -0.65% | -0.35% | +0.67% |

The strongest group beat the weakest in 56% of months (average gap +0.98% a month).

