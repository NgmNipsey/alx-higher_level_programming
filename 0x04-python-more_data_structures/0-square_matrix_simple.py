#!/usr/bin/python3
"""Computes the square values of integers."""


def square_matrix_simple(matrix=[]):
    tmp = []
    for i in matrix:
        tmp.append(list(map(lambda i: i**2, i)))
    return (tmp)
