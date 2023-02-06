#!/usr/bin/python3
"""" Function """


def is_same_class(obj, a_class):
    """
    Returns the list of available attributes and methods of an object
    """
    return type(obj) == a_class
