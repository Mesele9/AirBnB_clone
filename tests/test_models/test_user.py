#!/usr/bin/env python3
''' unit testing for User class '''

import unittest
from models.user import User


class TestUser(unittest.TestCase):
        ''' class for testing User '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = User()
                self.assertTrue('id' in a.__dict__)
                self.assertTrue('created_at' in a.__dict__)
                self.assertTrue('updated_at' in a.__dict__)
                self.assertEqual(type(a.email), str)
                self.assertEqual(type(a.password), str)
                self.assertEqual(type(a.first_name), str)
                self.assertEqual(type(a.last_name), str)

        def test_str(self):
                ''' testing User's __str___ '''
                b = User(id='my_id')
                self.assertTrue(b.__str__().startswith('[User] (my_id)'))
