# Philippines (PSE) — market guide

Data up to **Tue 27 Oct 2026**. Generated 27 Oct 2026.

> This is an automated technical analysis of past prices, not licensed financial advice. Signals are probabilities, not certainties. Check the company news and fundamentals and size every position so a stop-out is affordable.

## The market: Downtrend

Most stocks fall with the market in a downtrend. Expect bigger swings and consider buying smaller amounts.

| | |
|---|---|
| PSEi | 5,700.06 |
| vs 50-day average | -2.8% |
| vs 200-day average | -4.8% |
| 1 month / 3 months / 12 months | -1.2% / -8.8% / -2.8% |
| RSI (14) | 44 |
| Candles (last 3 days) | bullish marubozu |
| Stocks above their 200-day average | 29% |

PSEi before the first recorded real value is rebuilt from the AETF PSEi-tracker ETF, scaled to index points.

## Buy candidates

Liquid stocks with a score of 70 or more, above their 200-day average, not overextended (RSI ≤ 75, at most 30% above the 50-day average) and not too erratic (average daily range at most 5% of the price). Hold while the score stays at 60 or more; sell when it drops below at a month-end. These are the rules tested in [the back-test](backtest_ph.md).

**The market is in a downtrend.** In the back-test, buying anyway did better than waiting (waiting missed the rebounds), but expect bigger swings: consider smaller amounts.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| AEV | Aboitiz Equity Ventures, Inc. | ₱39.55 | ₱3,955 | 90 | +16% | +39% | 56 | 9.5 | 0.8 | +8% | +63% | 3.9% | bearish engulfing, shooting star, gravestone doji |
| SGP | Synergy Grid & Development Phils | ₱24.65 | ₱2,465 | 83 | -12% | +52% | 58 | 3.8 | 0.9 | +23% | +144% | 4.2% |  |
| MEG | Megaworld Corporation | ₱2.26 | ₱2,260 | 80 | +7% | +13% | 57 | 3.4 | 0.3 | +7% | +2% | 5.2% |  |
| PNB | Philippine National Bank | ₱77.35 | ₱774 | 80 | +28% | +49% | 57 | 4.3 | 0.5 | +11% | +17% | 5.7% | hanging man |
| ICT | International Container Terminal | ₱840.00 | ₱8,400 | 76 | -14% | +56% | 43 | – | – | – | – | 2.1% |  |
| FGEN | First Gen Corporation | ₱19.50 | ₱1,950 | 74 | -5% | +26% | 42 | – | 0.4 | – | -9% | 4.1% | inverted hammer |
| FPH | First Philippine Holdings Corpor | ₱85.50 | ₱855 | 73 | -7% | +17% | 33 | 1.8 | 0.2 | +10% | +3% | 2.6% |  |

**How much to buy.** Split the money you set aside for PSE stocks into 10 equal parts and put one part in each pick, working down the list as you have free parts: with ₱100,000 that is ₱10,000 a stock. Holding fewer stocks made the swings bigger without raising the return in [the back-test](backtest_ph.md). *Min. buy* is the cost of one PSE board lot, the smallest amount you can buy. Run the portfolio command with your cash in portfolio.csv to get share counts.

P/E, P/B, ROE (return on equity), profit growth and dividend yield come from the companies' latest reports (PSE Edge; dividend yield is cash dividends with an ex-date in the last 12 months divided by the price). They are shown for context and are not part of the score yet. A loss or a very high P/E is worth a closer look before buying.

## Avoid

Liquid stocks with the weakest scores: falling trend and lagging the market. If you own one, check it in the portfolio section.

| Stock | Name | Close | Min. buy | Score | 3 mo | 12 mo | RSI | P/E | P/B | ROE | Profit growth | Div yield | Recent candles |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| DMC | DMCI Holdings, Inc. | ₱7.01 | ₱701 | 10 | -8% | -39% | 34 | 5.5 | 0.8 | +14% | +25% | 11.1% | bullish engulfing |
| MRC | MRC Allied, Inc. | ₱0.64 | ₱640 | 10 | -19% | -36% | 37 | – | 0.5 | – | n/m | 0.0% | hammer, bullish marubozu |
| PLUS | DigiPlus Interactive Corp. | ₱6.98 | ₱698 | 16 | -30% | -70% | 35 | 2.4 | 0.7 | +29% | +17% | 11.9% | bullish engulfing |
| CEB | Cebu Air, Inc. | ₱23.50 | ₱2,350 | 19 | -19% | -25% | 53 | loss | 1.4 | -26% | -166% | 0.0% | bearish engulfing, hanging man |
| SCC | Semirara Mining and Power Corpor | ₱11.04 | ₱1,104 | 21 | -49% | -68% | 30 | 3.7 | 0.8 | +21% | +2% | 11.3% |  |
| AREIT | AREIT, Inc. | ₱36.00 | ₱3,600 | 23 | -3% | -17% | 43 | – | – | – | +36% | 6.9% |  |
| CREIT | Citicore Energy REIT Corp. | ₱2.78 | ₱2,780 | 23 | -18% | -24% | 31 | 13.0 | 4.0 | +30% | -0% | 7.3% | hammer |
| URC | Universal Robina Corporation | ₱57.30 | ₱573 | 24 | -5% | -25% | 41 | 11.2 | 1.0 | +9% | +10% | 7.7% | inverted hammer |

## Signals that have worked here

From the history study ([full table](signals_ph.md)). Only these count in the score.

- **breakout 52w high** (up): +0.84% vs the index over 10 days, right way 48% of 3,573 times — works as expected
- **bullish marubozu** (up): -0.22% vs the index over 10 days, right way 43% of 7,931 times — works in reverse
- **bullish engulfing** (up): -0.27% vs the index over 10 days, right way 44% of 5,308 times — works in reverse
- **macd cross up** (up): -0.28% vs the index over 10 days, right way 44% of 8,617 times — works in reverse
- **hammer** (up): -0.62% vs the index over 10 days, right way 44% of 4,746 times — works in reverse
- **dragonfly doji** (up): -0.69% vs the index over 10 days, right way 42% of 2,489 times — works in reverse
- **morning star** (up): -1.22% vs the index over 10 days, right way 36% of 452 times — works in reverse
- **three white soldiers** (up): -1.66% vs the index over 10 days, right way 30% of 77 times — works in reverse
- **gravestone doji** (down): +0.71% vs the index over 10 days, right way 52% of 1,402 times — works in reverse
- **bearish marubozu** (down): +0.33% vs the index over 10 days, right way 49% of 9,900 times — works in reverse
- **hanging man** (down): -0.24% vs the index over 10 days, right way 56% of 5,969 times — works as expected

## Has the score worked?

Each past month-end (153 months), liquid stocks were split into five equal groups by score (without the candle part). Average return over the next month beyond the index:

| Score group | 1 (weakest) | 2 | 3 | 4 | 5 (strongest) |
|---|---:|---:|---:|---:|---:|
| Next month vs index | -0.33% | -0.40% | -0.70% | -0.30% | +0.69% |

The strongest group beat the weakest in 55% of months (average gap +1.01% a month).

