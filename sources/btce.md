# BTC-e
BTC-e data sources:
- https://api.bitcoincharts.com/v1/csv/

Bitcoincharts does not contain OHCL data and trading data for 00:00:00 timestamps is missing. Therefore, the first availabe timestamp within the first opening hour of the year has been used.

## Opening price
The Bitcoin opening price at the start of every year (Central European Time / UTC+1).

| Unixtime   | ISO 8601 date/time format | BTC/USD   | BTC/EUR   |
|------------|---------------------------|----------:|----------:|
| 1325372499 | 2012-01-01T00:01:39+01:00 |      4.51 |           |
| 1356995168 | 2013-01-01T00:06:08+01:00 |     13.28 |           |
| 1388530831 | 2014-01-01T00:00:31+01:00 |    730.03 |           |
| 1420066800 | 2015-01-01T00:00:00+01:00 |       N/A |           |
| 1451602830 | 2016-01-01T00:00:30+01:00 |    428.95 |
| 1483225208 | 2017-01-01T00:00:08+01:00 |    928.89 |
