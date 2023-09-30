class Triangle:
    base = 10
    height = 20

    def area(self):
        return self.base * self.height / 2

    def perimeter(self):
        return self.base + 2 * self.height

# Create an object of the class
t1 = Triangle()

# Print the area and perimeter
print(f"The area of the triangle is: {t1.area()}")
print(f"The perimeter of the triangle is: {t1.perimeter()}")