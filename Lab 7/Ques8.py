#Program to add to distances in inch-feet by creating a class "AddDistance"

class AddDistance:
    def __init__(self):
        self.feet = 0
        self.inches = 0

    def set_distance(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def add_distance(self, feet, inches):
        self.feet += feet
        self.inches += inches
        if self.inches >= 12:
            self.feet += self.inches // 12
            self.inches %= 12

    def get_distance(self):
        return f"{self.feet} feet {self.inches} inches"

# Create an instance of the AddDistance class
distance_calculator = AddDistance()

# Set the first distance
feet1 = int(input("Enter feet for the first distance: "))
inches1 = int(input("Enter inches for the first distance: "))
distance_calculator.set_distance(feet1, inches1)

# Set the second distance
feet2 = int(input("Enter feet for the second distance: "))
inches2 = int(input("Enter inches for the second distance: "))
distance_calculator.add_distance(feet2, inches2)

# Get and print the total distance
total_distance = distance_calculator.get_distance()
print(f"Total Distance: {total_distance}")
