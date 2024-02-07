#!/usr/bin/python3
""" defines a json function """
import json


def load_from_json_file(filename):
    """ Creates an object from a json files """
    with open(filename) as fl:
        json.load(fl)
