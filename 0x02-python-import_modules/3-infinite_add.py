#!/usr/bin/python3
from sys import argv


def main():
    print(sum([int(arg) for arg in argv[1:]]))


if __name__ == "__main__":
    main()
