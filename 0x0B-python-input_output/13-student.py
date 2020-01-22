#!/usr/bin/python3
class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation
        of a Student instance. (same as 10-class_to_json.py)"""

        if attrs is None:
            return self.__dict__
        dict = {}
        for i in attrs:
            if i in self.__dict__:
                dict[i] = self.__dict__[i]
        return dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""

        for key, value in json.items():
            self.__dict__[key] = value
