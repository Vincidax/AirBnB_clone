import json
import os
from ..base_model import BaseModel


class FileStorage:
    """FileStorage class for managing file storage."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to the dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save the objects to the file."""
        with open(self.__file_path, 'w') as f:
            data = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(data, f)

    def reload(self):
        """Reload the objects from the file."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                self.__objects = {k: BaseModel(**v) for k, v in data.items()}
