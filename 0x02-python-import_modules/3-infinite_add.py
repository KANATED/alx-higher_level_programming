#!/usr/bin/python3
# The above line specifies the interpreter to be used when executing the script

import sys  # Import the sys module to access command-line arguments

# Convert each argument to an integer and sum them up
result = sum(int(arg) for arg in sys.argv[1:])

# Print the result
print(result)
