#!/bin/bash
################################################################################
# This script will print the BTC/EUR price at the start of every year.
# It uses public OHLC data from exchanges to retrieve the opening price.
################################################################################

YEARS="2020 2023"
TIMEZONE="Europe/Amsterdam"
PAIR="BTC-EUR"
API_URL="https://api.bitvavo.com/v2/BTC-EUR/candles?&interval=1h"

# Loop trough the years range.
for YEAR in `seq ${YEARS}`; do

  # Sleep to avoid rate limits.
  sleep 2

  # Create a unix timestamp for every year.
  UNIX_TIME=$(TZ=":${TIMEZONE}" date "+%s" -d "${YEAR}-01-01 00:00:00")

  # Create a iso 8601 format from the unix timestamp.
  ISO_8601=$(date --iso-8601=seconds -d @${UNIX_TIME})

  # Get the OHCL open price from the public exchange api.
  # Each bucket is an array of the following information:
  # [ time, open, high, low, close, volume, ...more... ]
  # The start and end are appended with 000 and 999 ms because milliseconds are required.
  OHLC_OPEN=$(curl --silent "${API_URL}&start=${UNIX_TIME}000&end=${UNIX_TIME}999" | jq -r '.[][1]')

  # Print the unix timestamp, year and openings price.
  echo "${UNIX_TIME} ${ISO_8601} ${OHLC_OPEN}"

done
