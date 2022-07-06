#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary) -> None:
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")


if __name__ == "__main__":
    print_sorted_dictionary()
