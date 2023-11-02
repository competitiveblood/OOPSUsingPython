#Program to print the area and the perimeter of a triangle of having sides 3,4,5 units by creating a class triangle
#with constructor having 3 sides as a parameter


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Create two rectangle objects with different dimensions
rectangle1 = Rectangle(3, 5)
rectangle2 = Rectangle(4, 7)

# Calculate and print the area of the two rectangles
area1 = rectangle1.area()
area2 = rectangle2.area()

print(f"Area of Rectangle 1: {area1}")
print(f"Area of Rectangle 2: {area2}")
