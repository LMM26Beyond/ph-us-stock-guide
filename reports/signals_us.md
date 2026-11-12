# Which signals work: US stocks

Tested on 4,776 stocks, Nov 2016 to Nov 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| piercing line | up | 27,592 | +0.18% | +0.22% | +0.40% | 48% | +0.8 | no reliable edge |
| bullish harami | up | 143,997 | +0.10% | +0.10% | +0.24% | 47% | +1.2 | no reliable edge |
| bullish marubozu | up | 82,396 | +0.03% | +0.09% | +0.09% | 47% | -1.5 | no reliable edge |
| macd cross up | up | 208,711 | -0.07% | +0.03% | +0.08% | 47% | -1.4 | no reliable edge |
| morning star | up | 7,987 | -0.18% | +0.02% | -0.03% | 47% | -1.0 | no reliable edge |
| dragonfly doji | up | 12,027 | -0.05% | +0.02% | +0.12% | 48% | +0.0 | no reliable edge |
| hammer | up | 77,534 | +0.05% | +0.02% | +0.12% | 47% | -0.2 | no reliable edge |
| breakout 52w high | up | 120,737 | -0.05% | +0.01% | +0.05% | 47% | -3.6 | no reliable edge |
| bullish engulfing | up | 102,387 | +0.05% | -0.03% | +0.00% | 47% | -2.6 | no reliable edge |
| rsi oversold exit | up | 64,848 | -0.07% | -0.10% | -0.06% | 47% | -3.3 | works in reverse |
| inverted hammer | up | 78,601 | -0.04% | -0.18% | -0.12% | 47% | -2.8 | no reliable edge |
| three white soldiers | up | 1,112 | -0.43% | -0.21% | -0.66% | 45% | +0.6 | no reliable edge |
| golden cross | up | 15,411 | -0.04% | -0.27% | -0.40% | 47% | -3.4 | works in reverse |
| volume surge up | up | 89,209 | -1.01% | -1.39% | -1.84% | 44% | -16.0 | works in reverse |
| death cross | down | 15,667 | +0.11% | +0.14% | +0.37% | 52% | +0.6 | no reliable edge |
| bearish engulfing | down | 132,640 | +0.06% | +0.13% | +0.07% | 53% | -0.9 | no reliable edge |
| evening star | down | 9,487 | +0.04% | +0.12% | +0.13% | 53% | -0.2 | no reliable edge |
| hanging man | down | 89,807 | +0.01% | +0.10% | +0.13% | 53% | -0.9 | no reliable edge |
| dark cloud cover | down | 34,486 | +0.06% | +0.09% | +0.09% | 53% | -1.5 | no reliable edge |
| bearish marubozu | down | 87,057 | +0.07% | +0.08% | +0.09% | 53% | -0.3 | no reliable edge |
| three black crows | down | 1,663 | +0.00% | +0.05% | -0.26% | 53% | -1.4 | no reliable edge |
| macd cross down | down | 211,167 | +0.07% | +0.04% | +0.04% | 53% | +0.6 | no reliable edge |
| gravestone doji | down | 12,454 | -0.09% | -0.06% | -0.22% | 52% | -2.8 | no reliable edge |
| bearish harami | down | 127,983 | -0.07% | -0.07% | -0.23% | 53% | -4.1 | no reliable edge |
| shooting star | down | 83,117 | -0.11% | -0.09% | -0.28% | 53% | -1.6 | no reliable edge |
| rsi overbought exit | down | 98,209 | -0.07% | -0.18% | -0.41% | 54% | -6.3 | no reliable edge |
| breakdown 52w low | down | 64,165 | -0.16% | -0.26% | -0.19% | 51% | -6.8 | works as expected |
| volume surge down | down | 81,590 | -0.26% | -0.37% | -0.48% | 53% | -4.1 | works as expected |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
