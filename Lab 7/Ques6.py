#Program to print the average of 3 numbers entered by creating a class "Average" having a method to calculate and
#print the average

class Average:
    def __init__(self):
        self.numbers = []

    def get_numbers(self):
        for i in range(3):
            number = float(input(f"Enter number {i + 1}: "))
            self.numbers.append(number)

    def calculate_average(self):
        if len(self.numbers) == 3:
            average = sum(self.numbers) / 3
            return average
        else:
            return None

    def print_average(self):
        average = self.calculate_average()
        if average is not None:
            print(f"The average of the three numbers is: {average}")
        else:
            print("Please enter exactly 3 numbers to calculate the average.")

# Create an instance of the Average class
average_calculator = Average()

# Get three numbers from the user
average_calculator.get_numbers()

# Calculate and print the average
average_calculator.print_average()
