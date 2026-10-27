# Philippines (PSE) — market guide

Data up to **Tue 27 Oct 2026**. Generated 27 Oct 2026.

> This is an automated technical analysis of past prices, not licensed financial advice. Signals are probabilities, not certainties. Check the company news and fundamentals and size every position so a stop-out is affordable.

## The market: Downtrend

Most stocks fall with the market in a downtrend. Expect bigger swings and consider buying smaller amounts.

| | |
|---|---|
| PSEi | 5,761.19 |
| vs 50-day average | -1.7% |
| vs 200-day average | -3.7% |
| 1 month / 3 months / 12 months | -0.1% / -7.8% / -1.7% |
| RSI (14) | 50 |
| Candles (last 3 days) | bullish marubozu, bullish marubozu |
| Stocks above their 200-day average | 31% |

PSEi before the first recorded real value is rebuilt from the AETF PSEi-tracker ETF, scaled to index points.

## Buy candidates

Liquid stocks with a score of 70 or more, above their 200-day average, not overextended (RSI ≤ 75, at most 30% above the 50-day average) and not too erratic (average daily range at most 5% of the price). Hold while the score stays at 60 or more; sell when it drops below at a month-end. These are the rules tested in [the back-test](backtest_ph.md).

**The market is in a downtrend.** In the back-test, buying anyway did better than waiting (waiting missed the rebounds), but expect bigger swings: consider smaller amounts.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| AEV | Aboitiz Equity Ventures, Inc. | ₱40.40 | ₱4,040 | 85 | +18% | +42% | 61 | 9.5 | 0.8 | +8% | +63% | 3.9% | bearish engulfing, shooting star |
| PNB | Philippine National Bank | ₱80.00 | ₱800 | 85 | +29% | +51% | 64 | 4.3 | 0.5 | +11% | +17% | 5.7% |  |
| SGP | Synergy Grid & Development Phils | ₱26.00 | ₱2,600 | 84 | -7% | +59% | 65 | 3.8 | 0.9 | +23% | +144% | 4.2% |  |
| MEG | Megaworld Corporation | ₱2.30 | ₱2,300 | 81 | +8% | +21% | 62 | 3.4 | 0.3 | +7% | +2% | 5.2% |  |
| ICT | International Container Terminal | ₱850.00 | ₱8,500 | 77 | -13% | +55% | 45 | – | – | – | – | 2.1% |  |
| FGEN | First Gen Corporation | ₱19.70 | ₱1,970 | 70 | -4% | +28% | 44 | – | 0.4 | – | -9% | 4.1% | bullish engulfing, inverted hammer |

**How much to buy.** Split the money you set aside for PSE stocks into 10 equal parts and put one part in each pick, working down the list as you have free parts: with ₱100,000 that is ₱10,000 a stock. Holding fewer stocks made the swings bigger without raising the return in [the back-test](backtest_ph.md). *Min. buy* is the cost of one PSE board lot, the smallest amount you can buy. Run the portfolio command with your cash in portfolio.csv to get share counts.

P/E, P/B, ROE (return on equity), profit growth and dividend yield come from the companies' latest reports (PSE Edge; dividend yield is cash dividends with an ex-date in the last 12 months divided by the price). They are shown for context and are not part of the score yet. A loss or a very high P/E is worth a closer look before buying.

## Avoid

Liquid stocks with the weakest scores: falling trend and lagging the market. If you own one, check it in the portfolio section.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| MRC | MRC Allied, Inc. | ₱0.63 | ₱630 | 9 | -21% | -38% | 35 | – | 0.5 | – | n/m | 0.0% | hammer, hammer |
| PLUS | DigiPlus Interactive Corp. | ₱6.93 | ₱693 | 16 | -31% | -70% | 34 | 2.4 | 0.7 | +29% | +17% | 11.9% | inverted hammer, bullish engulfing |
| CREIT | Citicore Energy REIT Corp. | ₱2.79 | ₱2,790 | 19 | -18% | -23% | 33 | 13.0 | 4.0 | +30% | -0% | 7.3% | bullish harami |
| DMC | DMCI Holdings, Inc. | ₱6.40 | ₱640 | 19 | -14% | -42% | 23 | 5.5 | 0.8 | +14% | +25% | 11.1% | bearish marubozu |
| MER | Manila Electric Company | ₱441.60 | ₱4,416 | 21 | -21% | -21% | 49 | 8.8 | 2.6 | +30% | +11% | 6.7% | bullish marubozu, bullish harami |
| JGS | JG Summit Holdings, Inc. | ₱17.00 | ₱1,700 | 21 | -28% | -29% | 40 | loss | 0.4 | -32% | -29% | 2.7% | bullish engulfing |
| SCC | Semirara Mining and Power Corpor | ₱10.50 | ₱1,050 | 21 | -50% | -69% | 27 | 3.7 | 0.8 | +21% | +2% | 11.3% |  |
| RCR | RL Commercial REIT, Inc. | ₱6.03 | ₱603 | 23 | -14% | -17% | 39 | 13.3 | 0.8 | +6% | +44% | 7.3% |  |
| URC | Universal Robina Corporation | ₱57.25 | ₱572 | 23 | -5% | -26% | 41 | 11.2 | 1.0 | +9% | +10% | 7.7% | inverted hammer |
| AREIT | AREIT, Inc. | ₱36.00 | ₱3,600 | 24 | -3% | -18% | 43 | – | – | – | +36% | 6.9% |  |
| MWC | Manila Water Company, Inc. | ₱31.80 | ₱3,180 | 25 | -9% | -14% | 45 | 5.0 | 0.9 | +17% | +6% | 6.5% | bullish engulfing |

## Signals that have worked here

From the history study ([full table](signals_ph.md)). Only these count in the score.

- **breakout 52w high** (up): +0.84% vs the index over 10 days, right way 48% of 3,574 times — works as expected
- **bullish marubozu** (up): -0.22% vs the index over 10 days, right way 43% of 7,932 times — works in reverse
- **bullish engulfing** (up): -0.27% vs the index over 10 days, right way 44% of 5,311 times — works in reverse
- **macd cross up** (up): -0.28% vs the index over 10 days, right way 44% of 8,623 times — works in reverse
- **hammer** (up): -0.62% vs the index over 10 days, right way 44% of 4,747 times — works in reverse
- **dragonfly doji** (up): -0.69% vs the index over 10 days, right way 42% of 2,490 times — works in reverse
- **morning star** (up): -1.22% vs the index over 10 days, right way 36% of 452 times — works in reverse
- **three white soldiers** (up): -1.66% vs the index over 10 days, right way 30% of 77 times — works in reverse
- **gravestone doji** (down): +0.72% vs the index over 10 days, right way 52% of 1,402 times — works in reverse
- **bearish marubozu** (down): +0.33% vs the index over 10 days, right way 49% of 9,901 times — works in reverse
- **hanging man** (down): -0.24% vs the index over 10 days, right way 56% of 5,970 times — works as expected

## Has the score worked?

Each past month-end (153 months), liquid stocks were split into five equal groups by score (without the candle part). Average return over the next month beyond the index:

| Score group | 1 (weakest) | 2 | 3 | 4 | 5 (strongest) |
|---|---:|---:|---:|---:|---:|
| Next month vs index | -0.33% | -0.40% | -0.70% | -0.30% | +0.69% |

The strongest group beat the weakest in 55% of months (average gap +1.01% a month).

