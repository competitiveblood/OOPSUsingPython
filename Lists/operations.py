# Initialize a list
my_list = [1, 2, 3, 4, 5]

# Append an element to the end of the list
my_list.append(6)
print("After appending 6:", my_list)

# Insert an element at a specific position
my_list.insert(2, 7)
print("After inserting 7 at position 2:", my_list)

# Extend the list with another list
extension = [8, 9, 10]
my_list.extend(extension)
print("After extending with [8, 9, 10]:", my_list)

# Remove the first occurrence of a value
my_list.remove(3)
print("After removing the first occurrence of 3:", my_list)

# Pop an element by index (default is the last element)
popped_element = my_list.pop(4)
print("Popped element at index 4:", popped_element, "Updated list:", my_list)

# Slice the list to get a subset
subset = my_list[1:4]
print("Sliced list [1:4]:", subset)

# Find the minimum and maximum values in the list
min_value = min(my_list)
max_value = max(my_list)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

# Reverse the list
my_list.reverse()
print("Reversed list:", my_list)

# Concatenate two lists
another_list = [11, 12, 13]
concatenated_list = my_list + another_list
print("Concatenated list:", concatenated_list)

# Count the occurrences of an element in the list
count_2 = my_list.count(2)
print("Count of 2 in the list:", count_2)

# Multiply each element by a scalar
multiplied_list = [x * 2 for x in my_list]
print("List after multiplying each element by 2:", multiplied_list)

# Sort the list in ascending order
my_list.sort()
print("Sorted list in ascending order:", my_list)

# Find the index of the first occurrence of a value
index_6 = my_list.index(6)
print("Index of the first occurrence of 6:", index_6)

# Clear the list (remove all elements)
my_list.clear()
print("Cleared list:", my_list)
