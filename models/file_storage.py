#!/usr/bin/python3
"""This code will control the storage of the file or 
rather the website"""

import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

def all(self):
    return self.__objects

def new(self, obj):
    key = "{}.{}".format(obj.__class__.__name__, obj.id)
    self.__objects[key] = obj

def save(self):
    serialized_objs = {}
    for key, obj in self.__objects.items():
        serialized_objs[key] = obj.to_dict()
    with open(self.__file_path, "w") as f:
        json.dump(serialized_objs, f)

def reload(self):
    try:
        with open(self.__file_path, "r") as f:
            serialized_objs = json.load(f)
            for key, serialized_obj in serialized_objs.items():
                class_name, obj_id = key.split(".")
                obj_dict = {}
                for attr, value in serialized_obj.items():
                    if attr == "__class__":
                        class_name = value
                    else:
                        obj_dict[attr] = value
                module = __import__("models." + class_name.lower(), fromlist=[class_name])
                cls = getattr(module, class_name)
                obj = cls(**obj_dict)
                self.__objects[key] = obj
    except FileNotFoundError:
        pass
