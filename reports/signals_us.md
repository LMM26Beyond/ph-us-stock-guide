# Which signals work: US stocks

Tested on 4,767 stocks, Nov 2016 to Nov 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| piercing line | up | 27,474 | +0.18% | +0.22% | +0.39% | 48% | +0.9 | no reliable edge |
| bullish harami | up | 143,679 | +0.10% | +0.10% | +0.25% | 47% | +1.2 | no reliable edge |
| bullish marubozu | up | 82,151 | +0.03% | +0.09% | +0.08% | 47% | -1.5 | no reliable edge |
| dragonfly doji | up | 11,980 | -0.05% | +0.03% | +0.12% | 48% | +0.1 | no reliable edge |
| breakout 52w high | up | 120,558 | -0.05% | +0.02% | +0.07% | 47% | -3.6 | no reliable edge |
| macd cross up | up | 207,897 | -0.08% | +0.02% | +0.07% | 47% | -1.5 | no reliable edge |
| hammer | up | 77,234 | +0.05% | +0.02% | +0.11% | 47% | -0.2 | no reliable edge |
| morning star | up | 7,964 | -0.18% | +0.01% | -0.02% | 47% | -1.1 | no reliable edge |
| bullish engulfing | up | 101,906 | +0.05% | -0.03% | -0.01% | 47% | -2.5 | no reliable edge |
| rsi oversold exit | up | 64,541 | -0.07% | -0.11% | -0.08% | 47% | -3.3 | works in reverse |
| inverted hammer | up | 78,366 | -0.04% | -0.17% | -0.12% | 47% | -2.7 | no reliable edge |
| three white soldiers | up | 1,109 | -0.44% | -0.22% | -0.66% | 45% | +0.5 | no reliable edge |
| golden cross | up | 15,380 | -0.04% | -0.26% | -0.39% | 47% | -3.4 | works in reverse |
| volume surge up | up | 89,028 | -1.01% | -1.38% | -1.83% | 44% | -15.9 | works in reverse |
| death cross | down | 15,574 | +0.11% | +0.13% | +0.35% | 52% | +0.6 | no reliable edge |
| bearish engulfing | down | 132,294 | +0.05% | +0.13% | +0.07% | 53% | -0.9 | no reliable edge |
| evening star | down | 9,460 | +0.04% | +0.12% | +0.12% | 53% | -0.2 | no reliable edge |
| bearish marubozu | down | 86,787 | +0.07% | +0.09% | +0.10% | 53% | -0.2 | no reliable edge |
| hanging man | down | 89,484 | +0.01% | +0.09% | +0.12% | 53% | -0.9 | no reliable edge |
| dark cloud cover | down | 34,366 | +0.06% | +0.08% | +0.09% | 53% | -1.6 | no reliable edge |
| three black crows | down | 1,662 | +0.00% | +0.06% | -0.25% | 53% | -1.4 | no reliable edge |
| macd cross down | down | 210,516 | +0.08% | +0.05% | +0.05% | 53% | +0.8 | no reliable edge |
| bearish harami | down | 127,560 | -0.07% | -0.07% | -0.23% | 53% | -4.0 | no reliable edge |
| gravestone doji | down | 12,416 | -0.09% | -0.07% | -0.22% | 52% | -2.7 | no reliable edge |
| shooting star | down | 82,874 | -0.11% | -0.09% | -0.27% | 53% | -1.6 | no reliable edge |
| rsi overbought exit | down | 98,031 | -0.07% | -0.17% | -0.39% | 54% | -6.2 | no reliable edge |
| breakdown 52w low | down | 63,794 | -0.14% | -0.24% | -0.18% | 51% | -6.7 | works as expected |
| volume surge down | down | 81,400 | -0.25% | -0.36% | -0.47% | 53% | -4.0 | works as expected |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
