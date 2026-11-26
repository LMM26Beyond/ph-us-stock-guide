# Philippines (PSE) — market guide

Data up to **Thu 26 Nov 2026**. Generated 26 Nov 2026.

> This is an automated technical analysis of past prices, not licensed financial advice. Signals are probabilities, not certainties. Check the company news and fundamentals and size every position so a stop-out is affordable.

## The market: Downtrend

Most stocks fall with the market in a downtrend. Expect bigger swings and consider buying smaller amounts.

| | |
|---|---|
| PSEi | 5,472.00 |
| vs 50-day average | -4.0% |
| vs 200-day average | -7.9% |
| 1 month / 3 months / 12 months | -4.1% / -10.7% / -1.6% |
| RSI (14) | 41 |
| Candles (last 3 days) | none |
| Stocks above their 200-day average | 14% |

PSEi before the first recorded real value is rebuilt from the AETF PSEi-tracker ETF, scaled to index points.

## Buy candidates

Liquid stocks with a score of 70 or more, above their 200-day average, not overextended (RSI ≤ 75, at most 30% above the 50-day average) and not too erratic (average daily range at most 5% of the price). Hold while the score stays at 60 or more; sell when it drops below at a month-end. These are the rules tested in [the back-test](backtest_ph.md).

**The market is in a downtrend.** In the back-test, buying anyway did better than waiting (waiting missed the rebounds), but expect bigger swings: consider smaller amounts.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| PNB | Philippine National Bank | ₱80.00 | ₱800 | 72 | +19% | +55% | 52 | 4.4 | 0.5 | +11% | +15% | 5.6% | dragonfly doji, piercing line |
| LTG | LT Group, Inc. | ₱15.48 | ₱1,548 | 71 | +2% | +4% | 56 | 4.8 | 0.6 | +13% | +14% | 8.3% |  |

**How much to buy.** Split the money you set aside for PSE stocks into 10 equal parts and put one part in each pick, working down the list as you have free parts: with ₱100,000 that is ₱10,000 a stock. Holding fewer stocks made the swings bigger without raising the return in [the back-test](backtest_ph.md). *Min. buy* is the cost of one PSE board lot, the smallest amount you can buy. Run the portfolio command with your cash in portfolio.csv to get share counts.

P/E, P/B, ROE (return on equity), profit growth and dividend yield come from the companies' latest reports (PSE Edge; dividend yield is cash dividends with an ex-date in the last 12 months divided by the price). They are shown for context and are not part of the score yet. A loss or a very high P/E is worth a closer look before buying.

## Avoid

