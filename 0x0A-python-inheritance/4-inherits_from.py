#!/usr/bin/python3
""" module: 4-inherits_from """


def inherits_from(obj, a_class):
    """  Represent inherits_from """
    return type(obj) != a_class and isinstance(obj, a_class)
