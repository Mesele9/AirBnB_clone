#!/usr/bin/env python3
''' Contains base model for future classes '''

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
        ''' Sets attributes and methods to be used in all future models '''

        class_att_dict = dict()

        def __init__(self, *args, **kwargs):
                ''' Initializes an object '''
                for key in kwargs.keys():
                        if key == 'created_at' or key == 'updated_at':
                                self.__dict__[key] = datetime.strptime(
                                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                        else:
                                self.__dict__[key] = kwargs[key]
                if 'id' not in self.__dict__.keys():
                        self.id = str(uuid4())
                if 'created_at' not in self.__dict__.keys():
                        self.created_at = datetime.today()
                models.storage.new(self)
                models.storage.save()

        def __str__(self):
                ''' Printable string of object '''
                return '[{}] ({}) {}'.format(
                        self.__class__.__name__, self.id, self.__dict__)

        def __repr__(self):
                ''' Repr is same as str for formatting reasons '''
                return self.__str__()

        def __setattr__(self, name, value):
                ''' Setattr is customized for updating '''
                self.__dict__[name] = value
                self.save()

        def save(self):
                ''' Updates updated_at attribute and saves to file '''
                self.__dict__['updated_at'] = datetime.today()
                models.storage.save()

        def to_dict(self):
                ''' Creates dictionary for easy saving to JSON '''
                base_dict = dict(self.__dict__)
                base_dict['__class__'] = self.__class__.__name__
                base_dict['created_at'] = self.created_at.isoformat()
                base_dict['updated_at'] = self.updated_at.isoformat()
                return base_dict
