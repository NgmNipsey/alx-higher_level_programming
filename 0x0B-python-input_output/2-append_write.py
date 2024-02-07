#!/usr/bin/python3
""" defines a function that append a string """


def append_write(filename="", text=""):
    """ append string to text file """
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
