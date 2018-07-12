import os
import csv
import math

# Path to collect data from the Resources folder
budgetcsv = os.path.join('Resources', 'budget_data.csv')

#Define variables
row_count = 0
total_revenue = 0
greatest_increase = 0
greatest_decrease = 0

# Read in the CSV file
with open(budgetcsv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
   
    for row in csvreader:
      row_count = row_count + 1
      total_revenue = total_revenue + int(row[1])

      if int(row[1]) > greatest_increase:
        greatest_increase = int(row[1])
        increase_month = str(row[0])

      if int(row[1]) < greatest_decrease:
        greatest_decrease = int(row[1])
        decrease_month = str(row[0])

#Return integer for average value so it looks good
average = int(total_revenue/row_count)


print(f"Finanacial Analysis")
print("-------------------")
print("Total Months: ", str(row_count))
print("Total Revenue: ", str(total_revenue))
print("Average Change: ", str(average))
print("Greatest Increase in Profits: ", str(increase_month)," ", str(greatest_increase))
print("Greatest Decrease in Profits: ", str(decrease_month)," ", str(greatest_decrease))


f = open("Output/PyBank.txt","w")
f.write('Finanacial Analysis' + '\n')
f.write("-------------------" + '\n')
f.write("Total Months: " + str(row_count) + '\n')
f.write("Average Change: " + str(average) + '\n')
f.write("Greatest Increase in Profits: " + str(increase_month)+ " " + str(greatest_increase) + '\n')
f.write("Greatest Decrease in Profits: " + str(decrease_month)+ " " + str(greatest_decrease)) 
f.close()

