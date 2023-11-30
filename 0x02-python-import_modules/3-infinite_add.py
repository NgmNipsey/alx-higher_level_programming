#!/usr/bin/python3
"""Program to add all arguments."""


def add_av(argv):
    count = len(argv) - 1
    if count == 0:
        print("{}".format(count))
        return
    else:
        i = 1
        add = 0
        while i <= count:
            add += int(argv[i])
            i += 1
        print("{}".format(add))


if __name__ == "__main__":
    import sys

    add_av(sys.argv)
