#!/usr/bin/python3

def max_integer(my_list=[]) -> int:
    return my_list.sort()[-1] if my_list else None


if __name__ == "__main__":
    max_integer()
