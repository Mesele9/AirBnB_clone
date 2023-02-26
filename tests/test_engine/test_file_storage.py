#!/usr/bin/env python3
''' unit testing for file storage class '''


from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models import storage
import unittest
import json


class TestFileStorage(unittest.TestCase):
    ''' class for testing File Storage '''
    def test_store_object(self):
        ''' testing storage of objects '''
        test_dict = {'id': 'test_storage',
                     'created_at': '2018-06-08T19:45:36.469639',
                     'updated_at': '2018-06-08T19:45:36.469672',
                     'test_attribute': 'still_arbitrary'}
        a = BaseModel(**test_dict)
        b = Place(**test_dict)
        with open('file.json', 'r') as f:
            file_dict = json.load(f)

        self.assertTrue('BaseModel.test_storage' in file_dict.keys())
        self.assertEqual(a.to_dict(), file_dict['BaseModel.test_storage'])

        self.assertTrue('Place.test_storage' in file_dict.keys())
        self.assertEqual(b.to_dict(), file_dict['Place.test_storage'])

    def testing_all(self):
        ''' testing retrieval of objects '''
        test_dict = {'id': 'test_retrieval',
                     'created_at': '2018-06-08T19:45:36.469639',
                     'updated_at': '2018-06-08T19:45:36.469672',
                     'test_attribute': 'still_arbitrary'}
        c = BaseModel(**test_dict)
        d = Review(**test_dict)
        all_objects = storage.all()

        from_json = all_objects['BaseModel.test_retrieval'].__dict__
        self.assertEqual(from_json, c.__dict__)

        self.assertEqual(all_objects[
            'Review.test_retrieval'].__dict__, d.__dict__)
