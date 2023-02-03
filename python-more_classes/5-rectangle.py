#!/usr/bin/python3
'''Rectangle'''


class Rectangle:
    '''class: Rectangle.'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        return self.__width*self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__width + self.__height)

    def __str__(self):
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        else:
            for i in range(self.__height):
                rec += str('#'*self.__width) + '\n'
                if i is not (self.__height):
                    rec += ""
            rec = rec[:-1]
            return rec

    def __repr__(self):
        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        print('Bye rectangle...')
