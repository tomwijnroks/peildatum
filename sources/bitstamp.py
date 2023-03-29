import requests
from datetime import datetime

from sources.exchange import Exchange

class Bitstamp(Exchange):
  start_year = 2012
  api_url ="https://www.bitstamp.net/api/v2/ohlc/btceur/"

  def params(self, year):
    params = {
      "step": 3600,
      "limit": 1,
      "start": str(self.timestamp(year))
    }

    return params

  def year(self, year):
    json_response = requests.get(
      self.api_url,
      params = self.params(year)
    ).json()

    if not json_response["data"]["ohlc"]:
      return None

    ohlc = {
      'open': json_response["data"]["ohlc"][0]["open"],
      'close': json_response["data"]["ohlc"][0]["close"],
      'high': json_response["data"]["ohlc"][0]["high"],
      'low': json_response["data"]["ohlc"][0]["low"],
    }

    return ohlc["open"]
