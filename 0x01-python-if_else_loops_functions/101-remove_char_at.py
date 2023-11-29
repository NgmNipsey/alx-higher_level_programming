#!/usr/bin/python3
"""Function that creat a coy of string, remove character at position n."""


def remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
