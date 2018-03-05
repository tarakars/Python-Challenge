import csv
import os

employee_data_path = os.path.join("raw_data", "employee_data1.csv")

employee_id=[]
first_name = []
last_name=[]
dob=[]
ssn=[]
state=[]
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


with open (employee_data_path, newline ="") as csvfile:
    employee_data = csv.reader(csvfile,delimiter=",")

    next(employee_data,None)
    
    for row in employee_data:
        employee_id.append(row[0])
        name = row[1].split(" ")
        first_name.append(name[0])
        last_name.append(name[1])
        dob.append(row[2])
        temp_ssn = row[3].split("-")
        temp_ssn[0] = "***"
        temp_ssn[1] = "***"
        encoded_ssn = "-" .join (temp_ssn)
        ssn.append(encoded_ssn)
        state.append(us_state_abbrev[row[4]])
    Pyboss_csv = zip(employee_id,first_name,last_name,dob,ssn,state)
    Pyboss_csv_path = os.path.join("Pyboss.csv")
    with open(Pyboss_csv_path,"w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Employee ID", "First Name", "Last Name", "DOB", "SSN", "State"])
        writer.writerows(Pyboss_csv)