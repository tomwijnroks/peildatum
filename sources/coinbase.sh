#!/bin/bash
################################################################################
# This script uses historical OHLC data from the Coinbase API.
# It tries to fetch the opening price at the start of every year.
################################################################################

YEARS="2016 2021"
TIMEZONE="Europe/Amsterdam"
PAIR="BTC-EUR"
API_URL="https://api.pro.coinbase.com/products/${PAIR}/candles?&granularity=3600"

# Loop trough the years range.
for YEAR in `seq ${YEARS}`; do

  # Prevent hitting rate limits.
  sleep 2

  # Create a unix timestamp for every year.
  UNIX_TIME=$(TZ=":${TIMEZONE}" date "+%s" -d "${YEAR}-01-01 00:00:00")

  # Create a iso 8601 format from the unix timestamp.
  ISO_8601=$(date --iso-8601=seconds -d @${UNIX_TIME})

  # Coinbase requires iso 8601 format without the timezone.
  ISO_8601_COINBASE=$(date --utc --iso-8601=seconds -d @${UNIX_TIME} | cut -f1 -d'+')

  # Get the OHCL open price from the public exchange api.
  # Each bucket is an array of the following information:
  # Format: [ time, low, high, open, close, volume ]
  OHLC_OPEN=$(curl --silent "${API_URL}&start=${ISO_8601_COINBASE}&end=${ISO_8601_COINBASE}" | jq -r '.[][3]')

  # Print the unix timestamp, year and openings price.
  echo "${UNIX_TIME} ${ISO_8601} ${OHLC_OPEN}"

done
