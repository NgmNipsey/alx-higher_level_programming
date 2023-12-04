#!/usr/bin/python3
"""Return tuples with the length of the string and it's first character."""


def multiple_returns(sentence):
    new_tuple = ()
    if len(sentence) == 0:
        new_tuple = 0, "None"
    else:
        new_tuple = len(sentence), sentence[0]
    return (new_tuple)
