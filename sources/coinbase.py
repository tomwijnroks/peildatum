import requests
from datetime import datetime
from dateutil import tz

from sources.exchange import Exchange

class Coinbase(Exchange):
  start_year = 2016
  api_url ="https://api.exchange.coinbase.com/products/BTC-EUR/candles"

  def params(self, year):
    params = {
      "granularity": 3600,
      "start": self.__custom_time(year),
      "end": self.__custom_time(year, True)
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
    low = min([hour[1] for hour in json_response])

    return {
      'open': json_response[-1][3],
      'high': high,
      'low': low,
      'close': json_response[0][4],
    }

  def __custom_time(self, year, use_end_date = False):
    # Prepare timezones for conversion.
    from_zone = tz.gettz(self.timezone)
    to_zone = tz.gettz('UTC')

    # Start with utc date.
    utc = datetime.fromisoformat(str(year)+"-01-01 00:00:00")

    if (use_end_date):
      utc = datetime.fromisoformat(str(year)+"-01-01 23:59:59")

    utc = utc.replace(tzinfo=from_zone)
    # Convert to local date.
    localtime = utc.astimezone(to_zone)

    # Coinbase requires ISO 8601 without the timezone/offset (strip all after '+' character).
    return str(localtime.isoformat()).split("+", 1)[0]
