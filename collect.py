from datetime import date
import yaml

from sources.binance import Binance
from sources.bitfinex import Bitfinex
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
  'bitfinex': Bitfinex(),
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
    with open("docs/_data/ohlc/"+name+".yaml", "r") as stream:
      exchange_data = yaml.safe_load(stream)
      if exchange_data:
        ohlc[name] = exchange_data
  except FileNotFoundError:
    pass

# Loop years.
for year in years:
  print("Year " + str(year))
  # Loop exchanges and get ohlc data for the provided year.
  for name, exchange in exchanges.items():
    year_ohlc = exchange.get(year)

    if not year in ohlc[name].keys():
      ohlc[name][year] = {
        "open": '-',
        "high": '-',
        "low": '-',
        "close": '-',
      }
    if year_ohlc:
      ohlc[name][year] = year_ohlc

    exchange_year_value = "{exchange} {year} ({source})\nOpen: {open} | High: {high} | Low: {low} | Close: {close}\n" .format(
      year = year,
      exchange = name,
      open = 'EUR '+str(ohlc[name][year]["open"]) if ohlc[name][year]["open"] != '-' else 'unknown',
      high = 'EUR '+str(ohlc[name][year]["high"]) if ohlc[name][year]["high"] != '-' else 'unknown',
      low = 'EUR '+str(ohlc[name][year]["low"]) if ohlc[name][year]["low"] != '-' else 'unknown',
      close = 'EUR '+str(ohlc[name][year]["close"]) if ohlc[name][year]["close"] != '-' else 'unknown',
      source = 'data from API' if year_ohlc else 'existing data'
    )
    print(exchange_year_value)

  print("")

# Define a custom representer for strings with numbers to make sure the amounts are quoted.
def quoted_presenter(dumper, data):
    if any(char.isdigit() for char in data):
      return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="")
yaml.add_representer(str, quoted_presenter)

for exchange_name, values in ohlc.items():
  filename = "docs/_data/ohlc/"+exchange_name + ".yaml"
  with open(filename, 'w+') as outfile:
    yaml.dump(values, outfile, default_flow_style=False)
