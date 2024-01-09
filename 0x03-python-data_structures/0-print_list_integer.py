#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Prints all integers of a list.

    Parameters:
    - my_list (list): The input list containing integers.

    Returns:
    - None
    """

    for item in my_list:
        print("{:d}".format(item))
