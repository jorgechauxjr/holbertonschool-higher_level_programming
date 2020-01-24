#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor, initialize a Square"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of class."""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
