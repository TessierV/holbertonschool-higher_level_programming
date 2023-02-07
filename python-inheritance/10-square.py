#!/usr/bin/python3
"""Creating a class: Sqaure"""


Rectangle = __import__('9-base_geometry').Rectangle


class Square(Rectangle):
    """def __init__"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return (self.__size*self.__size)
