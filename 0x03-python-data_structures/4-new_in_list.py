#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position without modifying the original list.

    Parameters:
    - my_list (list): The input list.
    - idx (int): The index where the element should be replaced.
    - element (int): The new element to be placed at the specified index.

    Returns:
    - A copy of the original list with the specified modification.
    - If idx is negative or out of range, returns a copy of the original list.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
