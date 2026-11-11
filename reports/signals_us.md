# Which signals work: US stocks

Tested on 4,775 stocks, Nov 2016 to Nov 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| piercing line | up | 27,576 | +0.18% | +0.22% | +0.40% | 48% | +0.8 | no reliable edge |
| bullish harami | up | 143,955 | +0.10% | +0.10% | +0.24% | 47% | +1.1 | no reliable edge |
| bullish marubozu | up | 82,351 | +0.03% | +0.09% | +0.09% | 47% | -1.5 | no reliable edge |
| macd cross up | up | 208,622 | -0.07% | +0.03% | +0.08% | 47% | -1.4 | no reliable edge |
| morning star | up | 7,985 | -0.18% | +0.02% | -0.03% | 47% | -1.0 | no reliable edge |
| dragonfly doji | up | 12,018 | -0.05% | +0.02% | +0.12% | 48% | +0.0 | no reliable edge |
| hammer | up | 77,492 | +0.05% | +0.02% | +0.12% | 47% | -0.2 | no reliable edge |
| breakout 52w high | up | 120,699 | -0.05% | +0.02% | +0.05% | 47% | -3.6 | no reliable edge |
| bullish engulfing | up | 102,327 | +0.05% | -0.03% | +0.00% | 47% | -2.6 | no reliable edge |
| rsi oversold exit | up | 64,815 | -0.07% | -0.10% | -0.06% | 47% | -3.3 | works in reverse |
| inverted hammer | up | 78,549 | -0.04% | -0.18% | -0.12% | 47% | -2.8 | no reliable edge |
| three white soldiers | up | 1,111 | -0.43% | -0.21% | -0.67% | 45% | +0.6 | no reliable edge |
| golden cross | up | 15,408 | -0.04% | -0.27% | -0.40% | 47% | -3.4 | works in reverse |
| volume surge up | up | 89,186 | -1.01% | -1.39% | -1.84% | 44% | -16.0 | works in reverse |
| death cross | down | 15,642 | +0.11% | +0.14% | +0.37% | 52% | +0.7 | no reliable edge |
| bearish engulfing | down | 132,555 | +0.06% | +0.13% | +0.07% | 53% | -0.9 | no reliable edge |
| evening star | down | 9,477 | +0.04% | +0.12% | +0.12% | 53% | -0.2 | no reliable edge |
| hanging man | down | 89,712 | +0.01% | +0.10% | +0.13% | 53% | -0.9 | no reliable edge |
| dark cloud cover | down | 34,463 | +0.06% | +0.09% | +0.10% | 53% | -1.5 | no reliable edge |
| bearish marubozu | down | 86,981 | +0.07% | +0.08% | +0.09% | 53% | -0.3 | no reliable edge |
| three black crows | down | 1,663 | +0.00% | +0.05% | -0.26% | 53% | -1.4 | no reliable edge |
| macd cross down | down | 210,973 | +0.07% | +0.04% | +0.04% | 53% | +0.6 | no reliable edge |
| gravestone doji | down | 12,448 | -0.09% | -0.06% | -0.22% | 52% | -2.7 | no reliable edge |
| bearish harami | down | 127,925 | -0.07% | -0.07% | -0.23% | 53% | -4.1 | no reliable edge |
| shooting star | down | 83,076 | -0.11% | -0.09% | -0.27% | 53% | -1.6 | no reliable edge |
| rsi overbought exit | down | 98,150 | -0.07% | -0.18% | -0.41% | 54% | -6.3 | no reliable edge |
| breakdown 52w low | down | 63,985 | -0.16% | -0.26% | -0.19% | 51% | -6.7 | works as expected |
| volume surge down | down | 81,522 | -0.26% | -0.37% | -0.48% | 53% | -4.1 | works as expected |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
