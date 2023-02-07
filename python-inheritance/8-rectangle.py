#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Creating a class: Rectangle"""


class Rectangle(BaseGeometry):
    """def __init__"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", width)
        self.__height = height

Rectangle = __import__('8-rectangle').Rectangle
