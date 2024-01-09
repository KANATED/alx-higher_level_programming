#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all occurrences of characters 'c' and 'C' from a string.

    Parameters:
    - my_string (str): The input string.

    Returns:
    - The new string without 'c' and 'C' characters.
    """

    # Using list comprehension to filter out 'c' and 'C' characters
    filtered_string = ''.join(char for char in my_string if char.lower() not in {'c', 'C'})

    return filtered_string
