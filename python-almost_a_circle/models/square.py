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


