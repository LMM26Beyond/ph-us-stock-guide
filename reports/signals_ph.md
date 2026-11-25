# Which signals work: Philippine stocks

Tested on 253 stocks, Sep 2009 to Nov 2026, liquid stocks only. **Excess** is the stock's return minus the market index's over the same days, compared with an ordinary day. **Right way** is how often the stock beat (bullish) or trailed (bearish) the index over the next 10 trading days; a coin flip is 50%.

A signal is called *working* only if it appeared at least 30 times, its result is statistically clear (|t| ≥ 2, counting each day once), and it points the same way in both halves of the history.

| Signal | Expects | Count | Excess 5d | Excess 10d | Excess 20d | Right way 10d | t | Verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| breakout 52w high | up | 3,580 | +0.66% | +0.84% | +1.90% | 48% | +3.6 | works as expected |
| golden cross | up | 744 | +0.32% | +0.22% | +0.06% | 48% | +0.7 | no reliable edge |
| inverted hammer | up | 6,052 | +0.18% | +0.13% | +0.03% | 50% | +0.7 | no reliable edge |
| volume surge up | up | 7,727 | -0.01% | +0.04% | +0.14% | 44% | -0.6 | no reliable edge |
| bullish harami | up | 5,733 | +0.02% | +0.02% | +0.13% | 48% | +0.1 | no reliable edge |
| rsi oversold exit | up | 2,941 | -0.08% | -0.07% | -0.02% | 47% | -2.0 | no reliable edge |
| bullish marubozu | up | 8,006 | -0.26% | -0.22% | -0.13% | 43% | -2.3 | works in reverse |
| bullish engulfing | up | 5,365 | -0.38% | -0.27% | -0.45% | 44% | -2.7 | works in reverse |
| macd cross up | up | 8,706 | -0.18% | -0.28% | -0.28% | 44% | -4.2 | works in reverse |
| piercing line | up | 530 | -0.18% | -0.34% | -0.55% | 47% | -2.0 | no reliable edge |
| hammer | up | 4,804 | -0.48% | -0.61% | -0.78% | 44% | -5.2 | works in reverse |
| dragonfly doji | up | 2,549 | -0.48% | -0.66% | -0.77% | 42% | -5.3 | works in reverse |
| morning star | up | 457 | -0.65% | -1.21% | -0.78% | 36% | -3.1 | works in reverse |
| three white soldiers | up | 77 | -1.62% | -1.66% | -1.96% | 30% | -2.3 | works in reverse |
| gravestone doji | down | 1,412 | +0.40% | +0.71% | +1.12% | 52% | +3.0 | works in reverse |
| evening star | down | 472 | +0.44% | +0.48% | +0.67% | 46% | +1.2 | no reliable edge |
| rsi overbought exit | down | 4,157 | +0.20% | +0.48% | +0.84% | 52% | +1.2 | no reliable edge |
| bearish marubozu | down | 9,977 | +0.32% | +0.32% | +0.27% | 49% | +4.6 | works in reverse |
| shooting star | down | 3,824 | +0.22% | +0.30% | +0.56% | 52% | +1.0 | no reliable edge |
| volume surge down | down | 5,706 | +0.33% | +0.21% | +0.29% | 49% | -0.5 | no reliable edge |
| bearish engulfing | down | 6,765 | +0.10% | +0.16% | +0.12% | 52% | +1.1 | no reliable edge |
| macd cross down | down | 9,247 | +0.04% | +0.11% | +0.03% | 51% | +1.6 | no reliable edge |
| bearish harami | down | 3,456 | -0.04% | +0.04% | +0.02% | 54% | +0.1 | no reliable edge |
| breakdown 52w low | down | 3,157 | -0.06% | +0.04% | +0.22% | 50% | +0.1 | no reliable edge |
| death cross | down | 609 | -0.01% | -0.01% | -0.07% | 54% | -0.1 | no reliable edge |
| dark cloud cover | down | 1,049 | +0.32% | -0.17% | -0.34% | 55% | -0.3 | no reliable edge |
| hanging man | down | 6,010 | -0.36% | -0.25% | -0.12% | 56% | -3.3 | works as expected |
| three black crows | down | 182 | +0.32% | -0.26% | +0.33% | 51% | -0.6 | no reliable edge |

Past results do not guarantee future ones. Survivorship: stocks that were delisted are missing from the data, which flatters long-run returns a little.
