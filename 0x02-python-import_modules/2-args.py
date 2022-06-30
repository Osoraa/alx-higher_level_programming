#!/usr/bin/python3
from sys import argv


def main():
    argLen = len(argv) - 1
    if not argLen:
        print("0 arguments.")
        return

    print("{:d} argument{:s}".format(argLen, "s" if argLen > 1 else ""))

    for index in range(1, argLen + 1):
        print(f"{index:d}: {argv[index]:s}")


if __name__ == "__main__":
    main()
