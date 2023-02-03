#!/usr/bin/python3
""" print square"""

def print_square(size):
    """square with the character #"""
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        if type(size) is float:
            raise TypeError('size must be an integer')
        else:
            raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print('')
