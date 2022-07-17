#Week 3 Assignment - Python
#Dale Munroe

#Module for reading CSV files

import os

import csv


import_file = os.path.join('Resources','budget_data.csv')
export_file = os.path.join('analysis','budget_analysis.csv')


# Variables for tracking calculation data

total_mths = 0
net_PandL = 0
net_chg_list = []
net_chg_mth =[]



# Reading CSV File using CSV module

# Read CSV into a Dictionary
with open(import_file, encoding='utf-8') as import_data:

    # CSV reader specifies delimiter and variable that holds contents
 
    csv_read= csv.reader(import_data, delimiter=',')

    # Read the header row 
    header = next(csv_read)
    print(f"CSV Header: {header}")

    first_row = next(csv_read)
    total_mths += 1
    net_PandL += int(first_row[1])
    prev_net_PandL = int (first_row[1])

    for row in csv_read:

        total_mths += 1
        net_PandL =  int(row[1])

        #Tracking the net change
        net_chg = int(row[1]) - prev_net_PandL
        prev_net_PandL = int(row[1])
        net_chg_list += [net_chg]
        net_chg_mth += [row[0]]

    print (net_chg_list)
    print (net_chg_mth)
    print(total_mths)
    print(net_PandL)








    csv_data_dict = {}
    
    csv_data_dict = {rows[0]:int(rows[1]) for rows in csv_data}
print(csv_data_dict)






with open(import_file, encoding='utf-8') as csv_file:

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
with open(import_file, encoding='utf-8') as csv_file:

    #Prints Wrapper DEL
    #Print (csv_file) DEL

    # CSV reader specifies delimiter and variable that holds contents
    #csv_reader is the data
    csv_data = csv.reader(csv_file, delimiter=',')
    total = 0
    
    for row in csv_data:
        if not str(row[1]).startswith('P'):
            total = total + int(row[1])
    print("Total: $" + str(total))

#-----------------------------------------------------------------------------------

    
