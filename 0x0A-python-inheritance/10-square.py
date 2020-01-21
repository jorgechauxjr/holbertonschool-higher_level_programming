#!/usr/bin/python3
class BaseGeometry:
    """Class BaseGeometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
    (task based on 8-rectangle.py)"""

    def __init__(self, width, height):
        """Constructor method for Rectangle
        Instantiation with width and height"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of rectangle"""

        area = self.__width * self.__height
        return area

    def __str__(self):
        """Returns string representation of a Rectangle"""

        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string


class Square(Rectangle):
    """Class Square that inherits from Rectangle (9-rectangle.py)"""

    def __init__(self, size):
        """Constructor method for square
        Instantiation with size"""

        super().__init__(size, size)
        self.__size = size
