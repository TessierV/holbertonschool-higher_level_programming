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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json return the dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ json save"""
        with open(cls.__name__+'.json', 'w+', encoding="utf-8") as file:
            dict  = []
            if list_objs is not None and len(list_objs) != 0:
                for i in list_objs:
                    dict.append(cls.to_dictionary(i))
                file.write(cls.to_json_string(dict))
            else:
                file.write("[]")
