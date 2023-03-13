import requests
from datetime import datetime
from dateutil import tz
import pandas as pd

from sources.exchange import Exchange

"""
Kraken does not provide history OHLC via their API.
Instead it is being calculated by using all trades withing the specified hour.

see: https://medium.com/analytics-vidhya/downloading-and-resampling-crypto-trade-data-with-python-5059ddcc9bcc
"""
class Kraken(Exchange):
  start_year = 2014
  api_url ="https://api.kraken.com/0/public/Trades"

  def params(self, timestamp):
    params = {
      "pair": "XBTEUR",
      "since": timestamp
    }

    return params

  def year(self, year):
    ohlc = self._get_ohlc(year)

    return ohlc["open"]


  def _get_ohlc(self, year):
    trades = self._get_trades(year)

    # Put all trades in a dataframe.
    tradesDF = pd.DataFrame.from_records(
      trades,
      columns=['Price','Volume','Time','BuySell','MarketLimit','Misc', 'TradeId']
    )
    tradesDF['Time'] = pd.to_datetime(tradesDF['Time'], unit='s')
    tradesDF.set_index('Time',inplace=True)

    ohlcDF = tradesDF.resample('1H')['Price'].agg(["first", "max", "min", "last"])

    ohlc = {
      'open': ohlcDF.iat[0, 0],
      'high': ohlcDF.iat[0, 1],
      'low': ohlcDF.iat[0, 2],
      'close': ohlcDF.iat[0, 3],
    }

    return ohlc

  def _get_trades(self, year):
    end_date = str(year)+"-01-01 01:00:00"
    start_date = str(year)+"-01-01 00:00:00"
    end_timestamp = int(datetime.fromisoformat(end_date).timestamp())*1000000000
    start_timestamp = int(datetime.fromisoformat(start_date).timestamp())*1000000000

    trades = list()

    # The api returns 1000 trades, call api in a loop in case not all trades are returned in the 1st call.
    while start_timestamp < end_timestamp:
      json_response = requests.get(self.api_url, params = self.params(start_timestamp)).json()
      trades.extend(json_response["result"]["XXBTZEUR"])

      # Set the new start date to get more trades when end date has not yet been reached.
      start_timestamp = int(json_response["result"]["last"])

    # Filter out trades that happened after the end date. Within the trade the transaction date is in the 3rd column.
    return list(filter(lambda trade: float(trade[2]) <= end_timestamp, trades))
