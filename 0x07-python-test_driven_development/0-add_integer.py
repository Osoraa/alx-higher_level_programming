#!/usr/bin/python3
"""The add_integer module

"""


def add_integer(a=None, b=98) -> int:
    """Adds two integers and returns result.

    Args:
        a: First parameter.
        b: Second parameter.

    Returns:
        The result of addition of a and b.

    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    try:
        a, b = int(a), int(b)
    except Exception as e:
        raise e

    return a + b


if __name__ == "__main__":
    add_integer()
