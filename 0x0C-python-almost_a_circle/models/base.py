#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        newlist = []
        if list_objs is None:
            cls.to_json_string(list_objs)

        with open(filename, "w") as Myfile:
            for item in list_objs:
                newlist.append(cls.to_dictionary(item))

            Myfile.write(cls.to_json_string(newlist))
