# Which signals work: US stocks

Tested on 4,765 stocks, Nov 2016 to Oct 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| piercing line | up | 27,431 | +0.18% | +0.21% | +0.38% | 48% | +0.8 | no reliable edge |
| bullish harami | up | 143,500 | +0.10% | +0.11% | +0.25% | 47% | +1.2 | no reliable edge |
| bullish marubozu | up | 82,078 | +0.02% | +0.09% | +0.08% | 47% | -1.6 | no reliable edge |
| dragonfly doji | up | 11,961 | -0.04% | +0.03% | +0.13% | 48% | +0.1 | no reliable edge |
| hammer | up | 77,080 | +0.06% | +0.02% | +0.11% | 47% | -0.2 | no reliable edge |
| breakout 52w high | up | 120,483 | -0.05% | +0.02% | +0.08% | 47% | -3.5 | no reliable edge |
| morning star | up | 7,956 | -0.18% | +0.01% | -0.02% | 47% | -1.1 | no reliable edge |
| macd cross up | up | 207,302 | -0.08% | +0.01% | +0.05% | 47% | -1.5 | no reliable edge |
| bullish engulfing | up | 101,735 | +0.05% | -0.04% | -0.02% | 47% | -2.6 | no reliable edge |
| rsi oversold exit | up | 64,350 | -0.07% | -0.11% | -0.10% | 47% | -3.3 | works in reverse |
| inverted hammer | up | 78,224 | -0.04% | -0.17% | -0.12% | 47% | -2.8 | no reliable edge |
| three white soldiers | up | 1,106 | -0.45% | -0.23% | -0.67% | 45% | +0.4 | no reliable edge |
| golden cross | up | 15,362 | -0.04% | -0.26% | -0.39% | 47% | -3.4 | works in reverse |
| volume surge up | up | 88,920 | -1.01% | -1.37% | -1.82% | 44% | -15.9 | works in reverse |
| death cross | down | 15,531 | +0.11% | +0.13% | +0.33% | 52% | +0.6 | no reliable edge |
| bearish engulfing | down | 132,081 | +0.05% | +0.13% | +0.06% | 53% | -0.9 | no reliable edge |
| evening star | down | 9,443 | +0.03% | +0.12% | +0.12% | 53% | -0.2 | no reliable edge |
| hanging man | down | 89,344 | +0.00% | +0.09% | +0.12% | 53% | -0.9 | no reliable edge |
| bearish marubozu | down | 86,682 | +0.07% | +0.09% | +0.10% | 53% | -0.2 | no reliable edge |
| dark cloud cover | down | 34,306 | +0.06% | +0.08% | +0.09% | 53% | -1.6 | no reliable edge |
| three black crows | down | 1,661 | +0.01% | +0.06% | -0.23% | 53% | -1.3 | no reliable edge |
| macd cross down | down | 210,290 | +0.08% | +0.05% | +0.05% | 53% | +0.8 | no reliable edge |
| bearish harami | down | 127,346 | -0.07% | -0.07% | -0.23% | 53% | -4.0 | no reliable edge |
| gravestone doji | down | 12,397 | -0.10% | -0.07% | -0.21% | 52% | -2.8 | no reliable edge |
| shooting star | down | 82,734 | -0.11% | -0.10% | -0.28% | 53% | -1.7 | no reliable edge |
| rsi overbought exit | down | 97,945 | -0.07% | -0.17% | -0.38% | 54% | -6.2 | no reliable edge |
| breakdown 52w low | down | 63,647 | -0.14% | -0.24% | -0.20% | 51% | -6.7 | works as expected |
| volume surge down | down | 81,309 | -0.25% | -0.36% | -0.47% | 53% | -3.9 | works as expected |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
