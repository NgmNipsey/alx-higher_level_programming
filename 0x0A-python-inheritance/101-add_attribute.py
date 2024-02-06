#!/usr/bin/python3
""" Defines attributes function """


def add_attribute(obj, attr_name, attr_value):
    """ Represents attribute function """
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
