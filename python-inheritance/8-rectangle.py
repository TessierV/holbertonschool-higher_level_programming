#!/usr/bin/python3
"""Creating an empty class: BaseGeometry"""


class BaseGeometry:
    """
    Creating an empty class: BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""Creating a class: Rectangle"""


class Rectangle(BaseGeometry):
    """def __init__"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", width)
        self.__height = height
