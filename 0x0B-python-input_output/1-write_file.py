#!/usr/bin/python3
"""Write string module."""


from codecs import utf_16_be_decode


def write_file(filename="", text=""):
    """Writes a string to a test file."""

    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
