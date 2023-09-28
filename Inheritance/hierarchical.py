#base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

#derived class1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

#derived class 2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")


#another example for hierarchical inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        return f"{self.name} is studying {subject}"

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self, topic):
        return f"{self.name} is teaching {topic}"

student = Student("John", 19, "102")
teacher = Teacher("Mary", 35, "Math")

print(student.introduce())
print(student.study("Computer Science"))

print(teacher.introduce())
print(teacher.teach("Algebra"))