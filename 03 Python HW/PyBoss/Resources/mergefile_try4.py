#Import Libraries 
import glob
import csv
import os
from datetime import datetime

### Merge two csv files from a directory
directory = "Directory" 

### Merge file procedure
to_merge = glob.glob(directory+"/*.csv")
to_merge.sort()
header_saved = False
outputfile = "Output/Merged_File.csv"
with open(outputfile,'w', encoding = 'utf-8-sig') as mergedfile:
    for filename in to_merge:
        with open(filename, encoding = 'utf-8-sig') as infiles:
            header = next(infiles)
            if not header_saved:
                mergedfile.write(header)
                header_saved = True
            for line in infiles:
                mergedfile.write(line)
                
# combined file = "Merged_File.csv"
#--------------------------------------------------------------

# load merged files as csvfile:
merged_csv = "Output/Merged_File.csv"

# load target column names
first_name = []
last_name = []
dob = []
ssn = []
state = []

#dictionary to abbreviate the state
stateabbrev = {
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

# open the merged_csv file and read into rows
with open(merged_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)

    for row in csvreader:
        split_name = row[1].split(" ")
        first_name.append(split_name[0])

        last_name.append(split_name[0])# for some reason split_name[1] does not work

        dob.append(str(row[2])) #I tried a crazy way to change dates.  Don't know how at all.
                                #I thought of using split, but I can't get it to work when it's simple

        split_ssn = str(row[3]).split("-")
        ssn.append("XXX-XX-" + split_ssn[0]) #this should be last for split_ssn[2] but I can't make it work

        newword =str(row[4])
        #state.append(stateabbrev[newword]) #I can't get the dictionary to work
        state.append("any state")

    cleaned_csv = zip(first_name, last_name, dob, ssn, state)

# Set variable for output file
output_file = os.path.join("Output/pyboss_final.csv")
		
# Open the output file
	
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["First Name", "Last Name", "DOB", "SSN",
    "State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
    
        
