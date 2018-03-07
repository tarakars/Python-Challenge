# Import Libraries
import csv
import os

#declaring the path for the file we read data from
employee_data_path = os.path.join("raw_data", "employee_data1.csv")

# declaring arrays to store columns and results from doing other operations
employee_id=[]
first_name = []
last_name=[]
dob=[]
ssn=[]
state=[]

#creating a library for the states and their abbrevations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#opening the file we read
with open (employee_data_path, newline ="") as csvfile:
    employee_data = csv.reader(csvfile,delimiter=",") # reading the CSV in to a variable

    next(employee_data,None) #skipping the first row because the first row is header
    
    #creating a for loop to lopp thru all the data we read
    for row in employee_data:
        employee_id.append(row[0]) # appending the 1st value in each row to employee ID array
        name = row[1].split(" ") # inorder to get the first and last name we are using split function
        first_name.append(name[0]) #appending the 0th value in the name array after we split the name
        last_name.append(name[1]) #appending the 1st value in the name array after we split the name
        dob.append(row[2]) # appending the 3rd value of every row from the data we read
        temp_ssn = row[3].split("-") # creating a temp SSN so we can split the data using - so we can mask first 6 digits
        temp_ssn[0] = "***" #replacing first 3 digits with astricks for every SSN in the data
        temp_ssn[1] = "***" #replacing first 3 digits with astricks for every SSN in the data
        encoded_ssn = "-" .join (temp_ssn) # joining the SSn we split and masked in to a new variable
        ssn.append(encoded_ssn) # appending the SSNs we encoded in to an array
        state.append(us_state_abbrev[row[4]]) # appening the state codes using the library we created above
    Pyboss_csv = zip(employee_id,first_name,last_name,dob,ssn,state) # zipping all the arrays
    Pyboss_csv_path = os.path.join("Pyboss.csv") # creating a new path and CSV file
    with open(Pyboss_csv_path,"w") as csvfile: # opening the file to write 'w' represents write function
        writer = csv.writer(csvfile) # writing the csv file using a variable
        writer.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN", "State"]) # writing the first row as a header
        writer.writerows(Pyboss_csv) # writing all other rows using the zipped file pyboss_csv