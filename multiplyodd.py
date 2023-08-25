def multiply_odd_numbers(start, end):
    product = 1
    for num in range(start, end + 1):
        if num % 2 != 0:
            product *= num
    return product

start_range = 5
end_range = 15

result = multiply_odd_numbers(start_range, end_range)
print(f"The product of odd numbers between {start_range} and {end_range} is {result}.")
