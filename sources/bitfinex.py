import requests
from datetime import datetime

from sources.exchange import Exchange

class Bitfinex(Exchange):
  start_year = 2018
  api_url = "https://api-pub.bitfinex.com/v2/candles/trade:1h:tBTCEUR/hist"

  def params(self, year):
    timestamp = self.timestamp(year)
    # End timestamp is +24 hours, minus 1 second, to stay within the same day at 23:59:59.
    endTimestamp = timestamp + 86400 - 1

    params = {
      "start": str(timestamp)+"000",
      "end": str(endTimestamp)+"999"
    }

    return params

  def year(self, year):
    json_response = requests.get(
      self.api_url,
      params = self.params(year)
    ).json()

    # The json response is a dict with groups per hour.
    # Find the min and max for the whole result set by looping over all hours.
    high = max([hour[3] for hour in json_response])
    low = min([hour[4] for hour in json_response])

    return {
      'open': json_response[-1][1],
      'close': json_response[0][2],
      'high': high,
      'low': low,
    }
