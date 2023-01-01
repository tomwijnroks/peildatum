#!/bin/bash
################################################################################
# This script uses historical OHLC data from Kraken OHLCVT files. OHLCVT data
# updates are provided at the end of each quarter.
#
# The archive file XBT_OHLCVT.zip contains the XBTEUR_60.csv file.
# Source: https://support.kraken.com/hc/en-us/articles/360047124832
#
################################################################################
#
# For recent OHLC data use the public api. Use a few minutes ahead of the actual
# time to get the right results.
#
# Example: use '1640991000' to get '1640991600' in the results.
# Array contains: (<time>, <open>, <high>, <low>, <close>, <vwap>, <volume>, <count>)
#
# curl --silent "https://api.kraken.com/0/public/OHLC?pair=XXBTZEUR&since=1640991000&interval=60" | jq
# {
#   "error": [],
#   "result": {
#     "XXBTZEUR": [
#       [
#         1640991600,
#         "40721.5",
#         "40881.9",
#         "40631.3",
#         "40660.3",
#         "40804.4",
#         "54.26003307",
#         824
#       ],
#
################################################################################

YEARS="2014 2023"
TIMEZONE="Europe/Amsterdam"
CSV_FILE="XBTEUR_60.csv"

# Loop trough the years range.
for YEAR in `seq ${YEARS}`; do

  # Create a unix timestamp for every year.
  UNIX_TIME=$(TZ=":${TIMEZONE}" date "+%s" -d "${YEAR}-01-01 00:00:00")

  # Create a iso 8601 format from the unix timestamp.
  ISO_8601=$(date --iso-8601=seconds -d @${UNIX_TIME})

  # Get the OHCL open price using the unix timestamp.
  OHLC_OPEN=$(grep "^${UNIX_TIME}" ${CSV_FILE} | awk -F, '{print $2}')

  # Print the unix timestamp, year and openings price.
  echo "${UNIX_TIME} ${ISO_8601} ${OHLC_OPEN}"

done
