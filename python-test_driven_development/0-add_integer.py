#!/usr/bin/python3
"""
    function to add two int
"""

def add_integer(a, b=98):
    '''function who add two integer'''
    try:
        return int(a) + int(b)
    except:
        if type(a) is not int and type(a) is not float:
            raise TypeError('a must be an integer')
        if type(b) is not int and type(b) is not float:
            raise TypeError('b must be an integer')
