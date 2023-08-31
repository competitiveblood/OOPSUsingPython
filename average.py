num1 = float(input("Enter value of first number: "))
num2 = float(input("Enter value of second number: "))
num3 = float(input("Enter value of third number: "))
y = (num1+num2+num3)/3
dev1=num1-y
dev2=num2-y
print("The average of the three numbers is",str(y))
print("The deviation of the first number from the average is",str(dev1))
print("The deviation of the second number from the average is",str(dev2))