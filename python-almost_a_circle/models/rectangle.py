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
        """function that rectangle #"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for l in range(self.__width):
                print('#', end='' if l != self.__width - 1 else '\n')

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        print_wh = "[Rectangle] ({}) {}/{} - {}/{}"
        return (print_wh.format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute"""
        if len(args) is not 0:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                if num == 1:
                    self.width = arg
                if num == 2:
                    self.height = arg
                if num == 3:
                    self.x = arg
                if num == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
