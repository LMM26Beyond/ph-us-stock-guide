# Philippines (PSE) — market guide

Data up to **Wed 25 Nov 2026**. Generated 25 Nov 2026.

> This is an automated technical analysis of past prices, not licensed financial advice. Signals are probabilities, not certainties. Check the company news and fundamentals and size every position so a stop-out is affordable.

## The market: Downtrend

Most stocks fall with the market in a downtrend. Expect bigger swings and consider buying smaller amounts.

| | |
|---|---|
| PSEi | 5,435.16 |
| vs 50-day average | -4.9% |
| vs 200-day average | -8.5% |
| 1 month / 3 months / 12 months | -4.9% / -10.2% / -2.6% |
| RSI (14) | 38 |
| Candles (last 3 days) | none |
| Stocks above their 200-day average | 19% |

PSEi before the first recorded real value is rebuilt from the AETF PSEi-tracker ETF, scaled to index points.

## Buy candidates

Liquid stocks with a score of 70 or more, above their 200-day average, not overextended (RSI ≤ 75, at most 30% above the 50-day average) and not too erratic (average daily range at most 5% of the price). Hold while the score stays at 60 or more; sell when it drops below at a month-end. These are the rules tested in [the back-test](backtest_ph.md).

**The market is in a downtrend.** In the back-test, buying anyway did better than waiting (waiting missed the rebounds), but expect bigger swings: consider smaller amounts.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| PNB | Philippine National Bank | ₱79.90 | ₱799 | 76 | +20% | +56% | 52 | 4.4 | 0.5 | +11% | +15% | 5.6% | piercing line |
| AC | Ayala Corporation | ₱529.00 | ₱5,290 | 74 | +4% | +26% | 44 | 6.5 | 0.6 | +10% | -22% | 1.8% | inverted hammer |
| LTG | LT Group, Inc. | ₱15.46 | ₱1,546 | 71 | +2% | +7% | 56 | 4.8 | 0.6 | +13% | +14% | 8.3% |  |

**How much to buy.** Split the money you set aside for PSE stocks into 10 equal parts and put one part in each pick, working down the list as you have free parts: with ₱100,000 that is ₱10,000 a stock. Holding fewer stocks made the swings bigger without raising the return in [the back-test](backtest_ph.md). *Min. buy* is the cost of one PSE board lot, the smallest amount you can buy. Run the portfolio command with your cash in portfolio.csv to get share counts.

P/E, P/B, ROE (return on equity), profit growth and dividend yield come from the companies' latest reports (PSE Edge; dividend yield is cash dividends with an ex-date in the last 12 months divided by the price). They are shown for context and are not part of the score yet. A loss or a very high P/E is worth a closer look before buying.

## Avoid

