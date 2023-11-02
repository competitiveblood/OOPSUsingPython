#Design a calculator by creating a class "Calculator" with separate method for each operation

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero."

# Create an instance of the Calculator class
calculator = Calculator()

# Perform calculations using the calculator's methods
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Addition:", calculator.add(num1, num2))
print("Subtraction:", calculator.subtract(num1, num2))
print("Multiplication:", calculator.multiply(num1, num2))
print("Division:", calculator.divide(num1, num2))
