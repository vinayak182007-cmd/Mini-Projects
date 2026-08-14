import add_data


# Initial Comment
print('Expense Tracker is Initiated')


def menu():
    while True:

        print('**'*25, 'Expense Tracker', '**'*25)
        print('Please select an option from Menu:')
        print('_'*70)
        print('| 1 = Add Expense | 2 = View Expenses | 3 = Total Expenses | 4 = Exit |')
        print('_'*70)

        selected_option = int(input('Enter your option --> '))
        if selected_option not in [1,2,3]:
            print('Invalid Input')
            print(menu())
        elif selected_option == 1:
            add_data.add_expense()
        elif selected_option == 2:
            import print_data
        elif selected_option == 3:
            import totaling
        elif selected_option == 4:
            print('Exiting Program. Goodbye!')
            exit()

print(menu())
