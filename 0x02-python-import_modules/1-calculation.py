#!/usr/bin/python3
# The above line specifies the interpreter to be used when executing the script

# Importing specific functions (add, sub, mul, div) from the calculator_1 module
from calculator_1 import add, sub, mul, div

# Assigning the value 10 to the variable 'a'
a = 10

# Assigning the value 5 to the variable 'b'
b = 5

# Calling the 'add' function from calculator_1 and storing the result in 'res_add'
res_add = add(a, b)

# Calling the 'sub' function from calculator_1 and storing the result in 'res_sub'
res_sub = sub(a, b)

# Calling the 'mul' function from calculator_1 and storing the result in 'res_mul'
res_mul = mul(a, b)

# Calling the 'div' function from calculator_1 and storing the result in 'res_div'
res_div = div(a, b)

# Printing the result of addition using string formatting
print("{:d} + {:d} = {:d}".format(a, b, res_add))

# Printing the result of subtraction using string formatting
print("{:d} - {:d} = {:d}".format(a, b, res_sub))

# Printing the result of multiplication using string formatting
print("{:d} * {:d} = {:d}".format(a, b, res_mul))

# Printing the result of division using string formatting
print("{:d} / {:d} = {:d}".format(a, b, res_div))
