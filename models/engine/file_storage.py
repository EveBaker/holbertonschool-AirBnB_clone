#!/usr/bin/python3
"""FILE STORAGE MODULE"""
import json
from models.base_model import BaseModel
from datetime import datetime
import models

class FileStorage:
    """STORE NEW FILES"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary of all objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key in data:
                    class_name = data[key]['__class__']
                    obj_dict = data[key]
                    cls = getattr(models, class_name)
                    instance = cls(**obj_dict)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass

def from_dict(self, obj_dict):
    class_name = obj_dict.get('__class__')
    if class_name:
        class_ = models.classes[class_name]
        obj = class_(**obj_dict)
        return obj
    else:
        raise ValueError("Missing '__class__' key in dictionary.")

def get(self, class_name, instance_id):
        key = "{}.{}".format(class_name, instance_id)
        return self.all().get(key)