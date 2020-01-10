#!/usr/bin/python3
# A class Square that defines a square


class Square:
    def __init__(self, size=0):  # init allow square class to be used
        self.__size = size   # asign private instance attribute size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(v) is not int for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(v < 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value
