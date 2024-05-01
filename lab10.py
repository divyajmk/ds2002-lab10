#!/home/gitpod/.pyenv/shims/python3



# 1. Error Handling - Built-in 
def new_throw_me_an_error():
    # Added try and except statements to print out the ZeroDivisionError
    try:
        val1 = 14
        val2 = 0
        return val1 / val2
    except ZeroDivisionError as e:
        print("ZeroDivisionError: Cannot divide by 0")

new_throw_me_an_error

# 2. Error Handling - finally
# The finally clause executes as the last task before the try statement completes. 
# The finally clause runs whether or not the try statement produces an exception.
# In this function, the finally clause serves to ensure that the file is properly closed after the write 
# operation is completed, regardless of whether an exception occured or not which is important as it ensures 
# that the cleanup (of closing the file) is always done.
# This finally clause is important as it ensures the file is closed once it is not needed anymore,
# and this helps prevent the file from being open and allowing other programs to access the file.
# If an exception occurs within the try block when the file is trying to be opened or written to, then 
# the try statement will stop executing, and the program will move to except block to handle the exception. 
# After the except block, the finally block is executed.

# 3. Error Handing - Imported Library 
import json

# Invalid JSON data
# Changes I made: put single quotes outside the {} and closed the key-value in ""
data = '{"invalid_json_key": "value"}'

try:
  # Attempt to load the JSON data
  json.loads(data)
except json.JSONDecodeError as e:
  # Print the JSON import error
  print(f"JSON import error: {e}")