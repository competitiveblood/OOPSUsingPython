def sum_even_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total

start_range = 10
end_range = 35

result = sum_even_numbers(start_range, end_range)
print(f"The sum of even numbers between {start_range} and {end_range} is {result}.")
