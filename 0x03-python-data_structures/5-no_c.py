#!/usr/bin/python3
""" Remove c and C in a string."""


def no_c(my_string):
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    return (new_string)
