def solve_quadratic_equation():
    # Print welcome message and instructions
    print("----Welcome to the Quadratic Equation Solver----")
    print()
    print("This program will solve quadratic equations of the form (ax^2 + bx + c = 0).")
    print()

    while True:
        start_exit = input("Enter 's' to start or 'e' to exit: ")

        # If user wants to start:
        if start_exit == "s":
            a = int(input("a: "))
            b = int(input("b: "))
            c = int(input("c: "))
            delta = b**2 - 4*a*c

            if a == 0:
                x = -c / b
                print(f"The equation has one real root: x = {x}")
                print()
            if delta < 0:
                print("The equation has no real roots.")
                print()
            elif delta == 0:
                x = -b / (2*a)
                print(f"The equation has one real root: x = {x}")
                print()
            elif delta > 0:
                x1 = (-b + delta**0.5) / (2*a)
                x2 = (-b - delta**0.5) / (2*a)
                print(
                    f"The equation has two real roots: x1 = {x1} and x2 = {x2}")
                print()

        # If user wants to exit, break out of loop
        elif start_exit == "e":
            break

        # If user inputs invalid option, print error message
        else:
            print("Invalid input! Please enter 's' to start or 'e' to exit")
            print()


solve_quadratic_equation()
