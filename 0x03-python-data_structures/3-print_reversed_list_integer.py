#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for item in my_list[::-1]:
            print("{:d}".format(item))


if __name__ == "__main__":
    print_reversed_list_integer()
