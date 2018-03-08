# First is first, Import the libraries
import csv
import os
import pandas as pd
import numpy as py


votes=[] #declaring Votes array to store veoter ID so we can track no.of Votes
percentage = [] #declaring this array to store percentages for each candiadate in the poll
candidates=[] #declaring this array to store the candidates colomun
final_candidates=[] #declaring this array to store the unique candiadate in the election
candidates_count=[] # declaring this array to store the no.of votes pe candidate

output = open("outputfile.txt","w") #created and opened a text file to write the results. 'w' denote the write function

election_data_path = os.path.join("raw_data", "election_data_1.csv") # declaring the path for the raw data we have

#printing the sentences in command prompt usinf print function and output.writelines is used to write the result in text file
print("Election Results")
output.writelines("Election Results")
print("----------------------------")
output.writelines("\n" + "----------------------------------------")

with open(election_data_path, newline="") as csvfile: #opening thr CSV file
    election_data = csv.reader(csvfile, delimiter = ",") #reading the CSV file in to a list

    next(election_data,None) # skipping thr first row to make sure we dont count header in the analysis

    #looping through the data we read in the list to do the calculations
    for row in election_data:
        candidates.append(row[2]) # appending the 3rd value of election_data to another list called candidates
        votes.append(row[0]) # appending the 1st value in the eletiond_data list to a new list called votes
    total_votes = len(votes) #using len function to get the lenght of the votes list, so that we get total no.of votes
    print("Total Votes:" + str(total_votes)) # printing the total votes we stored
    output.writelines("\n" + "Total Votes:" + str(total_votes)) # writing the total votes in a text file
    print("----------------------------------")
    output.writelines("\n" + "----------------------------------------")

    #looping through the array(candidates), we created to get the unique candidates
    for i in candidates:
        if i not in final_candidates: # condition to check if the candidate is already in the final candidate list
            final_candidates.append(i) #if the candidate is not in the list appending them to the final candidates list

    #loping through the range of 1 to the length of final candidates to get the no of votes per person
    for j in range(len(final_candidates)):
            candidates_count.append(candidates.count(final_candidates[j])) # appending the votes per candidate in the candidates_count array by using count funcion
            percentage.append((candidates_count[j]/total_votes)*100) # calculating the percentage of votes a candidate accquired
            print(final_candidates[int(j)]+ " : " + str(candidates_count[int(j)]) + " ( " + str("{0:.2f}%".format(percentage[j])) + " ) ") # printing all the results for each candidate
            output.writelines("\n" + final_candidates[int(j)]+ " : " + str(candidates_count[int(j)]) + " ( " + str("{0:.2f}%".format(percentage[j])) + " ) ") 

    winner = max(candidates) # getting the winner of the election by determining how many times the same canidate has been voted by using candidate array
    print("----------------------------------")
    output.writelines("\n" + "----------------------------------------")
    print("Winner:" + winner) # printing the winner
    output.writelines("\n" + "Winner:" + winner) # writing the winner in text file
    print("----------------------------------")
    output.writelines("\n" + "----------------------------------------")





