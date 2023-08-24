#circle is the class name 
#__init__ is the constructor name 
#radius and color are the attributes given 
#self.radius and self.color is the instance value given to the attributes 

class Circle(object):

    def __init__(self, radius=5, color="blue"):
        self.radius = radius
        self.color = color

    def add_rad(self, r):
        self.radius = self.radius + r
        return self.radius

# Creating an instance of the Circle class
S = Circle(10, 'red')

# Printing attributes of the instance
print(S.radius)
print(S.color)

# Calling the add_rad method
z = S.add_rad(20)

# Printing updated attributes
print(S.radius)
print(z)

OUTPUT of the code=
10
red
30
30
