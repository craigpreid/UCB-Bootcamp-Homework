import os
import csv

# Path to collect data from the Resources folder
resultscsv = os.path.join('Resources', 'election_data.csv')

#Define variables
total_votes = 0
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

# Read in the CSV file
with open(resultscsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
   
   #count the votes for each candidate row by row and get total
    for row in csvreader:
        total_votes = int(total_votes + 1)
        
        if str(row[2])== "Khan":
            khan_count = khan_count + 1
        elif str(row[2])== "Correy":
            correy_count = correy_count + 1
        elif str(row[2])== "Li":
            li_count = li_count + 1
        elif str(row[2])== "O'Tooley":
            otooley_count = otooley_count + 1

#Determine percentage and format output for each candidate
khan_portion = (khan_count/total_votes)*100 # this was the first line for testing the alogrithm
khan_portion = str(format(khan_portion, ',.3f'))
correy_portion = format((correy_count/total_votes)*100,'.3f')
li_portion = format((li_count/total_votes)*100,'.3f')
otooley_portion = format((otooley_count/total_votes)*100,'.3f')

#print results to terminal
print("Election Results")
print("--------------------------------")
print("Total Votes: " + str(format(total_votes, ',')))
print("--------------------------------")
print("Kahn:        " + str(khan_portion) +"%"+"("+ str(format(khan_count,','))+" votes)")
print("Correy:      " + str(correy_portion) +"%"+"  ("+ str(format(correy_count,','))+" votes)")
print("Li:          " + str(li_portion) +"%"+"  ("+ str(format(li_count,','))+" votes)")
print("O'Tooley:     " + str(otooley_portion) +"%"+"  ("+ str(format(otooley_count,','))+" votes)")

#print to txt file
f = open("Output/election_results.txt","w")
f.write("Election Results" +"\n")
f.write("-------------------------"+"\n")
f.write("Total Votes: " + str(format(total_votes,","))+"\n")
f.write("-------------------------" + "\n")
f.write("Kahn:        " + str(khan_portion) +"%"+"("+ str(format(khan_count,','))+" votes)"+"\n")
f.write("Correy:      " + str(correy_portion) +"%"+"  ("+ str(format(correy_count,','))+" votes)"+"\n")
f.write("Li:          " + str(li_portion) +"%"+"  ("+ str(format(li_count,','))+" votes)"+"\n")
f.write("O'Tooley:     " + str(otooley_portion) +"%"+"  ("+ str(format(otooley_count,','))+" votes)"+"\n")
    
f.close()

