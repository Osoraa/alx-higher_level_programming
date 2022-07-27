#!/usr/bin/python3
"""The print square module

Simple Usage:

    >>> func = __import__("4-print_square").print_square

    >>> func(2)
    ##
    ##

"""


def print_square(size=0):
    """Prints a square to stdout.

    Args:
        size (int): Length of square sides.

    Returns:
        None.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
