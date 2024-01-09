#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Parameters:
    - matrix (list of lists): The input matrix containing integers.

    Returns:
    - None
    """

    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()
