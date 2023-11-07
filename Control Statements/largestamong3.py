def find_greatest_number(num1,num2,num3):

    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3
    
greatest_number = find_greatest_number(10,20,30)

print(greatest_number)