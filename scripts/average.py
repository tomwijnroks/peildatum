#!/usr/bin/env python3
###############################################################################
# This script does:
# 1. Read a csv file and convert the unixtime to human date (yyyy-mm-dd).
# 2. Calculate the average value for the input_date for every csv file.
# 3. Calculate the total average value by using the csv file average value.
#
# Notes:
# The used csv files are from: https://api.bitcoincharts.com/v1/csv/
###############################################################################
import csv
from datetime import datetime

# Set count and sum to zero.
count = 0
sum = 0

# Loop trough columns 0 (unixtime) and 1 (value) and convert unixtime to human date and time.
for row in csv.reader(open(input_file)):
  date_ = datetime.utcfromtimestamp(float(row[0])).strftime('%Y%m%d')
  value = float(row[1])

  # Check if the date matches with the input_date.
  if date_ == input_date:
      # Calculate the average of the values and round to 2 decimals.
      count = count + 1
      sum = sum + value
      average = round(sum / count, 2)

# Print the results.
# Define the date and files.
input_date = '2019-01-01'
input_file = ['bitstampEUR.csv', 'coinbaseEUR.csv', 'krakenEUR.csv']

print('-'*40)
print('File    :', input_file)
print('Date    :', input_date)
print('Average :', average)
print('-'*40)
