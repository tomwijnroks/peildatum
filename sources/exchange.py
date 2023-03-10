from abc import ABC, abstractmethod
from datetime import datetime

class Exchange(ABC):
  timezone = "Europe/Amsterdam"

  def get(self, year):
    if year < self.start_year:
      return None

    value = self.year(year)

    return self.format(value)

  def format(self, value):
    formatted_value = '{:_.2f}'.format(float(value)).replace(".", ",").replace("_", ".")
    return formatted_value

  def timestamp(self, year):
    return int(datetime.fromisoformat(str(year)+"-01-01 00:00:00").timestamp())

  @abstractmethod
  def year(self, year):
    raise NotImplementedError("Must override year")
