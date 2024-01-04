import requests
from datetime import datetime

from sources.exchange import Exchange

class Bitvavo(Exchange):
  start_year = 2020
  api_url ="https://api.bitvavo.com/v2/BTC-EUR/candles"

  def params(self, year):
    timestamp = self.timestamp(year)

    # End timestamp is +24 hours, minus 1 second, to stay within the same day at 23:59:59.
    endTimestamp = timestamp + 86400 - 1

    params = {
      "interval": "1h",
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
    high = max([hour[2] for hour in json_response])
    low = min([hour[3] for hour in json_response])

    return {
      'open': json_response[-1][1],
      'high': high,
      'low': low,
      'close': json_response[0][4],
    }

