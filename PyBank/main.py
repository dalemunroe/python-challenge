#Import the OS module
from ast import Str
from decimal import ROUND_CEILING
import os

#Module for reading CSV files
import csv

csv_path = os.path.join('Resources','budget_data.csv')

# Reading CSV File using CSV module

# Count the total number of months
with open(csv_path, encoding='utf-8') as csv_file:

    #Prints Wrapper DEL
    #print (csv_file)

    # CSV reader specifies delimiter and variable that holds contents
    #csv_reader is the data
    csv_data = csv.reader(csv_file, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csv_data)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csv_data:
        #print(row)

    # Count the total number of months

    for row in csv_data:
        pass
    month_count = (csv_data.line_num - 1)
    print("Total Months: " + str(month_count))

#Sum Total P&L
with open(csv_path, encoding='utf-8') as csv_file:

    #Prints Wrapper DEL
    #Print (csv_file) DEL

    # CSV reader specifies delimiter and variable that holds contents
    #csv_reader is the data
    csv_data = csv.reader(csv_file, delimiter=',')
    total = 0
    csv_data1 = csv.reader(csv_file, delimiter=',')

    for row in csv_data:
        if not str(row[1]).startswith('P'):
            total = total + int(row[1])
    print("Total: $" + str(total))
