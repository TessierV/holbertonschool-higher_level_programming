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
