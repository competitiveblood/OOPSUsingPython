def calculator():
    print("Welcome to the calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Addition")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("The sum is", a + b)
    elif choice == 2:
        print("Subtraction")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("The difference is", a - b)
    elif choice == 3:
        print("Multiplication")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("The product is", a * b)
    elif choice == 4:
        print("Division")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print("The quotient is", a / b)
    elif choice == 5:
        print("Exit")
    else:
        print("Invalid choice")



