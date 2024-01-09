#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list.

    Parameters:
    - my_list (list): The input list.
    - idx (int): The index of the element to retrieve.

    Returns:
    - The element at the specified index.
    - None if idx is negative or out of range.
    """

    if idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
