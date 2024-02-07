#!/usr/bin/python3
""" defines a json function """
import json


def save_to_json_file(my_obj, filename):
    """
    Returns an object to a text file using json
    representation
    """
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
