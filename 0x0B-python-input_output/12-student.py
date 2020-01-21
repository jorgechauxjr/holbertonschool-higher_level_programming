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

        my_dict = self.__dict__

        if type(attrs) is list and all(type(x) == str for x in attrs):
            return {y: my_dict[y] for y in my_dict if y in attrs}
        return my_dict
