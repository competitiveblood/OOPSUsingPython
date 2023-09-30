class Student:
    def __init__(self, name, regist_number,subject):
        self.name = name
        self.regist = regist_number
        self.subject= subject

    def introduce(self):
        print(f"Hello, my name is {self.name} and my registration number is {self.regist_number} and my favourite subject is {self.subject}.")


person1 = Student("ABC", "20009302", "Engineering Economics")

person1.introduce()
