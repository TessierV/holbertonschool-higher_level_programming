#!/usr/bin/python3
"""Rectangle"""


from models.base import Base
"""inherit from Base"""


class Rectangle(Base):
    """Class: Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        self.__width = width

    @property
    def height(self):
        self.__height = height

    @property
    def x(self):
        self.__x = x

    @property
    def y(self):
        self.__y = y


    def area(self):
            """Returns area of instance"""
            return self.__width * self.__height
