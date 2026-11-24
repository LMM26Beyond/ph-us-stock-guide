# Back-test: United States

Oct 2017 to Nov 2026, starting with $20,000 and up to 40 stocks.

**Current rules.** Each month-end the stocks are scored with only the data known that day. Holdings scoring below 60 are sold. Free slots are filled with the report's buy candidates (score 70+, above the 200-day average, RSI ≤ 75, at most 30% above the 50-day average, average daily range at most 5% of the price) at the next day's open, in equal amounts.

Costs per trade: no commission, 0.003% regulatory fees and 0.05% slippage each way.

| Strategy | Yearly return | Total | Worst drop | Sharpe | Trades | Wins | Avg trade |
|---|---:|---:|---:|---:|---:|---:|---:|
| Current rules | +17.5% | +330.7% | -43.1% | 0.67 | 496 | 42% | +19.0% |
| Old rules (3 × ATR trailing stop, no buys in a downtrend, sell below 50, no range limit) | -0.8% | -7.1% | -42.0% | 0.07 | 1918 | 35% | +0.2% |
| Current rules, smaller amounts in more volatile stocks | +11.0% | +158.5% | -31.3% | 0.60 | 520 | 42% | +17.3% |
| Current rules, half as many stocks | +15.6% | +272.1% | -47.6% | 0.62 | 238 | 46% | +18.2% |
| Current rules + only profitable companies | +10.5% | +147.9% | -45.0% | 0.49 | 532 | 40% | +8.8% |
| Current rules + only ROE of 15% or more | +11.5% | +167.9% | -39.1% | 0.53 | 548 | 41% | +9.2% |
| Current rules + only P/E of 25 or less | +9.7% | +131.2% | -41.8% | 0.49 | 553 | 44% | +7.6% |
| Hold the index | +12.1% | +181.0% | -33.9% | 0.70 | – | – | – |

"Hold the index" is the S&P 500 with no costs and no dividends; the stock prices also exclude dividends, so the comparison is like for like.

## Tuned period and test period

The rule settings were the best of those tried on data up to Dec 2022, and the same settings came out on top in both markets. The later years were not used to pick them, so they are a fairer test, though not a perfectly blind one.

| Period | Current rules | S&P 500 |
|---|---:|---:|
| To Dec 2022 (tuned) | +14.3% a year | +8.0% a year |
| From Jan 2023 (test) | +22.9% a year | +17.8% a year |

## Position size

The current rules put an equal amount in each of up to 40 stocks. Two alternatives:

| Strategy | Yearly return | Worst drop | Tuned period | Test period |
|---|---:|---:|---:|---:|
| Current rules | +17.5% | -43.1% | +14.3% | +22.9% |
| Current rules, smaller amounts in more volatile stocks | +11.0% | -31.3% | +7.5% | +16.5% |
| Current rules, half as many stocks | +15.6% | -47.6% | +11.2% | +22.9% |

"Smaller amounts in more volatile stocks" scales each stock's amount by 2% divided by its average daily range as a share of the price, from half to double the equal amount. It gives smaller drops for a lower return: a choice for a cautious investor, not a free improvement. Holding fewer stocks made the swings bigger without raising the return in the tuned period, so keep the full number of stocks.

## Fundamentals filters

The same rules, but buying only companies that pass a test on their latest SEC filings as of each month-end (a company without the figure is skipped).

| Strategy | Tuned period | Test period |
|---|---:|---:|
| Current rules | +14.3% a year | +22.9% a year |
| Current rules + only profitable companies | +1.9% a year | +23.8% a year |
| Current rules + only ROE of 15% or more | +3.8% a year | +23.2% a year |
| Current rules + only P/E of 25 or less | +3.9% a year | +18.4% a year |

No filter beat the current rules in both periods. Strong momentum stocks are often young or fast-growing companies with losses or high P/Es, and the filters screen out exactly those. So the report shows P/E, P/B, ROE and growth as context only.

## Year by year

| Year | Current rules | S&P 500 | Difference |
|---|---:|---:|---:|
| 2017 | +3.3% | +3.8% | -0.6% |
| 2018 | -11.7% | -6.2% | -5.4% |
| 2019 | +24.9% | +28.9% | -4.0% |
| 2020 | +66.7% | +16.3% | +50.5% |
| 2021 | +14.4% | +26.9% | -12.5% |
| 2022 | -8.2% | -19.4% | +11.3% |
| 2023 | +12.0% | +24.2% | -12.2% |
| 2024 | +58.8% | +23.3% | +35.5% |
| 2025 | +31.1% | +16.4% | +14.7% |
| 2026 | -7.5% | +5.7% | -13.2% |

## Verdict

Following the current rules returned +17.5% a year against +12.1% for the S&P 500, after costs. The rules beat the index. The worst drop along the way was -43.1%, so expect deep falls and size your money accordingly.

What the tuning found: tight trailing stops (3 × ATR) sold good stocks on normal dips and were the biggest drag; sitting out market downtrends missed the rebounds; and the most erratic stocks (daily range above 5% of the price) hurt more than they helped.

Limits: delisted stocks are missing (which flatters the rules, more so in the US), dividends are ignored on both sides, and a past result does not promise a future one.
