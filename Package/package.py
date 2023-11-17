DIRECTORY FILE 

my_package/
    __init__.py
    math_operations/
        __init__.py
        addition.py
        subtraction.py

#my_package/__init__.py
# This file can be empty. It marks the `my_package` directory as a Python package.

#my_package/math_operations/__init__.py
# This file can be empty. It marks the `math_operations` directory as a Python package.

#my_package/math_operations/addition.py
def add(a, b):
    return a + b


#my_package/math_operations/subtraction.py
def subtract(a, b):
    return a - b

#Python code to use the package:
from my_package.math_operations import addition, subtraction

result_add = addition.add(5, 3)
result_subtract = subtraction.subtract(10, 4)

print("Addition:", result_add)
print("Subtraction:", result_subtract)


#This structure and code showcase a Python package my_package containing a sub-package math_operations with modules for addition and subtraction operations. The final Python code demonstrates how to import and utilize functions from these modules within the package for arithmetic operations.


my_package/: This directory serves as the main package directory.
__init__.py: An empty file used to mark the my_package directory as a Python package.
math_operations/: A sub-package within my_package.
__init__.py: An empty file used to mark the math_operations directory as a Python package.
addition.py: Contains code for addition operation.
subtraction.py: Contains code for subtraction operation.


