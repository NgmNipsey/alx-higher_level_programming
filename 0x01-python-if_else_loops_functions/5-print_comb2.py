#!/usr/bin/python3
"""Print numbers from 0 to 99."""

for numbers in range(0, 100):
    if numbers == 99:
        print("{}".format(numbers))
    else:
        print("{:02}".format(numbers), end=", ")
