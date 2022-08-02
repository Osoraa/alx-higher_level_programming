#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """Extends list functionality by sorting list.

    Args:
        list: List object sort and return for print.

    Return:
        Sorted list.
    """

    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))
