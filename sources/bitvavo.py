import requests
from datetime import datetime

from sources.exchange import Exchange

class Bitvavo(Exchange):
  start_year = 2020
  api_url ="https://api.bitvavo.com/v2/BTC-EUR/candles"

  def params(self, year):
    timestamp = self.timestamp(year)

    params = {
      "interval": "1h",
      "start": str(timestamp)+"000",
      "end": str(timestamp)+"999"
    }

    return params

  def year(self, year):
    json_response = requests.get(
      self.api_url,
      params = self.params(year)
    ).json()

    ohlc = {
      'open': json_response[0][1],
      'high': json_response[0][2],
      'low': json_response[0][3],
      'close': json_response[0][4],
    }

    return ohlc["open"]

