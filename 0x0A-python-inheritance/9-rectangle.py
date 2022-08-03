#!/usr/bin/python3
"""Rectange module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class.

    Args:
        width: Rectangle width.
        height: Rectangle height.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__height = height
        self.__width = width

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"

    def area(self):
        """Calculates rectangle area."""

        return self.__height * self.__width
