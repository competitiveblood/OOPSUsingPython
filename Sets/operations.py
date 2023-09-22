# Initialize two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Pop an element from the set (random element)
popped_element = set1.pop()
print("Popped element from set1:", popped_element)

# Remove an element from the set
set1.remove(2)
print("After removing 2 from set1:", set1)

# Clear all elements from a set
set2.clear()
print("Cleared set2:", set2)

# Union of two sets
union_set = set1.union(set2)  # or simply, union_set = set1 | set2
print("Union of set1 and set2:", union_set)

# Intersection of two sets
intersection_set = set1.intersection(set2)  # or simply, intersection_set = set1 & set2
print("Intersection of set1 and set2:", intersection_set)

# Difference between two sets (elements in set1 but not in set2)
difference_set = set1.difference(set2)  # or simply, difference_set = set1 - set2
print("Difference between set1 and set2:", difference_set)

# Symmetric difference between two sets (elements in either set but not in both)
symmetric_difference_set = set1.symmetric_difference(set2)  # or simply, symmetric_difference_set = set1 ^ set2
print("Symmetric difference between set1 and set2:", symmetric_difference_set)
