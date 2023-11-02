#Assign and print 'Name', 'Regno', 'Subject', 'Mark' of 5 students


class Student:
    def __init__(self, name, regno):
        self.Name = name
        self.Regno = regno
        self.Subject = ""
        self.Mark = 0

# Create a list to store student objects
students = []

# Create 5 student objects and add them to the list
for i in range(1, 6):
    name = input(f"Enter Name for Student {i}: ")
    regno = int(input(f"Enter Regno for Student {i}: "))
    student = Student(name, regno)
    students.append(student)

# Assign and print 'Subject' and 'Mark' for each student
for student in students:
    student.Subject = input(f"Enter Subject for {student.Name}: ")
    student.Mark = float(input(f"Enter Mark for {student.Name}: "))

# Print the details of all 5 students
for student in students:
    print(f"Name: {student.Name}")
    print(f"Regno: {student.Regno}")
    print(f"Subject: {student.Subject}")
    print(f"Mark: {student.Mark}")
    print()
