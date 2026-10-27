# Which signals work: US stocks

Tested on 4,759 stocks, Nov 2016 to Oct 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| piercing line | up | 27,342 | +0.18% | +0.21% | +0.38% | 48% | +0.8 | no reliable edge |
| bullish harami | up | 143,144 | +0.10% | +0.11% | +0.25% | 47% | +1.3 | no reliable edge |
| bullish marubozu | up | 82,016 | +0.02% | +0.08% | +0.08% | 47% | -1.6 | no reliable edge |
| dragonfly doji | up | 11,932 | -0.04% | +0.03% | +0.13% | 48% | +0.1 | no reliable edge |
| breakout 52w high | up | 120,445 | -0.05% | +0.02% | +0.08% | 47% | -3.4 | no reliable edge |
| hammer | up | 76,884 | +0.06% | +0.02% | +0.11% | 47% | -0.2 | no reliable edge |
| macd cross up | up | 206,946 | -0.08% | +0.01% | +0.05% | 47% | -1.6 | no reliable edge |
| morning star | up | 7,932 | -0.19% | +0.00% | -0.03% | 47% | -1.1 | no reliable edge |
| bullish engulfing | up | 101,439 | +0.05% | -0.04% | -0.03% | 47% | -2.6 | no reliable edge |
| rsi oversold exit | up | 64,025 | -0.07% | -0.11% | -0.12% | 47% | -3.3 | works in reverse |
| inverted hammer | up | 78,032 | -0.04% | -0.17% | -0.12% | 47% | -2.8 | no reliable edge |
| three white soldiers | up | 1,106 | -0.45% | -0.24% | -0.67% | 45% | +0.4 | no reliable edge |
| golden cross | up | 15,342 | -0.04% | -0.27% | -0.38% | 46% | -3.4 | works in reverse |
| volume surge up | up | 88,821 | -1.00% | -1.37% | -1.80% | 44% | -15.8 | works in reverse |
| death cross | down | 15,492 | +0.11% | +0.14% | +0.34% | 52% | +0.7 | no reliable edge |
| bearish engulfing | down | 131,910 | +0.05% | +0.13% | +0.06% | 53% | -1.0 | no reliable edge |
| evening star | down | 9,436 | +0.03% | +0.11% | +0.12% | 53% | -0.2 | no reliable edge |
| bearish marubozu | down | 86,426 | +0.08% | +0.09% | +0.10% | 53% | -0.2 | no reliable edge |
| hanging man | down | 89,288 | +0.00% | +0.09% | +0.12% | 53% | -0.9 | no reliable edge |
| dark cloud cover | down | 34,276 | +0.06% | +0.08% | +0.08% | 53% | -1.6 | no reliable edge |
| three black crows | down | 1,659 | +0.01% | +0.07% | -0.21% | 53% | -1.3 | no reliable edge |
| macd cross down | down | 210,042 | +0.08% | +0.06% | +0.06% | 53% | +0.8 | no reliable edge |
| bearish harami | down | 127,286 | -0.08% | -0.07% | -0.23% | 53% | -4.0 | no reliable edge |
| gravestone doji | down | 12,386 | -0.10% | -0.07% | -0.20% | 52% | -2.7 | no reliable edge |
| shooting star | down | 82,658 | -0.11% | -0.10% | -0.27% | 53% | -1.6 | no reliable edge |
| rsi overbought exit | down | 97,913 | -0.07% | -0.17% | -0.38% | 54% | -6.1 | no reliable edge |
| breakdown 52w low | down | 63,426 | -0.14% | -0.23% | -0.19% | 51% | -6.6 | works as expected |
| volume surge down | down | 81,206 | -0.25% | -0.36% | -0.46% | 53% | -3.9 | works as expected |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
