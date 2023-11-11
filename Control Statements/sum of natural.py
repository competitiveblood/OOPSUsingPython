def sum_of_numbers(n):
    """Return the sum of the first n natural numbers."""
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

# Example usage:
number = 10
result = sum_of_numbers(number)
print(f"The sum of the first {number} natural numbers is: {result}")
