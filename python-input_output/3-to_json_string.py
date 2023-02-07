#!/usr/bin/python3
""" This json import """

import json
""" Function """


def to_json_string(my_obj):
    """
    Write a function that reads a text file (UTF8) and prints it to stdout:
    """
    return json.dumps(my_obj)
