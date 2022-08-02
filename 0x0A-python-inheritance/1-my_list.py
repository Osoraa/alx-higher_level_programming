#!/usr/bin/python3
"""MyList module.

Simple Usage:
    >>> MyList = __import__('1-my_list').MyList

"""


class MyList(list):
    """Extends list functionality by sorting list.

    Args:
        None.
    """

    def __init__(self):
        pass

    def print_sorted(self):
        """Prints a sorted list.

        Args:
            None.

        Return:
            None.
        """

        print(sorted(self))
