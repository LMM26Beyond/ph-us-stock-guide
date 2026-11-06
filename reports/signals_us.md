# Which signals work: US stocks

Tested on 4,769 stocks, Nov 2016 to Nov 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| piercing line | up | 27,528 | +0.18% | +0.22% | +0.40% | 48% | +0.8 | no reliable edge |
| bullish harami | up | 143,785 | +0.10% | +0.10% | +0.24% | 47% | +1.1 | no reliable edge |
| bullish marubozu | up | 82,266 | +0.03% | +0.09% | +0.09% | 47% | -1.5 | no reliable edge |
| macd cross up | up | 208,301 | -0.07% | +0.02% | +0.07% | 47% | -1.4 | no reliable edge |
| dragonfly doji | up | 12,003 | -0.05% | +0.02% | +0.12% | 48% | +0.0 | no reliable edge |
| morning star | up | 7,975 | -0.18% | +0.02% | -0.02% | 47% | -1.0 | no reliable edge |
| hammer | up | 77,386 | +0.05% | +0.02% | +0.11% | 47% | -0.2 | no reliable edge |
| breakout 52w high | up | 120,609 | -0.05% | +0.01% | +0.06% | 47% | -3.6 | no reliable edge |
| bullish engulfing | up | 102,158 | +0.05% | -0.03% | -0.00% | 47% | -2.6 | no reliable edge |
| rsi oversold exit | up | 64,725 | -0.07% | -0.10% | -0.07% | 47% | -3.3 | works in reverse |
| inverted hammer | up | 78,416 | -0.04% | -0.18% | -0.13% | 47% | -2.8 | no reliable edge |
| three white soldiers | up | 1,111 | -0.43% | -0.21% | -0.67% | 45% | +0.6 | no reliable edge |
| golden cross | up | 15,387 | -0.04% | -0.27% | -0.40% | 47% | -3.4 | works in reverse |
| volume surge up | up | 89,084 | -1.01% | -1.38% | -1.83% | 44% | -16.0 | works in reverse |
| death cross | down | 15,603 | +0.11% | +0.14% | +0.36% | 52% | +0.6 | no reliable edge |
| bearish engulfing | down | 132,350 | +0.05% | +0.13% | +0.06% | 53% | -0.9 | no reliable edge |
| evening star | down | 9,462 | +0.04% | +0.11% | +0.11% | 53% | -0.2 | no reliable edge |
| hanging man | down | 89,571 | +0.01% | +0.09% | +0.12% | 53% | -1.0 | no reliable edge |
| bearish marubozu | down | 86,829 | +0.07% | +0.09% | +0.09% | 53% | -0.2 | no reliable edge |
| dark cloud cover | down | 34,394 | +0.07% | +0.08% | +0.09% | 53% | -1.6 | no reliable edge |
| three black crows | down | 1,662 | +0.00% | +0.05% | -0.26% | 53% | -1.4 | no reliable edge |
| macd cross down | down | 210,706 | +0.08% | +0.05% | +0.04% | 53% | +0.6 | no reliable edge |
| bearish harami | down | 127,765 | -0.07% | -0.06% | -0.23% | 53% | -4.0 | no reliable edge |
| gravestone doji | down | 12,430 | -0.09% | -0.07% | -0.22% | 52% | -2.7 | no reliable edge |
| shooting star | down | 82,963 | -0.11% | -0.09% | -0.28% | 53% | -1.6 | no reliable edge |
| rsi overbought exit | down | 98,059 | -0.07% | -0.17% | -0.40% | 54% | -6.3 | no reliable edge |
| breakdown 52w low | down | 63,864 | -0.15% | -0.25% | -0.19% | 51% | -6.7 | works as expected |
| volume surge down | down | 81,457 | -0.26% | -0.37% | -0.48% | 53% | -4.1 | works as expected |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
