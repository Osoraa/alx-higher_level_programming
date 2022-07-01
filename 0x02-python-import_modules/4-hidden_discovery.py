#!/usr/bin/python3
import hidden_4


def main():
    names = [name for name in dir(hidden_4) if name[:2] != "__"]
    for name in names:
        print(name)


if __name__ == "__main__":
    main()
