#Week 3 Assignment - Python
#Dale Munroe

#Module for reading CSV files

from cmath import exp
from fileinput import close
import os

import csv


import_file = os.path.join('Resources','budget_data.csv')
export_file = os.path.join('analysis','budget_analysis.txt')


# Variables for tracking calculation data

total_mths = 0
net_PandL = 0
net_chg_list = []
net_chg_mth =[]
max_profit_increase = ["",0]
max_profit_decrease = ["",999999999999]

# Reading CSV File using CSV module

# Read CSV into a Dictionary
with open(import_file, encoding='utf-8') as import_data:

    # CSV reader specifies delimiter and variable that holds contents
 
    csv_read= csv.reader(import_data, delimiter=',')

    # Read the header row 
    header = next(csv_read)
    #print(f"CSV Header: {header}")


    #Remove first row, before populating net change list
    first_row = next(csv_read)
    #print(first_row)
    

    total_mths += 1                         #adds back 1 to the counter  
    net_PandL += int(first_row[1])          #adds the skipped 1st row to the net
    prev_net_PandL = int (first_row[1])     #set 1st P&L value for average calc

    for row in csv_read:

        total_mths += 1                     #iteration month counter
        net_PandL +=  int(row[1])           #iteration Sum P&L 

        #Tracking the net change
        net_chg = int(row[1]) - prev_net_PandL  #calculate the changes in P&L 
        prev_net_PandL = int(row[1])            #set the previous month value 
        net_chg_list += [net_chg]               #add net change to a list
        net_chg_mth += [row[0]]                 #add month to a list

        #Maximum increase
        if net_chg > max_profit_increase [1]:   #tests if the value is greater and if true, 
            max_profit_increase [0] = row[0]    #returns the month TO row 1
            max_profit_increase [1] = net_chg   #returns the value TO row 2

        #Maximum decrease
        if net_chg < max_profit_decrease [1]:   #tests if the value is greater and if true,
            max_profit_decrease[0] = row[0]     #returns the month TO row 1
            max_profit_decrease[1] = net_chg    #returns the value TO row 2

    # Calculate average Net Change and rounds to 2 dec places

    net_mthly_avg = round(sum(net_chg_list) / len(net_chg_list), 2)



    print("Financial Analysis")
    print("-"*80)
    print("Total Months: " + str(total_mths))
    print("Total: " + str(net_PandL))
    print("Average Change: " + str(net_mthly_avg))
    print("Greatest Increase in Profits: " + str(max_profit_increase))
    print("Greatest_Decrease in Profits: " + str(max_profit_decrease))





#-------------------------------------------------------------------------------

# Open the file in "read" mode ('r') and store the contents in the variable "text"
with open(export_file, 'w') as f:
    output = (
        f.write("Financial Analysis")
        f.write("-"*80)
        f.write("Total Months: " + str(total_mths))
        f.write("Total: " + str(net_PandL))
        f.write("Average Change: " + str(net_mthly_avg))
        f.write("Greatest Increase in Profits: " + str(max_profit_increase))
        f.write("Greatest_Decrease in Profits: " + str(max_profit_decrease))
        f.close()
    )


report_text = (
    print("Financial Analysis")
    print("-"*80)
    print("Total Months: " + str(total_mths))
    print("Total: " + str(net_PandL))
    print("Average Change: " + str(net_mthly_avg))
    print("Greatest Increase in Profits: " + str(max_profit_increase))
    print("Greatest_Decrease in Profits: " + str(max_profit_decrease))
)