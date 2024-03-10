import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes and deserializes instances to/from JSON file"""

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = self._serialize_obj(obj)
        with open(self.__file_path, 'w') as file:
            json.dump(serialized, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                serialized = json.load(file)
                for key, serialized_obj in serialized.items():
                    cls_name, obj_id = key.split('.')
                    obj = self._deserialize_obj(cls_name, serialized_obj)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def _serialize_obj(self, obj):
        """Serialize a generic object"""
        if isinstance(obj, Place):
            return self._serialize_place(obj)
        elif isinstance(obj, State):
            return self._serialize_state(obj)
        elif isinstance(obj, City):
            return self._serialize_city(obj)
        elif isinstance(obj, Amenity):
            return self._serialize_amenity(obj)
        elif isinstance(obj, Review):
            return self._serialize_review(obj)
        else:
            return obj.to_dict()

    def _deserialize_obj(self, cls_name, serialized):
        """Deserialize a generic object"""
        if cls_name == 'Place':
            return self._deserialize_place(serialized)
        elif cls_name == 'State':
            return self._deserialize_state(serialized)
        elif cls_name == 'City':
            return self._deserialize_city(serialized)
        elif cls_name == 'Amenity':
            return self._deserialize_amenity(serialized)
        elif cls_name == 'Review':
            return self._deserialize_review(serialized)
        else:
            return self.classes[cls_name](**serialized)

    def _serialize_place(self, obj):
        """Serialize a Place object"""
        serialized = obj.to_dict()
        # Add any additional serialization logic specific to Place
        return serialized

    def _deserialize_place(self, serialized):
        """Deserialize a Place object"""
        # Add any additional deserialization logic specific to Place
        place = Place(**serialized)
        return place
