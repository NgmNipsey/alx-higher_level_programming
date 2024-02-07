#!/usr/python3
""" defines json function """
import json


def from_json_string(my_str):
    """ Returns an object represented by JSON """
    return json.loads(my_str)
