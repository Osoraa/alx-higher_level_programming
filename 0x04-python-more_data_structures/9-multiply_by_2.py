#!/usr/bin/python3


def multiply_by_2(a_dict=None):
    return {key: a_dict[key] * 2 for key in a_dict.keys()} if a_dict else None


if __name__ == "__main__":
    multiply_by_2()
