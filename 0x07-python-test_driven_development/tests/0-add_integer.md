# Doctest document for the add_integer module

## Import the add_integer function from the module

    >>> add_integer = __import__("0-add_integer").add_integer

Normal input with 2 positive numbers:

    >>> print(add_integer(1, 2))
    3

Normal input with positive and negative values:

    >>> print(add_integer(100, -2))
    98

Normal singular value input:

    >>> print(add_integer(2))
    100

Normal Floating point addition:

    >>> print(add_integer(100.3, -2))
    98

Error, passing None as input:

    >>> print(add_integer(None))
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> print(add_integer(2, None))
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

Error, passing an integer as a string as input:

    >>> print(add_integer(2, "3"))
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

Error, passing empty arguments:

    >>> print(add_integer())
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
