#!/usr/bin/python3
"""Return a key with a biggest value."""


def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        high_score = ''
        for i in my_list:
            if a_dictionary[i] == {}:
                return None
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                high_score = i
        return (high_score)
