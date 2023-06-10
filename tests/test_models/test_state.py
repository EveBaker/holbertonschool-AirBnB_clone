#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_name(self):
        state = State()
        self.assertEqual(state.name, '')
        state.name = 'California'
        self.assertEqual(state.name, 'California')


if __name__ == '__main__':
    unittest.main()
