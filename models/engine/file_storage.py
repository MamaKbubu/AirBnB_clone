#!/usr/bin/python3

import json


class FileStorage:
    """Represents File Storage using two attributes:
    __file_path (str): The name of the file to save objects to.
    __objects: dictionary - empty but will store all objects by <class name>.id (ex: to store a BaseModel object """
    __file__path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"]= obj

    def save(self):
        """: serializes __objects to the JSON file (path: __file_path)"""
        cp_dict = FileStorage.__objects
        dicobj = {}
        for obj in cp_dict.keys():
            dicobj[obj]= cp_dict[obj].to_dict()
        with open(FileStorage.__file__path, "w") as f:
            json.dump(dicobj,f)

    def reload(self):
        """Deserializes the jsonfile if not , pass"""
        try:
            with open(FileStorage.__file__path, "r") as f:
                dicobj = json.load(f)
                for x in dicobj.values():
                    cls_name = x["__class__"]
                    del x["__class__"]
                    self.new(eval(cls_name)(**x))

        except FileNotFoundError:
            return
