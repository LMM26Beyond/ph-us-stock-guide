# Reading candlesticks and indicators

This guide explains what the app looks for in a chart and how much weight each
signal deserves. The short version: candles and indicators describe what
buyers and sellers did. They tilt the odds a little at best. The app tests
every signal on PSE and US history (see `reports/signals_ph.md` and
`reports/signals_us.md`) and only lets the ones that held up count in a
stock's score.

## 1. One candle

Each candle covers one trading day.

```
      │   ← upper shadow (wick): the high
    ┌─┴─┐
    │   │ ← body: from open to close
    │   │    green/white = closed above the open (buyers won the day)
    └─┬─┘    red/black   = closed below the open (sellers won the day)
      │   ← lower shadow: the low
```

What the parts tell you:

- **Long body**: one side was in control all day.
- **Small body**: indecision; neither side won.
- **Long lower shadow**: sellers pushed the price down, buyers pushed it back up.
- **Long upper shadow**: buyers pushed it up, sellers pushed it back down.
- **Where** the candle appears matters more than its shape. A hammer after a
  fall is a possible turn; the same shape after a rise (a hanging man) is a
  warning. The app only counts a reversal pattern when the trend into it
  points the other way: the previous close must be below (or above) both the
  close 5 days earlier and the 10-day average.

"Long body" in the app means a body bigger than the average body of the
previous 20 days.

## 2. Single-candle patterns

| Pattern | Looks like | Where | Reading |
|---|---|---|---|
| **Doji** | Open ≈ close (body ≤ 10% of the day's range) | Anywhere | Indecision. Detected but not scored on its own. |
| **Dragonfly doji** | Doji with a long lower shadow, no upper shadow | After a fall | Sellers failed; possible bottom. Bullish. |
| **Gravestone doji** | Doji with a long upper shadow, no lower shadow | After a rise | Buyers failed; possible top. Bearish. |
| **Hammer** | Small body at the top, lower shadow ≥ 2× the body, almost no upper shadow | After a fall | Buyers stepped in. Bullish. |
| **Hanging man** | Same shape as a hammer | After a rise | Selling showed up inside an uptrend. Bearish. |
| **Inverted hammer** | Small body at the bottom, upper shadow ≥ 2× the body | After a fall | First attempt by buyers. Weakly bullish. |
| **Shooting star** | Same shape as an inverted hammer | After a rise | Rally rejected. Bearish. |
| **Bullish marubozu** | Long green body with almost no shadows (body ≥ 90% of range, 1.5× the average body) | Anywhere | Buyers in control from open to close. |
| **Bearish marubozu** | Long red body with almost no shadows | Anywhere | Sellers in control from open to close. |

## 3. Two-candle patterns

| Pattern | Looks like | Where | Reading |
|---|---|---|---|
| **Bullish engulfing** | Red candle, then a bigger green body that covers it | After a fall | Buyers took over. One of the better-known reversal signals. |
| **Bearish engulfing** | Green candle, then a bigger red body that covers it | After a rise | Sellers took over. |
| **Piercing line** | Long red candle, then a green one that opens below its close and closes above its midpoint | After a fall | Strong recovery inside one day. Bullish. |
| **Dark cloud cover** | Long green candle, then a red one that opens above its close and closes below its midpoint | After a rise | Bearish mirror of the piercing line. |
| **Bullish harami** | Long red candle, then a small body inside it | After a fall | Selling slowed down. Weakly bullish; wants confirmation. |
| **Bearish harami** | Long green candle, then a small body inside it | After a rise | Buying slowed down. Weakly bearish. |

## 4. Three-candle patterns

| Pattern | Looks like | Where | Reading |
|---|---|---|---|
| **Morning star** | Long red, a small "star" body that stays below it, then green closing above the first candle's midpoint | After a fall | Classic bottom. Bullish. |
| **Evening star** | Long green, a small star above it, then red closing below the first candle's midpoint | After a rise | Classic top. Bearish. |
| **Three white soldiers** | Three long green candles, each opening inside the previous body and closing higher | After a fall | Steady buying. Bullish. |
| **Three black crows** | Three long red candles, each opening inside the previous body and closing lower | After a rise | Steady selling. Bearish. |

## 5. Indicators

Indicators smooth the candles into a trend or a reading of strength.

| Indicator | What it is | How the app uses it |
|---|---|---|
| **Moving averages (SMA 50, 200)** | Average close over the last 50 or 200 days | Price above a rising 200-day average is an uptrend. **Golden cross**: the 50-day crosses above the 200-day. **Death cross**: crosses below. |
| **MACD** | 12-day minus 26-day exponential average, with a 9-day signal line | Histogram above zero = momentum up. Crosses of the signal line are studied as signals. |
| **RSI (14)** | 0–100 gauge of recent gains versus losses | Above 70 overbought, below 30 oversold. The signal studied is the *exit*: RSI climbing back above 30, or falling back below 70. Over 80 counts against a stock in the score. |
| **ATR (14)** | Average daily range, including gaps | Sets stop-loss distances: 3 × ATR below the price. |
| **Bollinger bands** | 20-day average ± 2 standard deviations | Computed for reference. |
| **52-week high / low** | Highest high and lowest low of the last year | A close above the 52-week high is a **breakout**; below the low, a **breakdown**. |
| **Volume surge** | Volume more than 2× its 20-day average with a move over 2% | Big moves on heavy volume show conviction. |
| **Momentum** | 12-month return skipping the latest month, and 6-month return versus the index | Stocks that have beaten the market for months tend to keep doing so for a while. This is one of the most consistent effects in market research. |

For the market itself (the PSEi and S&P 500), the report uses the index's
position versus its 50- and 200-day averages and the share of stocks above
their own 200-day average ("breadth") to call it an uptrend, a downtrend or
mixed.

## 6. How much to trust a signal

Textbook pattern lists rarely say how often the patterns work. Studies on
large data sets generally find that most single candle patterns have a small
edge or none once you compare them with an ordinary day, while trend and
momentum effects are more persistent. So the app checks rather than assumes:

1. For every time a signal appeared on a liquid stock, it measures the
   stock's return over the next 5, 10 and 20 trading days **minus the
   index's** return, and compares that with an ordinary day.
2. A signal is called *working* only if it appeared at least 30 times, the
   result is statistically clear (|t| ≥ 2, counting each date once because
   signals cluster on the same days), and it points the same way in both
   halves of the history.
3. Signals that work in reverse are flagged too, and count backwards.
4. The stock score (0–100) is mostly trend and momentum (70%). MACD and RSI
   add 10% each, and recent candles add the last 10%, using only signals that
   passed step 2.
5. The report also tests the score itself on past month-ends: did the
   top-scored fifth of stocks beat the bottom fifth over the next month?

## 7. Rules of thumb

- Trade with the market's trend. In a downtrend most stocks fall, whatever
  their candles say.
- Wait for confirmation: a bullish pattern means more if the next day closes
  higher.
- Patterns on thinly traded stocks are noise. The app ignores stocks that
  trade less than ₱5 million (or $5 million) a day.
- Always know your exit before you buy. The app gives a stop 3 × ATR below
  the price, and a trailing stop for holdings that rises with the price.
- None of this is financial advice. Check news and fundamentals, and size
  each position so a stop-out is affordable.
