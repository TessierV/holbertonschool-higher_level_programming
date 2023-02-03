#!/usr/bin/python3
""" print square"""

def print_square(size):
    """square with the character #"""
    if isinstance(size, int) is False:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) is True and size < 0: 
        raise TypeError('size must be an integer')
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print('')
