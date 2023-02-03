#!/usr/bin/python3
'''add_integer'''


def add_integer(a, b=98):
    '''function who add two integer'''
    try:
        result = a + b
        return int(result)
    except:
        if type(a) is not int and type(a) is not float:
            raise TypeError('a must be an integer')
        else:
            raise TypeError('b must be an integer')
