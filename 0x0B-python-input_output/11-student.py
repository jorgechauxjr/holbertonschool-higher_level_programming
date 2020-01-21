#!/usr/bin/python3
class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary representation
        of a Student instance. (same as 10-class_to_json.py)"""

        return self.__dict__
