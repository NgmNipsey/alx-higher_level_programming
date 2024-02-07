#!/usr/bin/python3
""" defines a function for JSON """
import json


def to_json_string(my_obj):
    """ Returns a json representantion """
    return json.dumps(my_obj)
