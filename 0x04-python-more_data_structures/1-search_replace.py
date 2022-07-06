#!/usr/bin/python3


def search_replace(my_list=[], old=None, new=None) -> list[int]:
    new_list = my_list[:]

    for index, value in enumerate(new_list):
        new_list[index] = new if value is old else value

    return new_list


if __name__ == "__main__":
    search_replace()
