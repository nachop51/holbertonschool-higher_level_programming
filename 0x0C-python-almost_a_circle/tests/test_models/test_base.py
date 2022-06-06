#!/usr/bin/python3
""" Unit Tests for base module """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """ Unit Tests class for base tests """

    def set_zero(self):
        """ Sets to 0 the instance counter of base """
        Base._Base__nb_objects = 0

    def test_1_0(self):
        b = Base(1)
        self.assertTrue(type(b) is Base)

    def test_1_1(self):
        b = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_1_2(self):
        self.set_zero()
        b = Base(-1)
        b2 = Base(0)
        b3 = Base()
        self.assertEqual(b.id, -1)
        self.assertEqual(b2.id, 0)
        self.assertEqual(b3.id, 1)

    def test_15_1(self):
        r = Rectangle(10, 7, 2, 8)
        r_dict = r.to_dictionary()
        json_dictionary = Base.to_json_string([r_dict])
        self.assertTrue(type(r_dict) is dict)
        self.assertTrue(type(json_dictionary) is str)


if __name__ == '__main__':
    unittest.main()
