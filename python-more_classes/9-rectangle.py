#!/usr/bin/python3
'''Rectangle'''


class Rectangle:
    '''class: Rectangle.'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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
                rec += str(str(self.print_symbol)*self.__width) + '\n'
                if i is not (self.__height):
                    rec += ""
            rec = rec[:-1]
            return rec

    def __repr__(self):
        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if type(rect_1) == type(rect_2):
            return rect_1
    
    @classmetod
    def square(cls, size=0):
        return Rectangle.width == Rectangle.height == Rectangle.size