#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    return f"{str[:n]:s}{str[n + 1:]:s}"
