import csv

f = open('employee_data1.csv')
csv_f = csv.reader(f)

name = []

for row in csv_f:
  name.append(row[1])

print (name)
