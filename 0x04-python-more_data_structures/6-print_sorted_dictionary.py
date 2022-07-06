#!/usr/bin/python3


def print_sorted_dictionary(a_dict) -> None:
    # for key in sorted(a_dict.keys()):
    #     print(f"{key}: {a_dict[key]}")
    for key, value in sorted(a_dict.items()):
        print(f"{key}: {value}")


if __name__ == "__main__":
    print_sorted_dictionary()
