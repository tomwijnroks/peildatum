from datetime import date
import yaml

from sources.binance import Binance
from sources.bitfenix import Bitfenix
from sources.bitstamp import Bitstamp
from sources.bitvavo import Bitvavo
from sources.coinbase import Coinbase
from sources.kraken import Kraken

end_year = date.today().year
start_year = 2012

# Create range of years to get ohlc data for (desc).
years = range(end_year, start_year-1, -1)

# Define available exchanges.
exchanges = {
  'binance': Binance(),
  'bitfenix': Bitfenix(),
  'bitstamp': Bitstamp(),
  'bitvavo': Bitvavo(),
  'coinbase': Coinbase(),
  'kraken': Kraken(),
}

# Create a dict to collect ohlc data for all exchanges.
ohlc = {}

# Loop exchanges and try to load existing data from yaml files.
for name, exchange in exchanges.items():
  ohlc[name] = {}
  try:
    with open("ohlc/"+name+".yaml", "r") as stream:
      exchange_data = yaml.safe_load(stream)
      if exchange_data:
        ohlc[name] = exchange_data
  except FileNotFoundError:
    pass

# Loop years.
for year in years:
  print(year)
  # Loop exchanges and get ohlc data for the provided year.
  for name, exchange in exchanges.items():
    value = exchange.get(year)

    if not year in ohlc[name].keys():
      ohlc[name][year] = {
        "open": '-',
      }
    if value:
      ohlc[name][year]["open"] = value

    exchange_year_value = "On 1 jan {year} {exchange} was worth {value}. ({source})" .format(
      year = year,
      exchange = name,
      value = 'EUR '+str(ohlc[name][year]["open"]) if ohlc[name][year]["open"] != '-' else 'unknown',
      source = 'data from API' if value else 'existing data'
    )
    print(exchange_year_value)

  print("")

for exchange_name, values in ohlc.items():
  filename = "ohlc/"+exchange_name + ".yaml"
  with open(filename, 'w') as outfile:
    yaml.dump(values, outfile, default_flow_style=False)
