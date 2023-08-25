def reverse_integer(number):
    reversed_number = 0
    while number != 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number
num = int(input("Enter an integer: "))
reversed_num = reverse_integer(num)
print(f"The reverse of {num} is {reversed_num}.")