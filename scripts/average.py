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

# Define the date and files.
input_date = '2019-01-01'
input_file = ['bitstampEUR.csv', 'coinbaseEUR.csv', 'krakenEUR.csv']

# Set the total file count and sum to zero.
total_count = 0
total_sum = 0

# Loop trough the input files.
for file in input_file:
  # Set file count and sum to zero.
  file_row = 0
  file_sum = 0

  # Loop trough columns 0 (unixtime) and 1 (value) and convert unixtime to human date.
  for row in csv.reader(open(file)):
    date_ = datetime.utcfromtimestamp(float(row[0])).strftime('%Y-%m-%d')
    value = float(row[1])

    # Check if the date matches with the input_date.
    if date_ == input_date:
      # Calculate the file average: sum values, devide by rows and round to 2 decimals.
      file_row = file_row + 1
      file_sum = file_sum + value
      file_avg = round(file_sum / file_row, 2)

    # If none of the rows matched the date set the file average to zero.
    if file_row == 0:
      file_avg = 0

  # Print the file results.
  print('-'*40)
  print('Date    :', input_date)
  print('File    :', file)
  print('Average :', file_avg)

  # Calulate the total average if the file average is not zero:
  # Sum the average file values, devide by the number of files and round to 2 decimals.
  if file_avg != 0:
    total_count = total_count + 1
    total_sum = total_sum + file_avg
    total_avg = round(total_sum / total_count, 2)
  else:
    total_avg = 0

# Print the total average value.
print('-'*40)
print('Total average value:', total_avg)
print('-'*40)
