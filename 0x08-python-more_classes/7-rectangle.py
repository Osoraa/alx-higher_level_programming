#!/usr/bin/python3
"""The Rectangle module

Makes available a Rectangle class for rectangle representation
"""


class Rectangle:
    """Creates an instance of a Rectangle.

    Args:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle

    Attributes:
        number_of_instances (int): Instance count.
        print_symbol: Symbol used to represent
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height
        self.__class__.set_num(True)

    @classmethod
    def set_num(cls, arg):
        """Sets the number of rectangle instances.
        Called in both initialisation and garbage collection.

        Args:
            arg (bool): True to increment, False to decrement.

        Returns:
            None.
        """

        if arg:
            cls.number_of_instances += 1
        else:
            cls.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def __str__(self) -> str:
        if not (self.__height and self.__width):
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.__width
                for _ in range(self.__height)]
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.set_num(False)

    def area(self) -> int:
        """Computes the area of a rectangle.

        Args:
            None

        Returns:
            Area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self) -> int:
        """Returns the perimeter of a rectangle.

        Args:
            None

         Returns:
            Perimeter of the rectangle
        """

        if self.__width and self.__height:
            return self.__width * 2 + self.__height * 2
        return 0

    # @classmethod
    # def set_print_sym(cls, arg="#"):
    #     """Sets the symbol used to print the rectangle.

    #     Args:
    #         arg (any): Object to use in __str__ method.

    #     Returns:
    #         None.
    #     """

    #     cls.print_symbol = arg







