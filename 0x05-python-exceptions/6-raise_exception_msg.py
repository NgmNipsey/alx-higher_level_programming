#!/usr/bin/python3
""" A function that raises a name exception with a message."""


def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError:
        print(message)
