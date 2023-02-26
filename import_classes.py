#!/usr/bin/env python3
''' Imports all classes '''
import sys

sys.path.append("/home/vagrant/AirBnB_clone/models")

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


my_classes = ['BaseModel', 'User', 'State', 'City',
              'Amenity', 'Place', 'Review']
