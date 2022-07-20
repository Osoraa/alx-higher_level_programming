#!/usr/bin/python3

"""Defines a Square class."""


class Square():
    """Defines a Square class."""

    def __init__(self, name) -> None:
        self.name = name

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, name):
        self.__name = name
