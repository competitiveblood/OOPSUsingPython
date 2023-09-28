class Baseclass1: #base class
    def Summation(self,a,b):
        return a+b;

class Baseclass2: #base class
    def Multiplication(self,a,b):
        return a*b;

class Derivedclass(Baseclass1,Baseclass2): #derived class
    def Divide(self,a,b):
        return a/b;

d=Derivedclass() #object of derived class

print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))
