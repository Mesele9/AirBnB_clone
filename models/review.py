#!/usr/bin/env python3
''' Contains Review class '''

from models.base_model import BaseModel


class Review(BaseModel):
        ''' Review of a place '''

        class_att_dict = {'place_id': str, 'user_id': str, 'text': str}

        place_id = ''
        user_id = ''
        text = ''
