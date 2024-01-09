#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list in reverse order.

    Parameters:
    - my_list (list): The input list containing integers.

    Returns:
    - None
    """

    reversed_list = my_list[::-1]

    for item in reversed_list:
        print("{:d}".format(item))
