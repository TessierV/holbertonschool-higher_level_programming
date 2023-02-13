#!/usr/bin/python3
"""Rectangle"""


from models.base import Base
"""inherit from Base"""


class Rectangle(Base):
    """Class: Rectangle"""
    print_symbol = '#'


    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """function that define area of the rectangle"""

        return self.__height * self.__width

    def display(self):
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        else:
            for i in range(self.__height):
                rec += str(str(self.print_symbol)*self.__width) + '\n'
                if i is not (self.__height):
                    rec += ""
            rec = rec[:-1]
            return rec
