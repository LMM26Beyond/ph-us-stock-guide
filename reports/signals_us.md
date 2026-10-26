# Which signals work: US stocks

Tested on 4,757 stocks, Nov 2016 to Oct 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| piercing line | up | 27,307 | +0.18% | +0.21% | +0.37% | 48% | +0.8 | no reliable edge |
| bullish harami | up | 143,018 | +0.10% | +0.11% | +0.26% | 47% | +1.3 | no reliable edge |
| bullish marubozu | up | 81,946 | +0.02% | +0.08% | +0.08% | 47% | -1.6 | no reliable edge |
| dragonfly doji | up | 11,914 | -0.04% | +0.03% | +0.13% | 48% | +0.1 | no reliable edge |
| hammer | up | 76,769 | +0.06% | +0.02% | +0.11% | 47% | -0.2 | no reliable edge |
| breakout 52w high | up | 120,377 | -0.05% | +0.02% | +0.08% | 47% | -3.4 | no reliable edge |
| macd cross up | up | 206,783 | -0.08% | +0.01% | +0.05% | 47% | -1.6 | no reliable edge |
| morning star | up | 7,926 | -0.19% | +0.00% | -0.02% | 47% | -1.1 | no reliable edge |
| bullish engulfing | up | 101,273 | +0.05% | -0.04% | -0.04% | 47% | -2.6 | no reliable edge |
| rsi oversold exit | up | 63,917 | -0.07% | -0.11% | -0.12% | 47% | -3.3 | works in reverse |
| inverted hammer | up | 77,951 | -0.04% | -0.18% | -0.12% | 47% | -2.8 | no reliable edge |
| three white soldiers | up | 1,105 | -0.45% | -0.23% | -0.68% | 45% | +0.5 | no reliable edge |
| golden cross | up | 15,327 | -0.04% | -0.26% | -0.38% | 47% | -3.4 | works in reverse |
| volume surge up | up | 88,761 | -1.00% | -1.36% | -1.80% | 44% | -15.8 | works in reverse |
| death cross | down | 15,472 | +0.11% | +0.14% | +0.35% | 52% | +0.7 | no reliable edge |
| bearish engulfing | down | 131,786 | +0.05% | +0.13% | +0.06% | 53% | -1.0 | no reliable edge |
| evening star | down | 9,431 | +0.03% | +0.11% | +0.12% | 53% | -0.3 | no reliable edge |
| bearish marubozu | down | 86,359 | +0.08% | +0.09% | +0.09% | 53% | -0.2 | no reliable edge |
| hanging man | down | 89,200 | +0.00% | +0.09% | +0.12% | 53% | -0.9 | no reliable edge |
| dark cloud cover | down | 34,239 | +0.06% | +0.07% | +0.08% | 53% | -1.7 | no reliable edge |
| three black crows | down | 1,658 | -0.00% | +0.06% | -0.22% | 53% | -1.3 | no reliable edge |
| macd cross down | down | 209,865 | +0.08% | +0.06% | +0.06% | 53% | +0.8 | no reliable edge |
| gravestone doji | down | 12,379 | -0.10% | -0.07% | -0.20% | 52% | -2.7 | no reliable edge |
| bearish harami | down | 127,167 | -0.08% | -0.07% | -0.23% | 53% | -4.0 | no reliable edge |
| shooting star | down | 82,591 | -0.11% | -0.10% | -0.27% | 53% | -1.6 | no reliable edge |
| rsi overbought exit | down | 97,851 | -0.07% | -0.17% | -0.38% | 54% | -6.1 | no reliable edge |
| breakdown 52w low | down | 63,352 | -0.14% | -0.23% | -0.19% | 51% | -6.6 | works as expected |
| volume surge down | down | 81,152 | -0.25% | -0.36% | -0.46% | 53% | -3.9 | works as expected |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
