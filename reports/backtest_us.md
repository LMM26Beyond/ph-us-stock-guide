# Back-test: United States

Oct 2017 to Oct 2026, starting with $20,000 and up to 40 stocks.

**Current rules.** Each month-end the stocks are scored with only the data known that day. Holdings scoring below 60 are sold. Free slots are filled with the report's buy candidates (score 70+, above the 200-day average, RSI ≤ 75, at most 30% above the 50-day average, average daily range at most 5% of the price) at the next day's open, in equal amounts.

Costs per trade: no commission, 0.003% regulatory fees and 0.05% slippage each way.

| Strategy | Yearly return | Total | Worst drop | Sharpe | Trades | Wins | Avg trade |
|---|---:|---:|---:|---:|---:|---:|---:|
| Current rules | +19.1% | +382.6% | -43.1% | 0.71 | 491 | 42% | +18.8% |
| Old rules (3 × ATR trailing stop, no buys in a downtrend, sell below 50, no range limit) | -0.1% | -0.5% | -42.2% | 0.11 | 1884 | 35% | +0.3% |
| Current rules, smaller amounts in more volatile stocks | +11.3% | +162.4% | -31.3% | 0.61 | 515 | 41% | +17.6% |
| Current rules, half as many stocks | +17.9% | +338.4% | -47.6% | 0.68 | 238 | 45% | +16.9% |
| Current rules + only profitable companies | +12.1% | +178.4% | -44.6% | 0.54 | 519 | 39% | +8.4% |
| Current rules + only ROE of 15% or more | +12.6% | +191.3% | -38.8% | 0.57 | 537 | 40% | +9.2% |
| Current rules + only P/E of 25 or less | +11.3% | +161.9% | -40.6% | 0.54 | 544 | 43% | +7.1% |
| Hold the index | +13.0% | +199.9% | -33.9% | 0.74 | – | – | – |

"Hold the index" is the S&P 500 with no costs and no dividends; the stock prices also exclude dividends, so the comparison is like for like.

## Tuned period and test period

The rule settings were the best of those tried on data up to Dec 2022, and the same settings came out on top in both markets. The later years were not used to pick them, so they are a fairer test, though not a perfectly blind one.

| Period | Current rules | S&P 500 |
|---|---:|---:|
| To Dec 2022 (tuned) | +14.1% a year | +8.0% a year |
| From Jan 2023 (test) | +27.5% a year | +20.2% a year |

## Position size

The current rules put an equal amount in each of up to 40 stocks. Two alternatives:

| Strategy | Yearly return | Worst drop | Tuned period | Test period |
|---|---:|---:|---:|---:|
| Current rules | +19.1% | -43.1% | +14.1% | +27.5% |
| Current rules, smaller amounts in more volatile stocks | +11.3% | -31.3% | +7.4% | +17.4% |
| Current rules, half as many stocks | +17.9% | -47.6% | +10.7% | +29.4% |

"Smaller amounts in more volatile stocks" scales each stock's amount by 2% divided by its average daily range as a share of the price, from half to double the equal amount. It gives smaller drops for a lower return: a choice for a cautious investor, not a free improvement. Holding fewer stocks made the swings bigger without raising the return in the tuned period, so keep the full number of stocks.

## Fundamentals filters

The same rules, but buying only companies that pass a test on their latest SEC filings as of each month-end (a company without the figure is skipped).

| Strategy | Tuned period | Test period |
|---|---:|---:|
| Current rules | +14.1% a year | +27.5% a year |
| Current rules + only profitable companies | +1.9% a year | +28.1% a year |
| Current rules + only ROE of 15% or more | +3.5% a year | +27.0% a year |
| Current rules + only P/E of 25 or less | +4.6% a year | +21.6% a year |

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
| 2026 | +4.2% | +12.8% | -8.6% |

## Verdict

Following the current rules returned +19.1% a year against +13.0% for the S&P 500, after costs. The rules beat the index. The worst drop along the way was -43.1%, so expect deep falls and size your money accordingly.

What the tuning found: tight trailing stops (3 × ATR) sold good stocks on normal dips and were the biggest drag; sitting out market downtrends missed the rebounds; and the most erratic stocks (daily range above 5% of the price) hurt more than they helped.

Limits: delisted stocks are missing (which flatters the rules, more so in the US), dividends are ignored on both sides, and a past result does not promise a future one.
