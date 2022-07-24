#!/usr/bin/python3
"""P"""


def add_integer(a, b=98):
    """Adds two integers and returns result"""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    try:
        a, b = int(a), int(b)
    except Exception:
        raise Exception

    return a + b