Liquid stocks with the weakest scores: falling trend and lagging the market. If you own one, check it in the portfolio section.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| DMC | DMCI Holdings, Inc. | ₱6.28 | ₱628 | 9 | -21% | -37% | 37 | 4.5 | 0.6 | +14% | +27% | 4.8% | bullish engulfing |
| MRC | MRC Allied, Inc. | ₱0.56 | ₱560 | 9 | -20% | -41% | 39 | – | 0.4 | – | n/m | 0.0% | bullish engulfing, bullish engulfing, bullish marubozu |
| PLUS | DigiPlus Interactive Corp. | ₱4.94 | ₱4,940 | 11 | -49% | -81% | 28 | 2.1 | 0.5 | +24% | -12% | 16.6% |  |
| CNVRG | Converge Information and Communi | ₱8.00 | ₱800 | 11 | -16% | -37% | 27 | 5.4 | 0.9 | +16% | -9% | 6.0% | hammer, inverted hammer |
| SCC | Semirara Mining and Power Corpor | ₱8.87 | ₱887 | 11 | -52% | -69% | 30 | 2.6 | 0.6 | +21% | +11% | 0.0% | inverted hammer |
| JGS | JG Summit Holdings, Inc. | ₱16.20 | ₱1,620 | 15 | -25% | -23% | 35 | loss | 0.4 | -33% | -33% | 2.7% |  |
| MWC | Manila Water Company, Inc. | ₱27.00 | ₱2,700 | 18 | -23% | -24% | 32 | 4.6 | 0.7 | +16% | -5% | 7.8% | inverted hammer |
| MER | Manila Electric Company | ₱381.00 | ₱3,810 | 18 | -21% | -36% | 38 | 7.6 | 2.4 | +32% | +21% | 7.5% | bearish marubozu |
| SEVN | Philippine Seven Corporation | ₱31.00 | ₱3,100 | 19 | -8% | -23% | 46 | 13.0 | 4.1 | +31% | +3% | 3.5% | bullish engulfing |
| BLOOM | Bloomberry Resorts Corporation | ₱1.67 | ₱1,670 | 20 | -31% | -43% | 25 | loss | 0.3 | -6% | n/m | 0.0% | inverted hammer |
| ACEN | ACEN CORPORATION | ₱2.19 | ₱2,190 | 21 | -25% | -4% | 28 | 17.4 | 0.6 | +3% | +84% | 2.2% | bullish engulfing |
| FB | San Miguel Food and Beverage, In | ₱44.05 | ₱4,405 | 21 | -7% | -16% | 44 | 9.2 | 1.9 | +21% | -9% | 11.0% | piercing line |
| ALI | Ayala Land, Inc. | ₱13.66 | ₱1,366 | 22 | -11% | -29% | 27 | 6.0 | 0.6 | +10% | -18% | 4.9% |  |
| GLO | Globe Telecom, Inc. | ₱1,282.00 | ₱6,410 | 22 | -23% | -22% | 22 | 8.9 | 1.2 | +13% | -7% | 7.7% |  |
| NIKL | Nickel Asia Corporation | ₱3.34 | ₱3,340 | 23 | -22% | -13% | 28 | 6.8 | 1.1 | +17% | +19% | 6.2% | inverted hammer |
| TEL | PLDT Inc. | ₱942.00 | ₱9,420 | 23 | -21% | -26% | 26 | 7.5 | 1.6 | +22% | -8% | 9.7% |  |
| GSMI | Ginebra San Miguel,  Inc. | ₱208.00 | ₱2,080 | 24 | -8% | -26% | 40 | 6.7 | 2.1 | +32% | +4% | 7.5% | hammer, bullish engulfing |
| GTCAP | GT Capital Holdings, Inc. | ₱434.00 | ₱4,340 | 24 | -13% | -15% | 45 | 3.1 | 0.3 | +10% | -10% | 3.1% |  |
| MYNLD | Maynilad Water Services, Inc. | ₱15.06 | ₱1,506 | 25 | -18% | +4% | 28 | 7.2 | 1.0 | +14% | +11% | 7.4% | inverted hammer, bullish harami |

## Signals that have worked here

From the history study ([full table](signals_ph.md)). Only these count in the score.

- **breakout 52w high** (up): +0.84% vs the index over 10 days, right way 48% of 3,581 times — works as expected
- **bullish marubozu** (up): -0.22% vs the index over 10 days, right way 43% of 8,007 times — works in reverse
- **bullish engulfing** (up): -0.27% vs the index over 10 days, right way 44% of 5,366 times — works in reverse
- **macd cross up** (up): -0.28% vs the index over 10 days, right way 44% of 8,710 times — works in reverse
- **hammer** (up): -0.61% vs the index over 10 days, right way 44% of 4,805 times — works in reverse
- **dragonfly doji** (up): -0.66% vs the index over 10 days, right way 42% of 2,550 times — works in reverse
- **morning star** (up): -1.21% vs the index over 10 days, right way 36% of 457 times — works in reverse
- **three white soldiers** (up): -1.66% vs the index over 10 days, right way 30% of 77 times — works in reverse
- **gravestone doji** (down): +0.71% vs the index over 10 days, right way 52% of 1,413 times — works in reverse
- **bearish marubozu** (down): +0.32% vs the index over 10 days, right way 49% of 9,977 times — works in reverse
- **hanging man** (down): -0.25% vs the index over 10 days, right way 56% of 6,014 times — works as expected

## Has the score worked?

Each past month-end (154 months), liquid stocks were split into five equal groups by score (without the candle part). Average return over the next month beyond the index:

| Score group | 1 (weakest) | 2 | 3 | 4 | 5 (strongest) |
|---|---:|---:|---:|---:|---:|
| Next month vs index | -0.31% | -0.40% | -0.65% | -0.35% | +0.67% |

The strongest group beat the weakest in 56% of months (average gap +0.98% a month).

