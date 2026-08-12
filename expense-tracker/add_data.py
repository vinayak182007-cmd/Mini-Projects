import csv

fields= ['Date', 'Expense Amount']

def add_expense():
   
   yno = int(input('Enter the Year: '))
   mno = int(input('Enter the Month (1 to 12): '))
   dof = int(input('Enter the Day of Month  (1 to 31): '))  

   if mno<1 or mno>12 or dof<1 or dof>31:
      print("Invalid date: Please enter a valid month (1-12) and day (1-31).")
      print(add_expense())
   elif mno in [4,6,9,11] and dof>30:
      print("Invalid date: This month has only 30 days.")
      print(add_expense()) 
   elif mno==2 and dof>29:
      print("Invalid date: February has only 28 or 29 days.")
      print(add_expense())    
   else:
      date= f"{yno}-{mno}-{dof}"

   def expense_entry():
      try:
         expense = int(input('Enter the expense amount: '))
      except ValueError:
         print("Invalid input. Please enter a valid expense amount.")
         print(expense_entry())
      return expense
         
   exp = expense_entry()
   values = [date, exp]

   with open('expenses.csv', mode='a', newline='') as file:
      csv_data= csv.writer(file)
      csv_data.writerow(values)
