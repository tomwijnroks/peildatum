#!/bin/bash
################################################################################
# This script uses historical OHLC data from the Bitstamp API.
# It tries to fetch the opening price at the start of every year.
################################################################################

YEARS="2012 2021"
TIMEZONE="Europe/Amsterdam"
#PAIR="btcusd"
PAIR="btceur"
API_URL="https://www.bitstamp.net/api/v2/ohlc/${PAIR}/?step=3600&limit=1&start="

# Loop trough the years range.
for YEAR in `seq ${YEARS}`; do

  # Prevent hitting rate limits.
  sleep 2

  # Create a unix timestamp for every year.
  UNIX_TIME=$(TZ=":${TIMEZONE}" date "+%s" -d "${YEAR}-01-01 00:00:00")

  # Create a iso 8601 format from the unix timestamp.
  ISO_8601=$(date --iso-8601=seconds -d @${UNIX_TIME})

  # Get the OHCL open price using the unix timestamp.
  # Each tick in the trading pair dictionary is represented as a list of OHLC data.
  # Format: { pair } [{ high, timestamp, volume, low, close, open }]
  OHLC_OPEN=$(curl --silent ${API_URL}${UNIX_TIME} | jq -r '.data.ohlc[].open')

  # Print the unix timestamp, year and openings price.
  echo "${UNIX_TIME} ${ISO_8601} ${OHLC_OPEN}"

done
