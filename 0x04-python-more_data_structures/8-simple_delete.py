#!/usr/bin/python3
"""a function that deletes a key in a dictionary."""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
