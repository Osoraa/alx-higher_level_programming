#!/usr/bin/python3


def element_at(my_list, idx):
    if 0 > idx or idx >= len(my_list):
        return None

    return my_list[idx]


if __name__ == "__main__":
    element_at()
