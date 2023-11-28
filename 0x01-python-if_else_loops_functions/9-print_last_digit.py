#!/usr/bin/python3
"""Function to print last digit of any given number."""


def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
