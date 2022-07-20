#!/usr/bin/python3

"""Defines a Square class."""


class Square:
    """Defines a Square class."""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (
            not isinstance(position, tuple)
            or not len(position) == 2
            or not all(isinstance(i, int) for i in position)
            or min(position) < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        self.__init__(value, self.__position)

    @position.setter
    def position(self, value):
        self.__init__(self.__size, value)

    def area(self):
        """Calculates the area of a square"""

        return self.__size**2

    def my_print(self):
        """Prints a square to stdout"""

        if not self.__size:
            print()
            return

        # Print (lines * position[1])
        for _ in range(self.__position[1]):
            print()

        # Print square with each line preceeded by (space * position[0])
        for _ in range(self.__size):
            print(f"{' ' * self.__position[0]}{'#' * self.__size}")
