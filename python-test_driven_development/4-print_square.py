#!/usr/bin/python3
""" print square"""

def print_square(size):
    """square with the character #"""
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, int) is True and size >= 0:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print('')
    else: 
        raise TypeError('size must be an integer')