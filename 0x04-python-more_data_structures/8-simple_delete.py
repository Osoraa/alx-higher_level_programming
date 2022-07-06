#!/usr/bin/python3


def simple_delete(a_dict=None, key="") -> dict:
    a_dict.pop(key, None)  # if key in a_dict.keys() else None
    return a_dict


if __name__ == "__main__":
    simple_delete()
