#!/usr/bin/python3
""" Returns a new dictionary with all values multiplied by 2. """


def multiply_by_2(a_dictionary):
    tmp_dictionary = a_dictionary.copy()
    for i in tmp_dictionary.keys():
        tmp_dictionary[i] *= 2
    return (tmp_dictionary)
