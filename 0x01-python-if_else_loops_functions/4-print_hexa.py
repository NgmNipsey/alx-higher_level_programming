#!/usr/bin/python3
"""Print given range of numbers in hexadecimal format"""

for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
