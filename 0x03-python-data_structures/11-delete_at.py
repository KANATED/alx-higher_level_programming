#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list.

    Parameters:
    - my_list (list): The input list.
    - idx (int): The index where the item should be deleted.

    Returns:
    - The modified list after deleting the item.
      If idx is negative or out of range, returns the same list.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list
