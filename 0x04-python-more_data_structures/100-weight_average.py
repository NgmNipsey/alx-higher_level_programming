#!/usr/bin/python3
"""Return average weight."""


def weight_average(my_list=[]):
    if my_list == [] or my_list == None:
        return (0)
    sumt = 0
    tnum = 0
    for x, y in my_list:
        sumt += x * y
        tnum += y
    return (sumt / tnum)
