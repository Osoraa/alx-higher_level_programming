#!/usr/bin/python3

def no_c(my_string):
    my_string = list(my_string)

    my_string = [char for char in my_string if char.lower() != "c"]
    return "".join(my_string)


if __name__ == "__main__":
    no_c()
