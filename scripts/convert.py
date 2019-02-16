#!/usr/bin/env python3
# Script to convert a csv file with 'unixtime,value,volume' to 'date,time,value'.
# A new csv file will be created based on the input_file name and input_date.
import csv
import os.path
from datetime import datetime

# Define the date and file.
input_date = '20190101'
input_file = 'test.csv'

# Use input_file without extension and append it with underscore, input_date and extension.
output_file = str(os.path.splitext(input_file)[0]) + '_' + str(input_date) + '.csv'

# Open the new output file.
f = open(output_file, 'w+')

# Loop trough columns 0 (unixtime) and 1 (value) and convert unixtime to human date and time.
for row in csv.reader(open(input_file)):
  date_ = datetime.utcfromtimestamp(float(row[0])).strftime('%Y%m%d')
  time_ = datetime.utcfromtimestamp(float(row[0])).strftime('%H:%M:%S')
  value = float(row[1])

  # If the date matches with the input_date write 'date,time,value' to the output file.
  if date_ == input_date:
      f.write('{},{},{}\n'.format(date_, time_, value))

# Close the output file.
f.close
