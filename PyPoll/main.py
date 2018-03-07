#Import the libraries
import csv
import os
import pandas as pd
import numpy as py


votes=[] #declaring Votes array to store veoter ID so we can track no.of Votes
percentage = [] #declaring this array to store percentages for each candiadate in the poll
candidates=[] #declaring this array to store the candidates colomun
final_candidates=[] #declaring this array to store the unique candiadate in the election
candidates_count=[] # declaring this array to store the no.of votes pe candidate

output = open("outputfile.txt","w")

election_data_path = os.path.join("raw_data", "election_data_1.csv") # declaring the path for the raw data we have

print("Election Results")
output.writelines("Election Results")
print("----------------------------")
output.writelines("\n" + "----------------------------------------")

with open(election_data_path, newline="") as csvfile:
    election_data = csv.reader(csvfile, delimiter = ",")

    next(election_data,None)

    for row in election_data:
        candidates.append(row[2])
        votes.append(row[0])
    total_votes = len(votes)
    print("Total Votes:" + str(total_votes))
    output.writelines("\n" + "Total Votes:" + str(total_votes))
    print("----------------------------------")
    output.writelines("\n" + "----------------------------------------")

    for i in candidates:
        if i not in final_candidates:
            final_candidates.append(i)
    for j in range(len(final_candidates)):
            candidates_count.append(candidates.count(final_candidates[j]))
            percentage.append((candidates_count[j]/total_votes)*100)
            print(final_candidates[int(j)]+ " : " + str(candidates_count[int(j)]) + " ( " + str("{0:.2f}%".format(percentage[j])) + " ) ")
            output.writelines("\n" + final_candidates[int(j)]+ " : " + str(candidates_count[int(j)]) + " ( " + str("{0:.2f}%".format(percentage[j])) + " ) ") 

    winner = max(candidates)
    print("----------------------------------")
    output.writelines("\n" + "----------------------------------------")
    print("Winner:" + winner)
    output.writelines("\n" + "Winner:" + winner)
    print("----------------------------------")
    output.writelines("\n" + "----------------------------------------")





