#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples.

    Parameters:
    - tuple_a (tuple): The first input tuple.
    - tuple_b (tuple): The second input tuple.

    Returns:
    - A tuple with the sum of corresponding elements from tuple_a and tuple_b.
    """

    # Use value 0 for each missing integer in smaller tuples
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Return a tuple with the sum of corresponding elements
    return (a[0] + b[0], a[1] + b[1])
