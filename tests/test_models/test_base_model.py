#!/usr/bin/env python3
''' unit testing for base class '''

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
        ''' class for testing Base Model '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = BaseModel()
                self.assertTrue('id' in a.__dict__)
                self.assertTrue('created_at' in a.__dict__)
                self.assertTrue('updated_at' in a.__dict__)
                self.assertEqual(type(a.id), str)

        def test_update(self):
                ''' testing that updated_at is updated automatically
                with changes '''
                b = BaseModel(sandwich='grilled cheese')
                self.assertEqual(b.sandwich, 'grilled cheese')
                prev_update = b.updated_at
                b.sandwich = 'ham and cheese'
                self.assertNotEqual(b.updated_at, prev_update)

        def test_str(self):
                ''' testing BaseModel's __str___ '''
                c = BaseModel(id='my_id')
                self.assertTrue(c.__str__().startswith('[BaseModel] (my_id)'))

        def test_to_dict_and_passing_dict_to_constructor(self):
                ''' testing to_dict method and passing
                a dict to the constructor '''
                test_dict = {'id': 'test_obj',
                             'created_at': '2018-06-08T19:45:36.469639',
                             'updated_at': '2018-06-08T19:45:36.469672',
                             '__class__': 'BaseModel',
                             'test_attribute': 'arbitrary'}
                d = BaseModel(**test_dict)
                d_dict = d.to_dict()
                self.assertEqual(d_dict, test_dict)


if __name__ == '__main__':
    unittest.main()
