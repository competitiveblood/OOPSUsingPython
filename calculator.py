first = input("Enter first number: ")
second = input("Enter second number: ")
first = int(first)
second = int(second)
print("----press keys for operator (+, -, *, /, %)----------")
operator = input("Enter operator: ")

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    if second != 0:  # Check for division by zero
        print(first / second)
    else:
        print("Division by zero is not allowed")
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operation")
