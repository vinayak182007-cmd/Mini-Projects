import csv

with open('expenses.csv', mode='r') as file:
    csv_data= csv.reader(file)
    data_list=[]
    for row in csv_data:
        data_list.append(row)

    for data in data_list:
        print(data)