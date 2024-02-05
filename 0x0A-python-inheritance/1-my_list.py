#!/usr/bin/python3
""" module: my_list """


class MyList(list):
    """ Represent MyList """

    def print_sorted(self):
        """ Sort and print list """
        print(sorted(self))
