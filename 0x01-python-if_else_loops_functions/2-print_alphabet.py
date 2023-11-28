#!/usr/bin/python3
"""Print ASCII alphabet in lowercase, not followed by newline"""

for i in range(97, 123):
    print("{}".format(chr(i)), end="")
