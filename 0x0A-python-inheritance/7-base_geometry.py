#!/usr/bin/python3
"""Base geometry module."""


class BaseGeometry:
    """Geometry class."""

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value=None):
        """Validates integer input"""

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
