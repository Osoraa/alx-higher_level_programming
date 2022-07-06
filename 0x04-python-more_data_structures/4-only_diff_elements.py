#!/usr/bin/python3


def only_diff_elements(set_1=None, set_2=None) -> set:
    return set_1.symmetric_difference(set_2) if set_1 or set_2 else None


if __name__ == "__main__":
    only_diff_elements()
