#!/usr/bin/python3
""" This json import """

import json
""" Function """


def from_json_string(my_str):
    """
    Write a function that returns an object
    (Python data structure) represented
    by a JSON string:
    """
    return json.loads(my_str)