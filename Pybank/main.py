# first is first - Import Libraries 
import csv
import os
import sys

revenue=[] # declare and array to store revenue as a list from the csv file
date=[] # declare and array to store date as a list from the csv file
rev_change=[] # declare and array to store change in revenue as list


#print("Financial Analysis")
#print("----------------------------------------")


budget_data_path = os.path.join("raw_data","budget_data_1.csv") # declaring the path for the CSV
with open(budget_data_path,newline="") as csvfile: # making sure our operations are done while opening the CSV
    budget_data = csv.reader(csvfile, delimiter = ",") # reading the csv file in to an object

    next(budget_data,None) # skipping the first row to avoid header in math operations below

    for row in budget_data: # creating a loop through the csv and create two arrays revenue and date
        revenue.append(float(row[1]))
        date.append(row[0])
    no_of_months = len(date)
    sum_revernue = sum(revenue)
    #print("Total number of months:" + str(no_of_months)) # len function is used to get the length of the array so we know how many months we have
    #print("Total Revenue:" + str(sum_revernue)) # sum function is used to get the sum of the array so we know the revenue

    for i in range(1,len(revenue)): # creating a loop through the revenue array to calculate the average revenue change
        rev_change.append(revenue[i] - revenue[i-1])
    average_rev_change = sum(rev_change)/len(rev_change)
    #print("average revenue change:" + str(average_rev_change))
    max_increase = max(rev_change) # max function is used to get the max value in the revenue change for the greatest increase in revenue in each month
    max_decrease = min(rev_change) # min function is used to get the max value in the revenue change for the greatest decrease in revenue in each month
    #print("Greatest Increase in the revenue:" + str(max_increase))
    #print("Greatest Decrease in the revenue:" + str(max_decrease))

financial_analysis = (
    f"\nFinancial Analysis"
    f"\n----------------------------------------"
    f"\nTotal number of months: {no_of_months}" # len function is used to get the length of the array so we know how many months we have
    f"\nTotal Revenue: {sum_revernue}" # sum function is used to get the sum of the array so we know the revenue
    f"\naverage revenue change: {average_rev_change}"
    f"\nGreatest Increase in the revenue: {max_increase}"
    f"\nGreatest Decrease in the revenue: {max_decrease}"

)
print(financial_analysis,end = "")

sys.stdout = open("outputfile.txt", 'w')
print(financial_analysis)




#creating a text file and writing our outputs in the file
#output = open("outputfile.txt","w")
#output.writelines("Financial Analysis")
#output.writelines("\n" + "----------------------------------------")
#output.writelines("\n" + "Total number of months:" + str(len(date)))
#output.writelines("\n" + "Total Revenue:" + str(sum(revenue)))
#output.writelines("\n" + "average revenue change:" + str(average_rev_change))
#output.writelines("\n" + "Greatest Increase in the revenue:" + str(max_increase))
#output.writelines("\n" + "Greatest Decrease in the revenue:" + str(max_decrease))








