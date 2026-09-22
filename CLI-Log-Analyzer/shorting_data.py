# This script reads a CSV file containing web server access logs, extracts the first 1000 non-empty rows, and writes them to a new CSV file.

import csv


def extract_csv_data():
    with open('C:\Me\BSc\Self Initiated Projects\mini\log_analyser\web-server-access-logs.csv','r',encoding='utf-8') as file:
        csv_data = csv.reader(file)
        for row in csv_data:
            yield row

data = extract_csv_data()

req_data = []
n = 0
while n < 1000:
    try:
        row = next(data)
        # Ignore completely empty rows
        if row:
            req_data.append(row)
        n += 1
    except StopIteration:
        break


with open(
    r'C:\Me\BSc\Self Initiated Projects\mini\log_analyser\shorted_data.csv',
    'w',
    newline='',
    encoding='utf-8'
) as file:
    writer = csv.writer(file)
    writer.writerows(req_data)