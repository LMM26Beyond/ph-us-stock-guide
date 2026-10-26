# Back-test: Philippines (PSE)

Sep 2014 to Oct 2026, starting with ₱1,000,000 and up to 10 stocks.

**Current rules.** Each month-end the stocks are scored with only the data known that day. Holdings scoring below 60 are sold. Free slots are filled with the report's buy candidates (score 70+, above the 200-day average, RSI ≤ 75, at most 30% above the 50-day average, average daily range at most 5% of the price) at the next day's open, in equal amounts.

Costs per trade: 0.25% commission (min ₱20) + 12% VAT, 0.015% PSE and SCCP fees, 0.6% sales tax on sells, and 0.2% slippage each way, about 1.3% for a round trip. Shares are bought in whole board lots.

| Strategy | Yearly return | Total | Worst drop | Sharpe | Trades | Wins | Avg trade |
|---|---:|---:|---:|---:|---:|---:|---:|
| Current rules | +7.0% | +127.4% | -45.7% | 0.43 | 215 | 33% | +4.1% |
| Old rules (3 × ATR trailing stop, no buys in a downtrend, sell below 50, no range limit) | -1.1% | -12.6% | -47.4% | 0.00 | 486 | 32% | -0.5% |
| Current rules, smaller amounts in more volatile stocks | +5.0% | +80.1% | -33.9% | 0.38 | 222 | 35% | +3.8% |
| Current rules, half as many stocks | +0.1% | +1.5% | -59.6% | 0.14 | 109 | 35% | +1.1% |
| Hold the index | -1.5% | -16.7% | -47.9% | -0.00 | – | – | – |

"Hold the index" is the PSEi with no costs and no dividends; the stock prices also exclude dividends, so the comparison is like for like.

## Tuned period and test period

The rule settings were the best of those tried on data up to Dec 2022, and the same settings came out on top in both markets. The later years were not used to pick them, so they are a fairer test, though not a perfectly blind one.

| Period | Current rules | PSEi |
|---|---:|---:|
| To Dec 2022 (tuned) | +5.0% a year | -1.8% a year |
| From Jan 2023 (test) | +11.0% a year | -0.8% a year |

## Position size

The current rules put an equal amount in each of up to 10 stocks. Two alternatives:

| Strategy | Yearly return | Worst drop | Tuned period | Test period |
|---|---:|---:|---:|---:|
| Current rules | +7.0% | -45.7% | +5.0% | +11.0% |
| Current rules, smaller amounts in more volatile stocks | +5.0% | -33.9% | +3.1% | +9.1% |
| Current rules, half as many stocks | +0.1% | -59.6% | -5.8% | +14.2% |

"Smaller amounts in more volatile stocks" scales each stock's amount by 2% divided by its average daily range as a share of the price, from half to double the equal amount. It gives smaller drops for a lower return: a choice for a cautious investor, not a free improvement. Holding fewer stocks made the swings bigger without raising the return in the tuned period, so keep the full number of stocks.

## Year by year

| Year | Current rules | PSEi | Difference |
|---|---:|---:|---:|
| 2014 | +4.3% | -0.6% | +4.9% |
| 2015 | -7.5% | -3.0% | -4.5% |
| 2016 | +12.0% | -0.4% | +12.4% |
| 2017 | +57.7% | +15.5% | +42.2% |
| 2018 | -22.3% | -14.6% | -7.7% |
| 2019 | -1.9% | +5.3% | -7.2% |
| 2020 | +17.8% | -8.0% | +25.8% |
| 2021 | +28.2% | +0.3% | +27.9% |
| 2022 | -23.5% | -6.7% | -16.8% |
| 2023 | -4.0% | +1.7% | -5.7% |
| 2024 | +41.8% | +2.8% | +39.0% |
| 2025 | +9.8% | -4.4% | +14.2% |
| 2026 | +1.4% | -3.0% | +4.4% |

## Verdict

Following the current rules returned +7.0% a year against -1.5% for the PSEi, after costs. The rules beat the index. The worst drop along the way was -45.7%, so expect deep falls and size your money accordingly.

What the tuning found: tight trailing stops (3 × ATR) sold good stocks on normal dips and were the biggest drag; sitting out market downtrends missed the rebounds; and the most erratic stocks (daily range above 5% of the price) hurt more than they helped.

Limits: delisted stocks are missing (which flatters the rules, more so in the US), dividends are ignored on both sides, and a past result does not promise a future one.
