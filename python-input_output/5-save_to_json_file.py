#!/usr/bin/python3
""" This json import """

import json
""" Function """


def save_to_json_file(my_obj, filename):
    """
    Write a function that writes an Object
    to a text file, using a JSON representation:
    """
    with open(filename, 'aw', encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
