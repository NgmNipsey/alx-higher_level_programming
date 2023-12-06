#!/usr/bin/python3
"""Replace all the elements in the list."""


def search_replace(my_list, search, replace):
    return (list(map(lambda i: replace if i is search else i, my_list)))
