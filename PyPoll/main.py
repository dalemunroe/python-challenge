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
max_candidate_count = ["",0]


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

    #print(total_votes_cast)
    #print(candidates_list)



#------------------------------------------------------------------------------
#Candidate calculation inside candidate_list loop


    candidate_percentage_list = []
    candidate_count_list = []

for candidate in candidates_list:


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


        percentage_of_votes = str(round(candidate_count / total_votes_cast * 100, 3)) + "%"
        #print(percentage_of_votes)
        candidate_percentage_list.append(percentage_of_votes)
        #print(candidate_percentage_list)
        candidate_count_list.append(candidate_count)
                
        #MWinning Candidate
        if candidate_count > max_candidate_count [1]:   #tests if the value is greater and if true, 
            max_candidate_count  [0] = candidate        #returns the Winners Name row 1
            max_candidate_count [1] = candidate_count  #returns the Number of Votes to row 2

        #reset the counts to 0
        percentage_of_votes = 0
        candidate_count = 0

        #print(candidate_percentage_list)        
        #print(candidate_count_list)
        #print(max_candidate_count)

report_list = zip(candidates_list, candidate_percentage_list, candidate_count_list)

#for name in report_list:
#    print(name)

#-------------------------------------------------------------------------------

# Write to Screen

print("")
print("")
print("Election Results: ")
print("-"*40)
print("Total Votes Cast: " + str(total_votes_cast))
print("-"*40)

for name in report_list:
    print(str(name[0]) + ":   " + str(name[1]) + "  (" + str(name[2])+ ")")

print("-"*40)
print ("Winner: " + max_candidate_count[0])
print("-"*40)

#-------------------------------------------------------------------------------

# Write *.txt file

lines = ["Election Results: ", "-"*80, "Total Votes Cast: " + str(total_votes_cast), "-"*80, str(name[0]) + ":   " + str(name[1]) + "  (" + str(name[2])+ ")", "-"*80, "Winner: " (max_candidate_count[0]), "-"*80]
with open(export_file, 'w') as datafile:
    for line in lines:
        datafile.write(line)
        datafile.write('\n')
