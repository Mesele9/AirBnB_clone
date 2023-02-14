#!/usr/bin/env python3
''' unit testing for City class '''

import unittest
from models.city import City


class TestCity(unittest.TestCase):
        ''' class for testing City '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = City()
                self.assertEqual(type(a.name), str)
                self.assertEqual(type(a.state_id), str)
