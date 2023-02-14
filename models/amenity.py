#!/usr/bin/env python3
''' Contains Amenity class '''

from models.base_model import BaseModel


class Amenity(BaseModel):
        ''' Represents an amenity '''

        class_att_dict = {'name': str}

        name = ''
