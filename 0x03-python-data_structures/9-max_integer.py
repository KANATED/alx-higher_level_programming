#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer in a list.

    Parameters:
    - my_list (list): The input list containing integers.

    Returns:
    - The biggest integer in the list.
    - If the list is empty, returns None.
    """

    if not my_list:  # Check if the list is empty
        return None

    max_value = my_list[0]

    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
