#Import modules
import os
import csv
from statistics import mean

#Define variables
total_voters = 0
candidates = {}
percentage = {}

#Find file
csvpath = os.path.join("/Users/Juango/Desktop/Python-challenge/PyPoll/election_data.csv")

#Open file
with open(csvpath, "r") as file:
    reader = csv.reader(file)
    header = next(reader)

#Create dictionary of candidates, their vote counts, and total votes
    for row in reader:
        total_voters += 1
        candidate_name = row[2]  
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

#Print Election Results
print("Election Results")
print("-----------------")

#Print total number of votes
print(f"Total Votes: {total_voters}")
print("-----------------")

#Loop dictionary and print candidates' vote percentages and votes  
for candidate, votes in candidates.items():
    percentage = (votes / total_voters) *100
    print(f'{candidate}: {percentage:.2f}% ({votes})')
print("-----------------")

#Find and print the winner 
print(f'Winner: {max(candidates, key=candidates.get)}')
print("-----------------")

#Export Election Results as a txt file
with open("Election Results.txt", "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-----------------\n")
    output_file.write(f"Total Votes: {total_voters}\n")
    output_file.write("-----------------\n")
    
#Export percentage as loop
    for candidate, votes in candidates.items():
        percentage = (votes / total_voters) *100
        output_file.write(f'{candidate}: {percentage:.2f}% ({votes})\n')

    output_file.write("-----------------\n")
    output_file.write(f'Winner: {max(candidates, key=candidates.get)}\n')
    output_file.write("-----------------")