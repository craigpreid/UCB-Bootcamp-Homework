import csv

filenames = ['employee_data1.csv', 'employee_data2.csv']
with open('output_file.csv', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())
