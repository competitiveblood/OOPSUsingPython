class Animal:
    def speak(self):
        print("animal speaking")

#The child class Dog inherits from the superclass Animal

class Dog(Animal):
    def bark(self):
        print("dog barking")

#The child class dogchild inherits aother child class Dog

class dogchild(Dog):
    def eat(self):
        print("dogchild eating bread...")

d = dogchild()
d.bark()
d.speak()
d.eat()