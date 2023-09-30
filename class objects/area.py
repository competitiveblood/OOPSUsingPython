class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

rectangle1 = Rectangle(3, 5)
rectangle2 = Rectangle(4, 9)


area1 = rectangle1.area()
print(f"The area of the first rectangle is: {area1}")


area2 = rectangle2.area()
print(f"The area of the second rectangle is: {area2}")
