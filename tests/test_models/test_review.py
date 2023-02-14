#!/usr/bin/env python3
''' unit testing for Review class '''

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
        ''' class for testing Review '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = Review()
                self.assertEqual(type(a.place_id), str)
                self.assertEqual(type(a.user_id), str)
                self.assertEqual(type(a.text), str)
