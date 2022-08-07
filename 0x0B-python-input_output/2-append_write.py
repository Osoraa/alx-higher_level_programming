#!/usr/bin/python3
"""Append write module."""


def append_write(filename="", text=""):
    """Appends a string at the end of a textfile.

    Args:
        filename: File to append text.
        text: Text to append.

    Returns:
        Number of characters written to <filename>.
    """

    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))


if __name__ == "__main__":
    append_write()
