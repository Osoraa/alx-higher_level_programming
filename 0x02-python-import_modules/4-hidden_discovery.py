#!/usr/bin/python3
__import__("0-add")


def main():
    names = [name for name in dir("0-add")]
    for name in names:
        print(name)


if __name__ == "__main__":
    main()
