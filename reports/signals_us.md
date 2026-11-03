# Which signals work: US stocks

Tested on 4,766 stocks, Nov 2016 to Nov 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| piercing line | up | 27,459 | +0.18% | +0.21% | +0.39% | 48% | +0.8 | no reliable edge |
| bullish harami | up | 143,664 | +0.10% | +0.10% | +0.25% | 47% | +1.2 | no reliable edge |
| bullish marubozu | up | 82,135 | +0.02% | +0.09% | +0.09% | 47% | -1.5 | no reliable edge |
| dragonfly doji | up | 11,976 | -0.04% | +0.04% | +0.12% | 48% | +0.1 | no reliable edge |
| hammer | up | 77,190 | +0.06% | +0.02% | +0.11% | 47% | -0.2 | no reliable edge |
| breakout 52w high | up | 120,545 | -0.05% | +0.02% | +0.07% | 47% | -3.6 | no reliable edge |
| macd cross up | up | 207,764 | -0.08% | +0.01% | +0.06% | 47% | -1.5 | no reliable edge |
| morning star | up | 7,964 | -0.19% | +0.01% | -0.02% | 47% | -1.1 | no reliable edge |
| bullish engulfing | up | 101,871 | +0.05% | -0.03% | -0.01% | 47% | -2.5 | no reliable edge |
| rsi oversold exit | up | 64,517 | -0.07% | -0.11% | -0.09% | 47% | -3.3 | works in reverse |
| inverted hammer | up | 78,320 | -0.04% | -0.18% | -0.12% | 47% | -2.8 | no reliable edge |
| three white soldiers | up | 1,109 | -0.44% | -0.22% | -0.66% | 45% | +0.5 | no reliable edge |
| golden cross | up | 15,373 | -0.04% | -0.26% | -0.39% | 47% | -3.4 | works in reverse |
| volume surge up | up | 89,010 | -1.01% | -1.38% | -1.83% | 44% | -15.9 | works in reverse |
| death cross | down | 15,557 | +0.11% | +0.13% | +0.35% | 52% | +0.6 | no reliable edge |
| bearish engulfing | down | 132,252 | +0.05% | +0.13% | +0.07% | 53% | -0.9 | no reliable edge |
| evening star | down | 9,451 | +0.03% | +0.11% | +0.12% | 53% | -0.2 | no reliable edge |
| hanging man | down | 89,422 | +0.01% | +0.09% | +0.12% | 53% | -0.9 | no reliable edge |
| bearish marubozu | down | 86,747 | +0.07% | +0.09% | +0.09% | 53% | -0.2 | no reliable edge |
| dark cloud cover | down | 34,354 | +0.06% | +0.08% | +0.09% | 53% | -1.6 | no reliable edge |
| three black crows | down | 1,662 | +0.00% | +0.05% | -0.25% | 53% | -1.4 | no reliable edge |
| macd cross down | down | 210,394 | +0.08% | +0.05% | +0.05% | 53% | +0.8 | no reliable edge |
| bearish harami | down | 127,456 | -0.07% | -0.07% | -0.23% | 53% | -4.0 | no reliable edge |
| gravestone doji | down | 12,407 | -0.10% | -0.07% | -0.21% | 52% | -2.7 | no reliable edge |
| shooting star | down | 82,821 | -0.11% | -0.10% | -0.27% | 53% | -1.6 | no reliable edge |
| rsi overbought exit | down | 98,001 | -0.07% | -0.17% | -0.39% | 54% | -6.2 | no reliable edge |
| breakdown 52w low | down | 63,714 | -0.14% | -0.24% | -0.20% | 51% | -6.7 | works as expected |
| volume surge down | down | 81,362 | -0.25% | -0.36% | -0.47% | 53% | -4.0 | works as expected |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
