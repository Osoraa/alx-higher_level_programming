#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    return [(i + 1) % 2 for i in my_list] if my_list else None


if __name__ == "__main__":
    print(divisible_by_2())
