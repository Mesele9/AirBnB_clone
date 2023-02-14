#!/usr/bin/env python3
''' unit testing for Place class '''

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
        ''' class for testing Place '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = Place()
                self.assertEqual(type(a.city_id), str)
                self.assertEqual(type(a.state_id), str)
                self.assertEqual(type(a.name), str)
                self.assertEqual(type(a.description), str)
                self.assertEqual(type(a.number_rooms), int)
                self.assertEqual(type(a.number_bathrooms), int)
                self.assertEqual(type(a.max_guest), int)
                self.assertEqual(type(a.price_by_night), float)
                self.assertEqual(type(a.latitude), float)
                self.assertEqual(type(a.longitude), float)
