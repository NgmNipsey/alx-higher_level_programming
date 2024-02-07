#!/usr/bin/python3
""" defines a fucntion """


def read_file(filename=""):
    """ read a text file (UTF8) and print to stdout """
    with open(filename, "r", encoding="utf-8") as fl:
        print(fl.read(), end="")
