# Back-test: United States

Oct 2017 to Oct 2026, starting with $20,000 and up to 40 stocks.

**Current rules.** Each month-end the stocks are scored with only the data known that day. Holdings scoring below 60 are sold. Free slots are filled with the report's buy candidates (score 70+, above the 200-day average, RSI ≤ 75, at most 30% above the 50-day average, average daily range at most 5% of the price) at the next day's open, in equal amounts.

Costs per trade: no commission, 0.003% regulatory fees and 0.05% slippage each way.

| Strategy | Yearly return | Total | Worst drop | Sharpe | Trades | Wins | Avg trade |
|---|---:|---:|---:|---:|---:|---:|---:|
| Current rules | +18.9% | +373.7% | -43.1% | 0.71 | 491 | 42% | +18.8% |
| Old rules (3 × ATR trailing stop, no buys in a downtrend, sell below 50, no range limit) | -0.2% | -1.5% | -42.5% | 0.10 | 1890 | 35% | +0.3% |
| Current rules + only profitable companies | +11.2% | +159.7% | -46.3% | 0.51 | 513 | 39% | +8.8% |
| Current rules + only ROE of 15% or more | +12.3% | +182.3% | -38.8% | 0.56 | 537 | 40% | +9.2% |
| Current rules + only P/E of 25 or less | +11.1% | +156.5% | -40.6% | 0.54 | 544 | 43% | +7.1% |
| Hold the index | +12.9% | +196.0% | -33.9% | 0.74 | – | – | – |

"Hold the index" is the S&P 500 with no costs and no dividends; the stock prices also exclude dividends, so the comparison is like for like.

## Tuned period and test period

The rule settings were the best of those tried on data up to Dec 2022, and the same settings came out on top in both markets. The later years were not used to pick them, so they are a fairer test, though not a perfectly blind one.

| Period | Current rules | S&P 500 |
|---|---:|---:|
| To Dec 2022 (tuned) | +14.1% a year | +8.0% a year |
| From Jan 2023 (test) | +26.9% a year | +19.9% a year |

## Fundamentals filters

The same rules, but buying only companies that pass a test on their latest SEC filings as of each month-end (a company without the figure is skipped).

| Strategy | Tuned period | Test period |
|---|---:|---:|
| Current rules | +14.1% a year | +26.9% a year |
| Current rules + only profitable companies | +1.6% a year | +26.5% a year |
| Current rules + only ROE of 15% or more | +3.5% a year | +26.1% a year |
| Current rules + only P/E of 25 or less | +4.6% a year | +21.0% a year |

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
| 2026 | +2.3% | +11.4% | -9.1% |

## Verdict

Following the current rules returned +18.9% a year against +12.9% for the S&P 500, after costs. The rules beat the index. The worst drop along the way was -43.1%, so expect deep falls and size your money accordingly.

What the tuning found: tight trailing stops (3 × ATR) sold good stocks on normal dips and were the biggest drag; sitting out market downtrends missed the rebounds; and the most erratic stocks (daily range above 5% of the price) hurt more than they helped.

Limits: delisted stocks are missing (which flatters the rules, more so in the US), dividends are ignored on both sides, and a past result does not promise a future one.
