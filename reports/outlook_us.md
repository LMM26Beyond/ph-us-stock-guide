# Candle outlook: US stocks

Market trend used: **Uptrend** (the index against its 50- and 200-day averages), data up to 2026-10-30.

For each stock with a candle pattern in its last 3 candles, the chance it closes higher 10 trading days later is what happened after the same pattern on all stocks when the market was in the same trend, compared with the usual chance on any day in that trend. A gap of 3 points or more is called *Leans up* or *Leans down*. The app also shows each stock's own record with the pattern, for reference: mixing it into the call made the calls worse on new data, because one stock has too few cases.

## Did it work on new data?

Track records built from data up to Dec 2022 only, then tested on 462,526 stock-days with a pattern from 2023-01-03 to 2026-10-16. On all of them, the stock was higher 10 days later 51% of the time.

| Call | Cases | Expected to rise | Actually rose |
|---|---:|---:|---:|
| Leans up | 11,548 | 54% | 63% |
| Leans down | 19,779 | 46% | 59% |
| No clear edge | 431,199 | 52% | 50% |

**The calls failed this test in this market, so they are switched off:** every stock shows *No clear edge*, with the track records for reference.

## Today

Leans up: 0, Leans down: 0, No clear edge: 1299 stocks.

Candle patterns are a weak signal on their own: most of them barely move the odds, and several work the opposite way from the textbook (see the signals report). Use the outlook as one input next to the trend score, not as a forecast.
