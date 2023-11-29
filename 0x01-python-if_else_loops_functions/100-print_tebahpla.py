#!/usr/bin/python3
"""Print ASCII alphabet in reverse alternatively."""

i = 0
for letter in range(ord('z'), ord('a') - 1, - 1):
    print("{}".format(chr(letter - i)), end="")
    i = 32 if i == 0 else 0
