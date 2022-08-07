#!/usr/bin/python3
"""Read file module."""


def read_file(filename=""):
    """Prints a textfile to stdout"""

    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")


if __name__ == "__main__":
    read_file()
