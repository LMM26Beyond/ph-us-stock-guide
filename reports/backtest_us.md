# Back-test: United States

Oct 2017 to Nov 2026, starting with $20,000 and up to 40 stocks.

**Current rules.** Each month-end the stocks are scored with only the data known that day. Holdings scoring below 60 are sold. Free slots are filled with the report's buy candidates (score 70+, above the 200-day average, RSI ≤ 75, at most 30% above the 50-day average, average daily range at most 5% of the price) at the next day's open, in equal amounts.

Costs per trade: no commission, 0.003% regulatory fees and 0.05% slippage each way.

| Strategy | Yearly return | Total | Worst drop | Sharpe | Trades | Wins | Avg trade |
|---|---:|---:|---:|---:|---:|---:|---:|
| Current rules | +18.5% | +360.6% | -43.1% | 0.70 | 499 | 42% | +18.5% |
| Old rules (3 × ATR trailing stop, no buys in a downtrend, sell below 50, no range limit) | -0.4% | -3.7% | -42.2% | 0.09 | 1890 | 35% | +0.3% |
| Current rules, smaller amounts in more volatile stocks | +11.0% | +156.1% | -31.3% | 0.60 | 524 | 41% | +17.3% |
| Current rules, half as many stocks | +17.2% | +316.4% | -47.6% | 0.66 | 241 | 45% | +16.8% |
| Current rules + only profitable companies | +11.1% | +158.6% | -44.6% | 0.51 | 531 | 40% | +8.7% |
| Current rules + only ROE of 15% or more | +12.0% | +177.2% | -38.8% | 0.55 | 550 | 40% | +9.3% |
| Current rules + only P/E of 25 or less | +10.9% | +154.3% | -40.6% | 0.53 | 553 | 44% | +7.4% |
| Hold the index | +12.7% | +193.9% | -33.9% | 0.73 | – | – | – |

"Hold the index" is the S&P 500 with no costs and no dividends; the stock prices also exclude dividends, so the comparison is like for like.

## Tuned period and test period

The rule settings were the best of those tried on data up to Dec 2022, and the same settings came out on top in both markets. The later years were not used to pick them, so they are a fairer test, though not a perfectly blind one.

| Period | Current rules | S&P 500 |
|---|---:|---:|
| To Dec 2022 (tuned) | +14.1% a year | +8.0% a year |
| From Jan 2023 (test) | +25.8% a year | +19.5% a year |

## Position size

The current rules put an equal amount in each of up to 40 stocks. Two alternatives:

| Strategy | Yearly return | Worst drop | Tuned period | Test period |
|---|---:|---:|---:|---:|
| Current rules | +18.5% | -43.1% | +14.1% | +25.8% |
| Current rules, smaller amounts in more volatile stocks | +11.0% | -31.3% | +7.4% | +16.6% |
| Current rules, half as many stocks | +17.2% | -47.6% | +10.7% | +27.5% |

"Smaller amounts in more volatile stocks" scales each stock's amount by 2% divided by its average daily range as a share of the price, from half to double the equal amount. It gives smaller drops for a lower return: a choice for a cautious investor, not a free improvement. Holding fewer stocks made the swings bigger without raising the return in the tuned period, so keep the full number of stocks.

## Fundamentals filters

The same rules, but buying only companies that pass a test on their latest SEC filings as of each month-end (a company without the figure is skipped).

| Strategy | Tuned period | Test period |
|---|---:|---:|
| Current rules | +14.1% a year | +25.8% a year |
| Current rules + only profitable companies | +1.9% a year | +25.5% a year |
| Current rules + only ROE of 15% or more | +3.5% a year | +25.2% a year |
| Current rules + only P/E of 25 or less | +4.6% a year | +20.5% a year |

No filter beat the current rules in both periods. Strong momentum stocks are often young or fast-growing companies with losses or high P/Es, and the filters screen out exactly those. So the report shows P/E, P/B, ROE and growth as context only.

## Year by year

| Year | Current rules | S&P 500 | Difference |
|---|---:|---:|---:|
| 2017 | +3.3% | +3.8% | -0.6% |
| 2018 | -11.7% | -6.2% | -5.4% |
| 2019 | +24.9% | +28.9% | -4.0% |
| 2020 | +66.7% | +16.3% | +50.5% |
| 2021 | +14.4% | +26.9% | -12.5% |
| 2022 | -9.1% | -19.4% | +10.4% |
| 2023 | +11.6% | +24.2% | -12.7% |
| 2024 | +57.9% | +23.3% | +34.6% |
| 2025 | +33.0% | +16.4% | +16.7% |
| 2026 | -0.5% | +10.6% | -11.1% |

## Verdict

Following the current rules returned +18.5% a year against +12.7% for the S&P 500, after costs. The rules beat the index. The worst drop along the way was -43.1%, so expect deep falls and size your money accordingly.

What the tuning found: tight trailing stops (3 × ATR) sold good stocks on normal dips and were the biggest drag; sitting out market downtrends missed the rebounds; and the most erratic stocks (daily range above 5% of the price) hurt more than they helped.

Limits: delisted stocks are missing (which flatters the rules, more so in the US), dividends are ignored on both sides, and a past result does not promise a future one.
