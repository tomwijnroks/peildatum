# Kraken
Kraken OHLC data sources:
- https://support.kraken.com/hc/en-us/articles/360047124832-Downloadable-historical-OHLCVT-Open-High-Low-Close-Volume-Trades-data
- Download: XBT_OHLCVT.zip (contains: XBTUSD_1.csv, XBTEUR_1.csv)

## Opening price
The Bitcoin opening price at the start of every year (Central European Time / UTC+1).

| Unixtime   | ISO 8601 date/time format | BTC/USD   | BTC/EUR   |
|------------|---------------------------|----------:|----------:|
| 1388530800 | 2014-01-01T00:00:00+01:00 |    679.77 |    495.30 |
| 1420066800 | 2015-01-01T00:00:00+01:00 |    316.66 |    261.88 |
| 1451602800 | 2016-01-01T00:00:00+01:00 |    430.98 |    395.77 |
| 1483225200 | 2017-01-01T00:00:00+01:00 |    959.24 |    914.41 |
| 1514761200 | 2018-01-01T00:00:00+01:00 |  13991.40 |  11899.60 |
| 1546297200 | 2019-01-01T00:00:00+01:00 |   3687.10 |    3236.0 |
| 1577833200 | 2020-01-01T00:00:00+01:00 |   7175.90 |    6410.0 |

## Currency converter
The 2014-2017 BTC/USD prices have been [converted](https://pypi.org/project/CurrencyConverter/) from BTC/EUR to USD. Historical rates are sourced from the European Central Bank.
```
currency_converter 495.30 EUR --to USD -d 2014-01-01
495.300 EUR = 679.774 USD on 2014-01-01

currency_converter 261.88 EUR --to USD -d 2015-01-01
261.880 EUR = 316.665 USD on 2015-01-01

currency_converter 395.77 EUR --to USD -d 2016-01-01
395.770 EUR = 430.984 USD on 2016-01-01

currency_converter 914.41 EUR --to USD -d 2017-01-01
914.410 EUR = 959.247 USD on 2017-01-01
```
