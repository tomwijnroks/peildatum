#!/usr/bin/env python3
# Script to convert a csv file with 'unixtime,value,volume' to 'date,time,value'.
import csv
from datetime import datetime

# Define the date and files.
input_date = '20181231'
input_file = ['bitstampEUR.csv', 'coinbaseEUR.csv', 'krakenEUR.csv']

# Loop trough the input files.
for file_ in input_file:

  # Use input_file without extension and append it with underscore, input_date and extension.
  output_file = str(input_date) + '_' + str(file_)
  f = open(output_file, 'w+')

  # Loop trough columns 0 (unixtime) and 1 (value) and convert unixtime to human date and time.
  for row in csv.reader(open(file_)):
    date_ = datetime.utcfromtimestamp(float(row[0])).strftime('%Y%m%d')
    time_ = datetime.utcfromtimestamp(float(row[0])).strftime('%H:%M:%S')
    value = float(row[1])

    # If the date matches with the input_date write 'date,time,value' to the output file.
    if date_ == input_date:
      f.write('{},{},{}\n'.format(date_, time_, value))

  # Close the output file.
  f.close
