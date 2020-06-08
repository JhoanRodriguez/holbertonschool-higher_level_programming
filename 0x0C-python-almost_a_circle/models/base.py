#!/usr/bin/python3
"""
This modules contains a class Base
"""
import json


class Base:
    """
    This class has a private attribute __nb_objects = 0
    a class constructor definition to check for id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of class which checks for id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This functions returns the json string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function writes the json
        string representation of list_objs
        to a file
        """
        filename = cls.__name__ + ".json"
        newlist = []
        if list_objs is None:
            cls.to_json_string(list_objs)
        else:
            for item in list_objs:
                newlist.append(cls.to_dictionary(item))
        with open(filename, "w") as Myfile:
            Myfile.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """
        This function returns the list
        of the json string represenation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This function returns an instance
        with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            aux = cls(1, 1)
        elif cls.__name__ == "Square":
            aux = cls(1)
        aux.update(**dictionary)
        return aux

    @classmethod
    def load_from_file(cls):
        """
        This function returns a list
        of instances
        """
        filename = cls.__name__ + ".json"
        newlist = []
        if cls is None:
            return newlist
        try:
            with open(filename, "r") as Myfile:
                newlist = cls.from_json_string(Myfile.read())
            for item in range(len(newlist)):
                newlist[item] = cls.create(**newlist[item])
        except Exception:
            pass
        return newlist
