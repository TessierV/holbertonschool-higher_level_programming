#!/usr/bin/python3
"""Square"""


from models.rectangle import Rectangle
"""inherit from Base"""


class Square(Rectangle):
    """Class: Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        print_square = "[Square] ({}) {}/{} - {}"
        return (print_square.format
                (self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """ Size square """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute"""
        if len(args) is not 0:
            for num, arg in enumerate(args):
                if num == 0:
                    self.id = arg
                if num == 1:
                    self.size = arg
                if num == 2:
                    self.x = arg
                if num == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
