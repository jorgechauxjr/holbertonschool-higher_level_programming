#!/usr/bin/python3

import json


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
        dicct = []

        if list_objs is not None:
            for i in list_objs:
                dicct.append(cls.to_dictionary(i))

        with open(newfile, "w", encoding="UTF8") as lista:
            lista.write(cls.to_json_string(dicct))
