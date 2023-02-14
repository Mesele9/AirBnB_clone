#!/usr/bin/env python3
''' unit testing for State class '''

import unittest
from models.state import State


class TestState(unittest.TestCase):
        ''' class for testing State '''

        def test_attribute_creation(self):
                ''' testing that instance initializes with correct
                attributes '''
                a = State()
                self.assertEqual(type(a.name), str)
