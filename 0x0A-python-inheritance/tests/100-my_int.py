#!/usr/bin/python3
""" defines module: MyInt(int) """


class MyInt(int):
    """ Represent MyInt class """
    def __eq__(self, other):
        """ Invert == to != """
        return super().__ne__(other)
    def __ne__(self, other):
        """ Invert != to == """
        return super().__eq__(other)
