from abc import ABC, abstractmethod
from datetime import datetime
from dateutil import tz

class Exchange(ABC):
  timezone = "Europe/Amsterdam"

  def get(self, year):
    if year < self.start_year:
      return None

    value = self.year(year)

    if value:
      return {
        'open': self.format(value["open"]),
        'close': self.format(value["close"]),
        'high': self.format(value["high"]),
        'low': self.format(value["low"]),
      }

    return None

  def format(self, value):
    formatted_value = '{:_.2f}'.format(float(value)).replace(".", ",").replace("_", ".")
    return formatted_value

  def timestamp(self, year):
    ts_timezone = tz.gettz(self.timezone)
    ts_datetime = datetime.fromisoformat(str(year)+"-01-01 00:00:00")
    ts_replaced = ts_datetime.replace(tzinfo=ts_timezone)
    return int(ts_replaced.timestamp())

  @abstractmethod
  def year(self, year):
    raise NotImplementedError("Must override year")
