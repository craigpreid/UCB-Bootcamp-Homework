import csv

allFiles = ("employee_data1.csv", "employee_data2.csv")

df_out_filename = 'df_out.csv'
write_headers = True
with open(df_out_filename, 'wb') as fout:
    writer = csv.writer(fout)
    for filename in allFiles:
        with open(filename) as fin:
            reader = csv.reader(fin)
            csv_header = next(filename)
            if write_headers:
                write_headers = False  # Only write headers once.
                writer.writerow(headers)
            writer.writerows(reader)  # Write all remaining rows.
