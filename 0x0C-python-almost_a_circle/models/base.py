#!/usr/bin/python3
"""This is class base"""
import json
import os


class Base:
    """Class that manage id attribute in all future classes
    and to avoid duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method initialize a Base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""

        newfile = "{}.json".format(cls.__name__)
        ls = []

        if list_objs is not None:
            for i in list_objs:
                ls.append(cls.to_dictionary(i))

        with open(newfile, "w", encoding='utf-8') as f:
            f.write(cls.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Square":
            dummy = cls(2)
            dummy.update(**dictionary)
            return dummy

        if cls.__name__ == "Rectangle":
            dummy = cls(2, 4)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        newfile = "{}.json".format(cls.__name__)
        my_list = []

        if os.path.isfile(newfile):
            with open(newfile, encoding="utf-8") as f:
                items = cls.from_json_string(f.read())
            for i in items:
                my_list.append(cls.create(**i))
            return my_list
        else:
            return []
