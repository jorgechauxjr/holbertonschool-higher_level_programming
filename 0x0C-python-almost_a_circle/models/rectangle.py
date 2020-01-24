#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method, initialize a Rectangle"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """Getter for the width"""

            return self.__width

        @property
        def height(self):
            """Getter for the height"""

            return self.__height

        @property
        def x(self):
            """Getter for x"""

            return self.__x

        @property
        def y(self):
            """Getter for y"""

        @width.setter
        def width(self, width):
            """Setter for width."""

            self.__width = width

        @height.setter
        def height(self, height):
            """Setter for height"""

            self.__height = height

        @x.setter
        def x(self, x):
            """Setter for x"""

            self.__x

        @y.setter
        def y(self, y):
            """Setter for y"""

            self.__y = y
