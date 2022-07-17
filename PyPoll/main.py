#Week 3 Assignment - Python
# Pypoll
#Dale Munroe

#Module for reading CSV files

from cmath import exp
from fileinput import close
import os

import csv


import_file = os.path.join('Resources','election_data.csv')
export_file = os.path.join('analysis','election_analysis.txt')

# Variables for tracking calculation data

total_votes_cast = 0

candidates_list = []
candidate_votes = []



# Read CSV into a Dictionary
with open(import_file, encoding='utf-8') as import_data:

    # CSV reader specifies delimiter and variable that holds contents
 
    csv_read= csv.reader(import_data, delimiter=',')

    # Read the header row 
    header = next(csv_read)
    #print(f"CSV Header: {header}")

    for row in csv_read:

        #count total number of votes
        total_votes_cast += 1

        candidate = str(row[2])
        if candidate not in candidates_list:
            candidates_list.append(row[2])

    print(candidates_list)


#-----------------------------------------------------------------------
#option 1 

# Read CSV into a Dictionary
with open(import_file, encoding='utf-8') as import_data:
 
    # CSV reader specifies delimiter and variable that holds contents
 
    csv_read= csv.reader(import_data, delimiter=',')

    # Read the header row 
    header = next(csv_read)
    #print(f"CSV Header: {header}")
    #   
    candidate_count_list = []
    candidate_count = 0

    for row in csv_read:
        for candidate in candidates_list:
            candidate_count += 1
        candidate_count_list.append(candidate_count)
        candidate_count = 0
    print(candidate_count_list)

#------------------------------------------------------------------------------
#option 2


# Read CSV into a Dictionary
with open(import_file, encoding='utf-8') as import_data:
 
    # CSV reader specifies delimiter and variable that holds contents
 
    csv_read= csv.reader(import_data, delimiter=',')

    # Read the header row 
    header = next(csv_read)
    #print(f"CSV Header: {header}")
    #   
    candidate_count_list = []

    for row in csv_read:     

        candidate_count = 0
        candidate_name = str(row[2])
        
        for candidate in candidates_list:
            if candidate_name == csv_read(row[2]):
                candidate_count += 1
            print(candidate_count)

    print(candidate)
    candidate_count_list.append(candidate_count)

print(candidate_count_list)



#------------------------------------------------------------------------------
#option 3


for candidate in candidates_list:

    candidate_count_list = []
    candidate_count = 0

# Read CSV into a Dictionary
    with open(import_file, encoding='utf-8') as import_data:
 
        # CSV reader specifies delimiter and variable that holds contents
 
        csv_read= csv.reader(import_data, delimiter=',')

        #Read the header row 
        header = next(csv_read)
        #print(f"CSV Header: {header}")

        for row in csv_read:
            if candidate == row[2]:
                candidate_count += 1

        #print(candidate_count)
        candidate_count_list.append(candidate_count)
        
    print(candidate_count_list)




















print("Election Results: ")
print("-"*80)
print("Total Votes Cast: " + str(total_votes_cast))
print("-"*80)