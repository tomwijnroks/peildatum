import requests
from datetime import datetime
from dateutil import tz
import pandas as pd
from time import sleep

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
    return self._get_ohlc(year)


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

    high = ohlcDF.get("max").max()
    low = ohlcDF.get("min").min()

    ohlc = {
      'open': ohlcDF.iat[0, 0],
      'high': high,
      'low': low,
      'close': ohlcDF.iat[-1, 3],
    }

    return ohlc

  def _get_trades(self, year):
    end_date = str(year)+"-01-01 23:59:59"
    start_date = str(year)+"-01-01 00:00:00"
    end_timestamp = int(datetime.fromisoformat(end_date).timestamp())*1000000000
    start_timestamp = int(datetime.fromisoformat(start_date).timestamp())*1000000000

    trades = list()

    # The api returns 1000 trades, call api in a loop in case not all trades are returned in the 1st call.
    counter = 1;
    while start_timestamp < end_timestamp:
      print("Get Kraken trades {1} to {2} for year {0}".format(str(year), 1000*counter-1000, 1000*counter))
      json_response = requests.get(self.api_url, params = self.params(start_timestamp)).json()
      trades.extend(json_response["result"]["XXBTZEUR"])

      # Set the new start date to get more trades when end date has not yet been reached.
      start_timestamp = int(json_response["result"]["last"])
      counter += 1
      # Getting trade data for Kraken results in multiple API calls.
      # To not hit the API rate limit, a sleep had to be added.
      sleep(1)

    # Filter out trades that happened after the end date. Within the trade the transaction date is in the 3rd column.
    return list(filter(lambda trade: float(trade[2]) <= end_timestamp, trades))
