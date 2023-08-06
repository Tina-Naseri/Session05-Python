def hash_table_generator():
    # Print welcome message and instructions
    print("----Welcome to the #Hash Table Generator#----")
    print()
    print("--> Each cell of the table is represented by a # character.")
    print("--> To use the program, you have to provide two inputs: ")
    print("1. the number of rows")
    print("2. the number of columns")
    print()

    while True:
        start_exit = input("Enter 's' to start or 'e' to exit: ")

        # If user wants to start:
        if start_exit == "s":
            rows = int(input("The number of rows: "))
            columns = int(input("The number of columns: "))
            for i in range(rows):
                for i in range(columns):
                    print("#", end=" ")
                print()

        # If user wants to exit, break out of loop
        elif start_exit == "e":
            break

        # If user inputs invalid option, print error message
        else:
            print("Invalid input! Please enter 's' to start or 'e' to exit")
            print()


hash_table_generator()
