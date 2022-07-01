#!/usr/bin/python3
from sys import exit, argv
from calculator_1 import add, sub, div, mul


def main():
    if len(argv) != 4:
        # print(f"Usage: {argv[0]:s} <a> <operator> <b>")
        for arg in argv:
            print(arg)
        exit(1)

    a, op, b = int(argv[1]), argv[2], int(argv[3])
    op_dict = {
        "+": add(a, b),
        "-": sub(a, b),
        "*": mul(a, b),
        "/": div(a, b),
    }

    if op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, op, b, op_dict[op]))


if __name__ == "__main__":
    main()
