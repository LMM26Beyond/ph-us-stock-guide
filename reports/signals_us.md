# Which signals work: US stocks

Tested on 4,783 stocks, Nov 2016 to Nov 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| piercing line | up | 27,811 | +0.17% | +0.22% | +0.38% | 48% | +0.8 | no reliable edge |
| bullish marubozu | up | 83,309 | +0.03% | +0.12% | +0.11% | 47% | -1.6 | no reliable edge |
| bullish harami | up | 144,884 | +0.10% | +0.09% | +0.22% | 48% | +1.0 | no reliable edge |
| macd cross up | up | 210,080 | -0.08% | +0.02% | +0.06% | 47% | -1.5 | no reliable edge |
| morning star | up | 8,072 | -0.16% | +0.02% | -0.02% | 47% | -0.9 | no reliable edge |
| dragonfly doji | up | 12,107 | -0.06% | +0.02% | +0.11% | 48% | -0.0 | no reliable edge |
| hammer | up | 77,970 | +0.04% | +0.01% | +0.09% | 47% | -0.3 | no reliable edge |
| breakout 52w high | up | 121,291 | -0.05% | +0.00% | +0.05% | 47% | -3.7 | no reliable edge |
| bullish engulfing | up | 103,123 | +0.05% | -0.02% | -0.01% | 47% | -2.5 | no reliable edge |
| rsi oversold exit | up | 65,698 | -0.07% | -0.10% | -0.09% | 48% | -3.4 | works in reverse |
| inverted hammer | up | 79,015 | -0.05% | -0.19% | -0.14% | 47% | -2.9 | no reliable edge |
| three white soldiers | up | 1,119 | -0.46% | -0.24% | -0.69% | 45% | +0.5 | no reliable edge |
| golden cross | up | 15,461 | -0.04% | -0.28% | -0.42% | 47% | -3.5 | works in reverse |
| volume surge up | up | 89,710 | -1.01% | -1.39% | -1.84% | 44% | -16.1 | works in reverse |
| death cross | down | 15,863 | +0.11% | +0.15% | +0.40% | 52% | +0.6 | no reliable edge |
| bearish engulfing | down | 133,394 | +0.06% | +0.14% | +0.08% | 53% | -0.9 | no reliable edge |
| evening star | down | 9,525 | +0.04% | +0.13% | +0.15% | 52% | -0.2 | no reliable edge |
| dark cloud cover | down | 34,784 | +0.07% | +0.10% | +0.11% | 53% | -1.6 | no reliable edge |
| hanging man | down | 90,370 | +0.01% | +0.10% | +0.14% | 53% | -0.9 | no reliable edge |
| bearish marubozu | down | 87,426 | +0.07% | +0.08% | +0.08% | 53% | -0.3 | no reliable edge |
| macd cross down | down | 212,081 | +0.07% | +0.04% | +0.03% | 53% | +0.6 | no reliable edge |
| three black crows | down | 1,666 | -0.01% | +0.03% | -0.27% | 53% | -1.5 | no reliable edge |
| bearish harami | down | 129,129 | -0.07% | -0.04% | -0.20% | 53% | -4.2 | no reliable edge |
| gravestone doji | down | 12,533 | -0.08% | -0.05% | -0.21% | 52% | -2.7 | no reliable edge |
| shooting star | down | 83,653 | -0.11% | -0.09% | -0.27% | 53% | -1.7 | no reliable edge |
| rsi overbought exit | down | 98,777 | -0.07% | -0.18% | -0.39% | 54% | -6.4 | works as expected |
| breakdown 52w low | down | 64,582 | -0.16% | -0.25% | -0.22% | 51% | -6.8 | works as expected |
| volume surge down | down | 82,080 | -0.26% | -0.38% | -0.48% | 53% | -4.1 | works as expected |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
