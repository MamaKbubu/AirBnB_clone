#!usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:
    """This is a simple break down of the source,
    this class will explain everything"""
    def __init__(self):
        """creates instance variables"""
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def __str__(self):
        """returns human readable comments"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """it gives you the current time with updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type().__name__
        new_dict["created_at"] = self.created_at.isoformat
        new_dict["updated_at"] = self.updated_at.isoformat
        return new_dict
