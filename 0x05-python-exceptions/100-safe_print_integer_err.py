#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as ve:
        print("Exception: {}".format(ve), file=stderr)
        return False


if __name__ == "__main__":
    safe_print_integer_err()
