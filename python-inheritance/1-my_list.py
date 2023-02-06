#!/usr/bin/python3
"""" Function """

class MyList(list):
    """
    Returns the list of available attributes and methods of an object
    """
    def print_sorted(self):
        print(sorted(self))
