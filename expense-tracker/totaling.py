import csv

def total_expense():
    total= 0.0
    exp_list=[]
    with open("expenses.csv",'r') as csv_file:
        csv_data= list(csv.reader(csv_file))

        for row in csv_data[1:]:
            exp_list.append(row[1:])

    for expense in exp_list:
        for data in expense:
            total += float(data)
    return f'Total Expenses: ${total}'

print(total_expense())