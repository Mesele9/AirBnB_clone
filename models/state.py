#!/usr/bin/env python3
''' Contains State class '''

from models.base_model import BaseModel


class State(BaseModel):
        ''' Represents a state in USA '''

        class_att_dict = {'name': str}

        name = ''
