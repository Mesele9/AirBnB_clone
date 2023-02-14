#!/usr/bin/env python3
''' Contains City class '''

from models.base_model import BaseModel


class City(BaseModel):
        ''' Represents a city '''

        class_att_dict = {'name': str, 'state_id': str}

        name = ''
        state_id = ''
