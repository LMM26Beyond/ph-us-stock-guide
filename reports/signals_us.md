# Which signals work: US stocks

Tested on 4,778 stocks, Nov 2016 to Nov 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| piercing line | up | 27,731 | +0.17% | +0.22% | +0.39% | 48% | +0.8 | no reliable edge |
| bullish marubozu | up | 82,911 | +0.03% | +0.11% | +0.11% | 47% | -1.5 | no reliable edge |
| bullish harami | up | 144,556 | +0.10% | +0.09% | +0.22% | 47% | +1.1 | no reliable edge |
| macd cross up | up | 209,359 | -0.07% | +0.03% | +0.08% | 47% | -1.4 | no reliable edge |
| morning star | up | 8,036 | -0.16% | +0.02% | -0.01% | 47% | -1.0 | no reliable edge |
| dragonfly doji | up | 12,068 | -0.06% | +0.01% | +0.11% | 48% | -0.1 | no reliable edge |
| breakout 52w high | up | 120,980 | -0.05% | +0.01% | +0.05% | 47% | -3.6 | no reliable edge |
| hammer | up | 77,728 | +0.04% | +0.00% | +0.10% | 47% | -0.4 | no reliable edge |
| bullish engulfing | up | 102,779 | +0.05% | -0.02% | -0.01% | 47% | -2.5 | no reliable edge |
| rsi oversold exit | up | 65,360 | -0.07% | -0.09% | -0.06% | 48% | -3.3 | works in reverse |
| inverted hammer | up | 78,837 | -0.05% | -0.19% | -0.13% | 47% | -2.9 | no reliable edge |
| three white soldiers | up | 1,114 | -0.44% | -0.22% | -0.67% | 45% | +0.6 | no reliable edge |
| golden cross | up | 15,431 | -0.04% | -0.28% | -0.42% | 47% | -3.5 | works in reverse |
| volume surge up | up | 89,405 | -1.02% | -1.39% | -1.84% | 44% | -16.1 | works in reverse |
| bearish engulfing | down | 133,027 | +0.06% | +0.14% | +0.07% | 53% | -0.9 | no reliable edge |
| death cross | down | 15,760 | +0.10% | +0.14% | +0.38% | 52% | +0.6 | no reliable edge |
| evening star | down | 9,511 | +0.04% | +0.13% | +0.15% | 53% | -0.2 | no reliable edge |
| dark cloud cover | down | 34,709 | +0.08% | +0.10% | +0.11% | 53% | -1.6 | no reliable edge |
| hanging man | down | 89,990 | +0.01% | +0.09% | +0.13% | 53% | -0.9 | no reliable edge |
| bearish marubozu | down | 87,286 | +0.07% | +0.08% | +0.08% | 53% | -0.3 | no reliable edge |
| three black crows | down | 1,665 | +0.00% | +0.04% | -0.27% | 53% | -1.4 | no reliable edge |
| macd cross down | down | 211,566 | +0.07% | +0.04% | +0.03% | 53% | +0.5 | no reliable edge |
| gravestone doji | down | 12,485 | -0.08% | -0.05% | -0.21% | 52% | -2.7 | no reliable edge |
| bearish harami | down | 128,281 | -0.07% | -0.07% | -0.23% | 53% | -4.1 | no reliable edge |
| shooting star | down | 83,370 | -0.10% | -0.09% | -0.27% | 53% | -1.7 | no reliable edge |
| rsi overbought exit | down | 98,388 | -0.08% | -0.18% | -0.41% | 54% | -6.4 | no reliable edge |
| breakdown 52w low | down | 64,367 | -0.17% | -0.26% | -0.20% | 51% | -6.8 | works as expected |
| volume surge down | down | 81,775 | -0.26% | -0.38% | -0.49% | 53% | -4.1 | works as expected |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
