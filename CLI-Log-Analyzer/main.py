import top_requested_url

def menu():
    print("Welcome to the CLI Log Analyzer!")
    print("Please select an option:")
    print("1. Find the top requested URL")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        file_path = input("Enter the path to the CSV file: ")
        analyzer = top_requested_url.TopRequestedURL(file_path)
        analyzer.fetch_top_requested_url()
    elif choice == '2':
        print("Exiting the program.")
        exit()
    else:
        print("Invalid choice. Please try again.")
        menu()

menu()
