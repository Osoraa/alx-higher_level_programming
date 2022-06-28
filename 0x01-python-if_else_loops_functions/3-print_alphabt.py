#!/usr/bin/python3
for i in "abcdefghijklmnopqrstuvwxyz":
    print("{:s}".format(i if i not in "qe" else ""), end="")
