#!/usr/bin/python3
""" A function that raises a type exception."""


def raise_exception():
    try:
        raise TypeError("Exception raised")
    except TypeError:
        print("Exception raised")
