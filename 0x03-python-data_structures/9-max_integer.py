#!/usr/bin/python3
"""Function that find biggest integer."""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        maxim = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > maxim:
                maxim = my_list[i]
    return (maxim)

