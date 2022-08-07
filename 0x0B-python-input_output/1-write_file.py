#!/usr/bin/python3
"""Write file module."""


def write_file(filename="", text=""):
    """Writes a string to a test file.

    Args:
        filename: File to write text.
        text: Text to append.

    Returns:
        Number of characters written to <filename>"""

    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))


if __name__ == "__main__":
    write_file()
