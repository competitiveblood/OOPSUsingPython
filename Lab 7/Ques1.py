#create a class named student with a string variable "Name", integer variable "regno". Assign the regno as
#'20003902' and that of name "ABC" by creating an object

class Student:
    def __init__(self, name, regno):
        self.Name = name
        self.regno = regno

# Creating an object of the Student class with the specified values
student_object = Student("ABC", 20003902)

# Accessing the object's attributes
print("Name:", student_object.Name)
print("Registration Number:", student_object.regno)
