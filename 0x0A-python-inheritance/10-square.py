#!/usr/bin/python3

"""
module for Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """Constructor method for square
        Instantiation with size"""

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

"""Because square inherits from Rectangle and Rectangle from BaseGeometry
the method area is implemented by inheritance"""
