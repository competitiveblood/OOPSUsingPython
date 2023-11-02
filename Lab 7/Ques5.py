#Same as 4) but without having any parameter in its constructor

class Rectangle:
    def __init__(self):
        self.length = 0  # Initialize the length to 0
        self.breadth = 0  # Initialize the breadth to 0

    def set_dimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Create two rectangle objects and set their dimensions
rectangle1 = Rectangle()
rectangle1.set_dimensions(3, 5)

rectangle2 = Rectangle()
rectangle2.set_dimensions(4, 7)

# Calculate and print the area of the two rectangles
area1 = rectangle1.area()
area2 = rectangle2.area()

print(f"Area of Rectangle 1: {area1}")
print(f"Area of Rectangle 2: {area2}")
