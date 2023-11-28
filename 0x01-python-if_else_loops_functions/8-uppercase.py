#!/usr/bin/python3
"""Print string in uppercase."""


def uppercase(str):
    for a in str:
        if ord(a) >= 97 and ord(a) <= 122:
            a = chr(ord(a) - 32)
        print("{}".format(a), end="")
    print("")