Liquid stocks with the weakest scores: falling trend and lagging the market. If you own one, check it in the portfolio section.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| MRC | MRC Allied, Inc. | ₱0.53 | ₱530 | 8 | -24% | -45% | 25 | – | 0.4 | – | n/m | 0.0% | bullish engulfing, bullish marubozu, hammer |
| PLUS | DigiPlus Interactive Corp. | ₱5.12 | ₱512 | 11 | -48% | -80% | 30 | 2.1 | 0.5 | +24% | -12% | 16.6% |  |
| SCC | Semirara Mining and Power Corpor | ₱8.92 | ₱892 | 11 | -52% | -69% | 30 | 2.6 | 0.6 | +21% | +11% | 0.0% | inverted hammer |
| DMC | DMCI Holdings, Inc. | ₱6.11 | ₱611 | 14 | -22% | -39% | 28 | 4.5 | 0.6 | +14% | +27% | 4.8% |  |
| GSMI | Ginebra San Miguel,  Inc. | ₱208.00 | ₱2,080 | 14 | -8% | -26% | 40 | 6.7 | 2.1 | +32% | +4% | 7.5% | hammer, bullish engulfing |
| JGS | JG Summit Holdings, Inc. | ₱16.56 | ₱1,656 | 15 | -23% | -22% | 39 | loss | 0.4 | -33% | -33% | 2.7% |  |
| CNVRG | Converge Information and Communi | ₱8.04 | ₱804 | 16 | -15% | -36% | 28 | 5.4 | 0.9 | +16% | -9% | 6.0% | inverted hammer |
| BLOOM | Bloomberry Resorts Corporation | ₱1.70 | ₱1,700 | 17 | -31% | -43% | 27 | loss | 0.3 | -6% | n/m | 0.0% | inverted hammer, dragonfly doji |
| MER | Manila Electric Company | ₱360.00 | ₱3,600 | 18 | -25% | -36% | 27 | 7.6 | 2.4 | +32% | +21% | 7.5% | bearish marubozu, bearish marubozu |
| MWC | Manila Water Company, Inc. | ₱26.10 | ₱2,610 | 18 | -27% | -25% | 20 | 4.6 | 0.7 | +16% | -5% | 7.8% | inverted hammer |
| ALI | Ayala Land, Inc. | ₱13.70 | ₱1,370 | 21 | -13% | -28% | 27 | 6.0 | 0.6 | +10% | -18% | 4.9% |  |
| FB | San Miguel Food and Beverage, In | ₱44.00 | ₱4,400 | 21 | -7% | -15% | 44 | 9.2 | 1.9 | +21% | -9% | 11.0% | piercing line |
| ACEN | ACEN CORPORATION | ₱2.30 | ₱2,300 | 22 | -20% | -0% | 33 | 17.4 | 0.6 | +3% | +84% | 2.2% | bullish engulfing, hammer |
| SEVN | Philippine Seven Corporation | ₱30.60 | ₱3,060 | 22 | -9% | -24% | 41 | 13.0 | 4.1 | +31% | +3% | 3.5% |  |
| NIKL | Nickel Asia Corporation | ₱3.32 | ₱3,320 | 23 | -23% | -14% | 26 | 6.8 | 1.1 | +17% | +19% | 6.2% | inverted hammer |
| GLO | Globe Telecom, Inc. | ₱1,250.00 | ₱6,250 | 23 | -26% | -17% | 11 | 8.9 | 1.2 | +13% | -7% | 7.7% |  |
| GTCAP | GT Capital Holdings, Inc. | ₱435.00 | ₱4,350 | 23 | -13% | -14% | 46 | 3.1 | 0.3 | +10% | -10% | 3.1% |  |
| AREIT | AREIT, Inc. | ₱35.35 | ₱3,535 | 24 | -6% | -15% | 44 | – | 0.9 | – | +31% | 7.2% | inverted hammer |
| TEL | PLDT Inc. | ₱960.00 | ₱9,600 | 24 | -20% | -21% | 28 | 7.5 | 1.6 | +22% | -8% | 9.7% |  |
| MYNLD | Maynilad Water Services, Inc. | ₱15.10 | ₱1,510 | 25 | -16% | +7% | 28 | 7.2 | 1.0 | +14% | +11% | 7.4% | inverted hammer, bullish harami |

## Signals that have worked here

From the history study ([full table](signals_ph.md)). Only these count in the score.

- **breakout 52w high** (up): +0.84% vs the index over 10 days, right way 48% of 3,580 times — works as expected
- **bullish marubozu** (up): -0.22% vs the index over 10 days, right way 43% of 8,006 times — works in reverse
- **bullish engulfing** (up): -0.27% vs the index over 10 days, right way 44% of 5,365 times — works in reverse
- **macd cross up** (up): -0.28% vs the index over 10 days, right way 44% of 8,706 times — works in reverse
- **hammer** (up): -0.61% vs the index over 10 days, right way 44% of 4,804 times — works in reverse
- **dragonfly doji** (up): -0.66% vs the index over 10 days, right way 42% of 2,549 times — works in reverse
- **morning star** (up): -1.21% vs the index over 10 days, right way 36% of 457 times — works in reverse
- **three white soldiers** (up): -1.66% vs the index over 10 days, right way 30% of 77 times — works in reverse
- **gravestone doji** (down): +0.71% vs the index over 10 days, right way 52% of 1,412 times — works in reverse
- **bearish marubozu** (down): +0.32% vs the index over 10 days, right way 49% of 9,977 times — works in reverse
- **hanging man** (down): -0.25% vs the index over 10 days, right way 56% of 6,010 times — works as expected

## Has the score worked?

Each past month-end (154 months), liquid stocks were split into five equal groups by score (without the candle part). Average return over the next month beyond the index:

| Score group | 1 (weakest) | 2 | 3 | 4 | 5 (strongest) |
|---|---:|---:|---:|---:|---:|
| Next month vs index | -0.31% | -0.40% | -0.65% | -0.35% | +0.67% |

The strongest group beat the weakest in 56% of months (average gap +0.98% a month).

