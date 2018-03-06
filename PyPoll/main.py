# Import Libraries
import csv
import os
import pandas as pd
import numpy as py


votes=[]
percentage = []
candidates=[]
final_candidates=[]
candidates_count=[]

election_data_path = os.path.join("raw_data", "election_data_1.csv")

print("Election Results")
print("----------------------------")

with open(election_data_path, newline="") as csvfile:
    election_data = csv.reader(csvfile, delimiter = ",")

    next(election_data,None)

    for row in election_data:
        candidates.append(row[2])
        votes.append(row[0])
    total_votes = len(votes)
    print("Total Votes:" + str(total_votes))
    print("----------------------------------")

    for i in candidates:
        if i not in final_candidates:
            final_candidates.append(i)
    for j in range(len(final_candidates)):
            candidates_count.append(candidates.count(final_candidates[j]))
            percentage.append((candidates_count[j]/total_votes)*100)
            print(final_candidates[int(j)]+ " : " + str(candidates_count[int(j)]) + " ( " + str("{0:.0f}%".format(percentage[j])) + " ) ")     

    winner = max(candidates)
    print("----------------------------------")
    print("Winner:" + winner)
    print("----------------------------------")