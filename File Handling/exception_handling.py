a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
try:
    c=a/b
    print(c)
except:
    print("Exception Raised")
else:
    print("No Exception Raised")
finally:
    print("Program ends")

# try: The try block contains code that you think might generate an error.

# except: The except block contains code that handles the error. You can have multiple except blocks to handle different types of errors.
# The except block contains code that will be executed if an error occurs in the try block. You can specify the type of error that you want to handle by using the except keyword followed by the type of error. For example, except ZeroDivisionError will handle the ZeroDivisionError exception.

# else: The else block is executed if there are no errors in the try block.

# finally: The finally block is always executed, regardless of whether or not there are errors in the try block.

