def is_prime_number(a):
    if a <= 1:
        return False
    elif a <= 3:
        return True
    elif a % 2 == 0:
        return False
    else:
        for i in range(3, int(a ** 0.5) + 1, 2):
            if a % i == 0:
                return False
        return True


num = int(input("Enter a number: "))
if is_prime_number(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
