#!/usr/bin/python3
"""The name saying module.

Simple Usage:

    >>> func = __import__('3-say_my_name').say_my_name

    >>> func("Osoraa", "Nwankwo")
    My name is Osoraa Nwankwo

"""


def say_my_name(fname="", lname=""):
    """Prints firstname and lastname of a user in a sentence.

    Args:
        fname: User's first name.
        lname: User's last name.

    Returns:
        None.
    """

    if not isinstance(fname, str):
        raise TypeError("first_name must be a string")

    if not isinstance(lname, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {fname} {lname}")
