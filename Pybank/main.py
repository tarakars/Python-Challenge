# first is first - Import Libraries 
import csv
import os
import pandas as pd
import numpy

revenue=[] # declare and array to store revenue as a list from the csv file
date=[] # declare and array to store date as a list from the csv file
rev_change=[] # declare and array to store change in revenue as list

print("Financial Analysis")
print("------------------------------------------------------------------")


budget_data_path = os.path.join("raw_data","budget_data_1.csv") # declaring the path for the CSV

with open(budget_data_path,newline="") as csvfile: # making sure our operations are done while opening the CSV
    budget_data = csv.reader(csvfile, delimiter = ",") # reading the csv file in to an object

    next(budget_data,None) # skipping the first row to avoid header in math operations below

    for row in budget_data: # creating a loop through the csv and create two arrays revenue and date
        revenue.append(float(row[1]))
        date.append(row[0])
    print("Total number of months:" + str(len(date))) # len function is used to get the length of the array so we know how many months we have
    print("Total Revenue:" + str(sum(revenue))) # sum function is used to get the sum of the array so we know the revenue

    for i in range(1,len(revenue)): # creating a loop through the revenue array to calculate the average revenue change
        rev_change.append(revenue[i] - revenue[i-1])
    average_rev_change = sum(rev_change)/len(rev_change)
    print("average revenue change:" + str(average_rev_change))

    max_increase = max(rev_change) # max function is used to get the max value in the revenue change for the greatest increase in revenue in each month
    max_decrease = min(rev_change) # min function is used to get the max value in the revenue change for the greatest decrease in revenue in each month
    print("Greatest Increase in the revenue:" + str(max_increase))
    print("Greatest Decrease in the revenue:" + str(max_decrease))


