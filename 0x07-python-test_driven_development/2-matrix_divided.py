#!/usr/bin/python3
"""The matrix division module.

Simple Usage:

    >>> func = __import__('2-matrix_divided').matrix_divided

    >>> func([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

"""


def matrix_divided(matrix, div):
    """Divides the elements of a matrix.

    Args:
        matrix: List of ints and Floats.
        div: Int or float used to divide members of the matrix.

    Returns:
        Returns a new matrix of the results of the operation.
    """

    matrix_type_err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(matrix_type_err)

    row_len = len(matrix[0])

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_type_err)

        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

        for col in row:
            if type(col) not in (int, float):
                raise TypeError(matrix_type_err)

    return [[round(col / div, 2) for col in row] for row in matrix]
