#!/usr/bin/python3
# The above line specifies the interpreter to be used when executing the script

import sys  # Import the sys module to access command-line arguments

# Retrieve the number of arguments using len(sys.argv)
num_args = len(sys.argv) - 1  # Subtracting 1 to exclude the script name

# Print the number of arguments
print("{:d} argument{}{}".format(num_args, 's' if num_args != 1 else '', ':' if num_args > 0 else '.'))

# Print each argument along with its position (starting at 1)
for i, arg in enumerate(sys.argv[1:], start=1):
    print("{:d}: {}".format(i, arg))
