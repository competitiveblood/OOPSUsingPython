def is_leap_year(year):
  """Returns True if year is a leap year, False otherwise."""

  if year % 4 == 0 and year % 100 != 0:
    return True
  elif year % 400 == 0:
    return True
  else:
    return False

# Example usage:

print(is_leap_year(2024))  # True
print(is_leap_year(2023))  # False