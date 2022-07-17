#Week 3 Assignment - PyPoll
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
winner = ["",0]


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

    print(total_votes_cast)
    print(candidates_list)



#------------------------------------------------------------------------------
#Candidate calculation inside candidate_list loop


for candidate in candidates_list:

    candidate_percentage_list = []
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

        candidate_count_list.append(str(candidate_count))
        print(candidate_count_list)
        print(candidate_count)
        percentage_of_votes = str(round(candidate_count / total_votes_cast * 100, 3)) + "%"
        print(percentage_of_votes)
        candidate_percentage_list.append(percentage_of_votes)
        print(candidate_percentage_list)
        candidate_count_list.append(candidate_count)
        percentage_of_votes = 0
        candidate_count = 0

        #print(candidate_percentage_list)        
        #print(candidate_count_list)

report_list = zip(candidates_list, candidate_percentage_list, candidate_count_list)

for name in report_list:
    print(report_list)

#-------------------------------------------------------------------------------

# Write to Screen


print("Election Results: ")
print("-"*80)
print("Total Votes Cast: " + str(total_votes_cast))
print("-"*80)
print(report_list)
print("-"*80)
print ("Winner: " + winner)
print("-"*80)

#-------------------------------------------------------------------------------

# Write *.txt file

lines = ["Election Results: ", "-"*80, "Total Votes Cast: " + str(total_votes_cast), "-"*80, str(report_list), "-"*80, "Winner: " (winner), "-"*80]
with open(export_file, 'w') as datafile:
    for line in lines:
        datafile.write(line)
        datafile.write('\n')
