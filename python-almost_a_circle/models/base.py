#!/usr/bin/python3
""" import json """
import json


class Base:
    """
    first class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ json return the dictionaries"""
        string = []
        if list_dictionaries is None:
            return string
        else:
            return json.dumps(list_dictionaries)
