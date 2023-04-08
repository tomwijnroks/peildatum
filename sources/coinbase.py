import requests
from datetime import datetime
from dateutil import tz

from sources.exchange import Exchange

class Coinbase(Exchange):
  start_year = 2016
  api_url ="https://api.pro.coinbase.com/products/BTC-EUR/candles"

  def params(self, year):
    coinbase_time = self.__custom_time(year)

    params = {
      "granularity": 3600,
      "start": coinbase_time,
      "end": coinbase_time
    }

    return params

  def year(self, year):
    json_response = requests.get(
      self.api_url,
      params = self.params(year)
    ).json()

    return {
      'open': json_response[0][3],
      'high': json_response[0][2],
      'low': json_response[0][1],
      'close': json_response[0][4],
    }

  def __custom_time(self, year):
    # Prepare timezones for conversion.
    from_zone = tz.gettz(self.timezone)
    to_zone = tz.gettz('UTC')

    # Start with utc date.
    utc = datetime.fromisoformat(str(year)+"-01-01 00:00:00")
    utc = utc.replace(tzinfo=from_zone)
    # Convert to local date.
    localtime = utc.astimezone(to_zone)

    # Coinbase requires ISO 8601 without the timezone/offset (strip all after '+' character).
    return str(localtime.isoformat()).split("+", 1)[0]
