# Create an empty dictionary
my_dict = {}

# Add new elements to the dictionary
my_dict['apple'] = 3
my_dict['banana'] = 5
my_dict['cherry'] = 2
my_dict['date'] = 4

print("Original dictionary:", my_dict)

# Create another dictionary
other_dict = {'apple': 2, 'banana': 3, 'kiwi': 6}

# Calculate the sum of two dictionaries
sum_dict = {key: my_dict.get(key, 0) + other_dict.get(key, 0) for key in set(my_dict) | set(other_dict)}
print("Sum of dictionaries:", sum_dict)

# Create a dictionary with keys from 10 to 20 and values 5 times the keys
new_dict = {key: key * 5 for key in range(10, 21)}
print("Dictionary with keys from 10 to 20:", new_dict)

# Calculate the sum of all values in a dictionary
total_sum = sum(my_dict.values())
print("Sum of all values in the dictionary:", total_sum)

# Calculate the product of all values in a dictionary
total_product = 1
for value in my_dict.values():
    total_product *= value
print("Product of all values in the dictionary:", total_product)

# Sort the dictionary by keys
sorted_dict = {key: my_dict[key] for key in sorted(my_dict)}
print("Sorted dictionary by keys:", sorted_dict)

# Find the maximum and minimum values in a dictionary
max_value = max(my_dict.values())
min_value = min(my_dict.values())
print("Maximum value:", max_value)
print("Minimum value:", min_value)

# Remove elements from the dictionary
del my_dict['cherry']
print("Dictionary after removing 'cherry':", my_dict)
