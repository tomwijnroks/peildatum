#!/bin/bash
################################################################################
# This script uses historical OHLC data from Kraken OHLCVT files.
# It tries to fetch the opening price at the start of every year.
#
# Source: https://support.kraken.com/hc/en-us/articles/360047124832
################################################################################

YEARS="2014 2020"
TIMEZONE="Europe/Amsterdam"
CSV_FILE="XBTEUR_60.csv"

# Loop trough the years range.
for YEAR in `seq ${YEARS}`; do

  # Create a unix timestamp for every year.
  UNIX_TIME=$(TZ=":${TIMEZONE}" date "+%s" -d "${YEAR}-01-01 00:00:00")

  # Create a iso 8601 format from the unix timestamp.
  ISO_8601=$(date --iso-8601=seconds -d @${UNIX_TIME})

  # Get the OHCL open price using the unix timestamp.
  OHLC_OPEN=$(grep "^${UNIX_TIME}" ${CSV_FILE} | awk -F, '{print $5}')

  # Print the unix timestamp, year and openings price.
  echo "${UNIX_TIME} ${ISO_8601} ${OHLC_OPEN}"

done
