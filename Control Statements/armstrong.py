def is_armstrong_number(n):
  """Returns True if n is an Armstrong number, False otherwise."""

  sum = 0
  number = n
  while number > 0:
    digit = number % 10
    sum += digit ** len(str(n))
    number //= 10

  return sum == n