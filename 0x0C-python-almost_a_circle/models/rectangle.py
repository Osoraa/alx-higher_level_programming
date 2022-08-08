#!/usr/bin/python3
"""Rectangle module."""

from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class that inherits from the Base class.

    Args:
        width: Rectangle width.
        height: Rectangle height.
        x: x value
        y: y value
        id: Public instance id"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Setter/getter for width
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    # Setter/getter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # Setter/getter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    # Setter/getter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
