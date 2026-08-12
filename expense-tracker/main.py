import add_data


# Initial Comment
print('Expense Tracker is Initiated')
print('**'*25, 'Expense Tracker', '**'*25)


print('Please select an option from Menu:')
print('_'*50)
print('| 1 = Add Expense | 2 = View Expenses | 3 = Exit |')
print('_'*50)

selected_option = input('Enter your option --> ')

if selected_option == '1':
    add_data.add_expense()
if selected_option == '2':
    import print_data
if selected_option == '3':
    print('Exiting the program. Goodbye!')
    exit()
