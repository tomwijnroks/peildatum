#!/usr/bin/env python3
###############################################################################
# This script does:
# 1. Read a csv file and convert the unixtime to human date (yyyymmdd).
# 2. Calculate the average value for the given input_date and print it.
###############################################################################
import csv
from datetime import datetime

# Define the file and date.
input_file = 'test.csv'
input_date = '20190101'

# Set count and sum to zero.
count = 0
sum = 0

# Loop trough columns 0 (unixtime) and 1 (value) and convert unixtime to human date.
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
print('-'*40)
print('File    :', input_file)
print('Date    :', input_date)
print('Average :', average)
print('-'*40)
