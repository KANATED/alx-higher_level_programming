#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Parameters:
    - sentence (str): The input string.

    Returns:
    - A tuple with the length of the string and its first character.
    """

    if not sentence:  # Check if the sentence is empty
        return (0, None)

    # Return a tuple with the length and the first character
    return (len(sentence), sentence[0])
