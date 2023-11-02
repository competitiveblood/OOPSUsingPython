#Program the print the area of 2 rectangles having side (3,5) and (4,7) by creating a class "Rectangle" and
#creating method area and pass the parameters length and breadth to its constructor

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
