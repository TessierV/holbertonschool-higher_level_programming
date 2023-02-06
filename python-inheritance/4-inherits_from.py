#!/usr/bin/python3
""" Function """


def inherits_from(obj, a_class):
    """
     function that returns True if the object
     is an instance of a class that inherited
     (directly or indirectly) from the specified
     class ; otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
