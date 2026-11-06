# Which signals work: Philippine stocks

Tested on 252 stocks, Sep 2009 to Nov 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| breakout 52w high | up | 3,575 | +0.66% | +0.84% | +1.90% | 48% | +3.6 | works as expected |
| golden cross | up | 740 | +0.30% | +0.19% | +0.01% | 47% | +0.7 | no reliable edge |
| inverted hammer | up | 6,027 | +0.19% | +0.14% | +0.04% | 50% | +0.7 | no reliable edge |
| volume surge up | up | 7,680 | -0.01% | +0.03% | +0.15% | 44% | -0.6 | no reliable edge |
| bullish harami | up | 5,709 | +0.02% | +0.01% | +0.14% | 48% | +0.1 | no reliable edge |
| rsi oversold exit | up | 2,911 | -0.08% | -0.08% | -0.03% | 47% | -2.0 | no reliable edge |
| bullish marubozu | up | 7,943 | -0.26% | -0.22% | -0.13% | 43% | -2.3 | works in reverse |
| bullish engulfing | up | 5,333 | -0.38% | -0.27% | -0.44% | 44% | -2.7 | works in reverse |
| macd cross up | up | 8,644 | -0.18% | -0.27% | -0.27% | 44% | -4.1 | works in reverse |
| piercing line | up | 529 | -0.18% | -0.34% | -0.54% | 47% | -2.0 | no reliable edge |
| hammer | up | 4,765 | -0.48% | -0.62% | -0.79% | 44% | -5.3 | works in reverse |
| dragonfly doji | up | 2,496 | -0.51% | -0.68% | -0.81% | 42% | -5.2 | works in reverse |
| morning star | up | 452 | -0.66% | -1.22% | -0.89% | 36% | -3.1 | works in reverse |
| three white soldiers | up | 77 | -1.62% | -1.66% | -1.95% | 30% | -2.3 | works in reverse |
| gravestone doji | down | 1,403 | +0.38% | +0.71% | +1.12% | 52% | +3.1 | works in reverse |
| rsi overbought exit | down | 4,137 | +0.20% | +0.48% | +0.87% | 52% | +1.2 | no reliable edge |
| evening star | down | 471 | +0.44% | +0.47% | +0.66% | 46% | +1.2 | no reliable edge |
| bearish marubozu | down | 9,924 | +0.32% | +0.33% | +0.27% | 49% | +4.6 | works in reverse |
| shooting star | down | 3,793 | +0.21% | +0.29% | +0.55% | 52% | +1.0 | no reliable edge |
| volume surge down | down | 5,662 | +0.32% | +0.20% | +0.29% | 50% | -0.6 | no reliable edge |
| bearish engulfing | down | 6,713 | +0.09% | +0.15% | +0.11% | 52% | +1.1 | no reliable edge |
| macd cross down | down | 9,206 | +0.05% | +0.12% | +0.03% | 51% | +1.6 | no reliable edge |
| bearish harami | down | 3,440 | -0.04% | +0.03% | +0.02% | 54% | +0.1 | no reliable edge |
| breakdown 52w low | down | 3,147 | -0.08% | +0.03% | +0.22% | 50% | +0.1 | no reliable edge |
| death cross | down | 604 | -0.01% | -0.02% | -0.07% | 54% | -0.0 | no reliable edge |
| dark cloud cover | down | 1,043 | +0.33% | -0.16% | -0.34% | 55% | -0.4 | no reliable edge |
| hanging man | down | 5,975 | -0.36% | -0.24% | -0.11% | 56% | -3.3 | works as expected |
| three black crows | down | 181 | +0.30% | -0.30% | +0.23% | 51% | -0.6 | no reliable edge |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
