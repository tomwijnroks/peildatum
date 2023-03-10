import requests
from datetime import datetime

from sources.exchange import Exchange

class Bitfenix(Exchange):
  start_year = 2018
  api_url = "https://api-pub.bitfinex.com/v2/candles/trade:1h:tBTCEUR/hist"

  def params(self, year):
    timestamp = self.timestamp(year)

    params = {
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
      'close': json_response[0][2],
      'high': json_response[0][3],
      'low': json_response[0][4],
    }

    return ohlc["open"]


