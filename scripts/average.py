#!/usr/bin/env python3
# Script to read a csv file with values and calculate the average value.
import csv

# Define the csv file.
csv_file = 'test_20190101.csv'

# Set count and sum to zero.
count = 0
sum = 0

# Loop trough all rows to read values from column 2.
for row in csv.reader(open(csv_file)):
  value = float(row[2])

  # Calculate the average of all values and round to 2 decimals.
  count = count + 1
  sum = sum + value
  average = round(sum / count, 2)

# Print the result.
print('Average:', average)
