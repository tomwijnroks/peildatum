import requests
from datetime import datetime

from sources.exchange import Exchange

class Bitstamp(Exchange):
  start_year = 2012
  api_url ="https://www.bitstamp.net/api/v2/ohlc/btceur/"

  def params(self, year):
    params = {
      "step": 3600,
      "limit": 24,
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

    # The json response is a dict with groups per hour.
    # Find the min and max for the whole result set by looping over all hours.
    high = max([hour["high"] for hour in json_response["data"]["ohlc"]])
    low = min([hour["low"] for hour in json_response["data"]["ohlc"]])

    return {
      'open': json_response["data"]["ohlc"][0]["open"],
      'close': json_response["data"]["ohlc"][-1]["close"],
      'high': high,
      'low': low,
    }
