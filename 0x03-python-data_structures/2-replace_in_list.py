#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position.

    Parameters:
    - my_list (list): The input list.
    - idx (int): The index where the element should be replaced.
    - element (int): The new element to be placed at the specified index.

    Returns:
    - The modified list.
    - If idx is negative or out of range, returns the original list.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
