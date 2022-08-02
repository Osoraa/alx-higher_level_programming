#!/usr/bin/python3
"""MyList module"""


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
