# Back-test: United States

Oct 2017 to Nov 2026, starting with $20,000 and up to 40 stocks.

**Current rules.** Each month-end the stocks are scored with only the data known that day. Holdings scoring below 60 are sold. Free slots are filled with the report's buy candidates (score 70+, above the 200-day average, RSI ≤ 75, at most 30% above the 50-day average, average daily range at most 5% of the price) at the next day's open, in equal amounts.

Costs per trade: no commission, 0.003% regulatory fees and 0.05% slippage each way.

| Strategy | Yearly return | Total | Worst drop | Sharpe | Trades | Wins | Avg trade |
|---|---:|---:|---:|---:|---:|---:|---:|
| Current rules | +17.9% | +343.1% | -43.1% | 0.68 | 496 | 42% | +18.8% |
| Old rules (3 × ATR trailing stop, no buys in a downtrend, sell below 50, no range limit) | -0.7% | -6.5% | -43.6% | 0.08 | 1908 | 34% | +0.2% |
| Current rules, smaller amounts in more volatile stocks | +11.6% | +170.0% | -31.3% | 0.62 | 520 | 42% | +17.3% |
| Current rules, half as many stocks | +16.7% | +301.9% | -47.6% | 0.64 | 238 | 46% | +18.2% |
| Current rules + only profitable companies | +11.6% | +170.5% | -44.8% | 0.52 | 521 | 40% | +9.3% |
| Current rules + only ROE of 15% or more | +12.5% | +189.1% | -38.6% | 0.56 | 543 | 41% | +9.8% |
| Current rules + only P/E of 25 or less | +11.0% | +156.1% | -40.6% | 0.53 | 551 | 44% | +7.6% |
| Hold the index | +12.7% | +194.8% | -33.9% | 0.73 | – | – | – |

"Hold the index" is the S&P 500 with no costs and no dividends; the stock prices also exclude dividends, so the comparison is like for like.

## Tuned period and test period

The rule settings were the best of those tried on data up to Dec 2022, and the same settings came out on top in both markets. The later years were not used to pick them, so they are a fairer test, though not a perfectly blind one.

| Period | Current rules | S&P 500 |
|---|---:|---:|
| To Dec 2022 (tuned) | +13.7% a year | +8.0% a year |
| From Jan 2023 (test) | +25.0% a year | +19.5% a year |

## Position size

The current rules put an equal amount in each of up to 40 stocks. Two alternatives:

| Strategy | Yearly return | Worst drop | Tuned period | Test period |
|---|---:|---:|---:|---:|
| Current rules | +17.9% | -43.1% | +13.7% | +25.0% |
| Current rules, smaller amounts in more volatile stocks | +11.6% | -31.3% | +7.5% | +17.9% |
| Current rules, half as many stocks | +16.7% | -47.6% | +11.2% | +25.5% |

"Smaller amounts in more volatile stocks" scales each stock's amount by 2% divided by its average daily range as a share of the price, from half to double the equal amount. It gives smaller drops for a lower return: a choice for a cautious investor, not a free improvement. Holding fewer stocks made the swings bigger without raising the return in the tuned period, so keep the full number of stocks.

## Fundamentals filters

The same rules, but buying only companies that pass a test on their latest SEC filings as of each month-end (a company without the figure is skipped).

| Strategy | Tuned period | Test period |
|---|---:|---:|
| Current rules | +13.7% a year | +25.0% a year |
| Current rules + only profitable companies | +2.2% a year | +26.3% a year |
| Current rules + only ROE of 15% or more | +4.3% a year | +25.2% a year |
| Current rules + only P/E of 25 or less | +4.6% a year | +20.7% a year |

No filter beat the current rules in both periods. Strong momentum stocks are often young or fast-growing companies with losses or high P/Es, and the filters screen out exactly those. So the report shows P/E, P/B, ROE and growth as context only.

## Year by year

| Year | Current rules | S&P 500 | Difference |
|---|---:|---:|---:|
| 2017 | +3.3% | +3.8% | -0.6% |
| 2018 | -11.7% | -6.2% | -5.4% |
| 2019 | +24.9% | +28.9% | -4.0% |
| 2020 | +66.7% | +16.3% | +50.5% |
| 2021 | +10.8% | +26.9% | -16.1% |
| 2022 | -7.9% | -19.4% | +11.5% |
| 2023 | +12.5% | +24.2% | -11.7% |
| 2024 | +56.4% | +23.3% | +33.0% |
| 2025 | +30.6% | +16.4% | +14.2% |
| 2026 | -0.5% | +10.9% | -11.4% |

## Verdict

Following the current rules returned +17.9% a year against +12.7% for the S&P 500, after costs. The rules beat the index. The worst drop along the way was -43.1%, so expect deep falls and size your money accordingly.

What the tuning found: tight trailing stops (3 × ATR) sold good stocks on normal dips and were the biggest drag; sitting out market downtrends missed the rebounds; and the most erratic stocks (daily range above 5% of the price) hurt more than they helped.

Limits: delisted stocks are missing (which flatters the rules, more so in the US), dividends are ignored on both sides, and a past result does not promise a future one.
