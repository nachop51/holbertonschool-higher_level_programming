#!/usr/bin/python3
""" Unit Tests for base module """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
import os
from io import StringIO


class BaseTest(unittest.TestCase):
    """ Unit Tests class for base tests """

    def set_zero(self):
        """ Sets to 0 the instance counter of base """
        Base._Base__nb_objects = 0

    def test_1_0(self):
        ''' Test type for Base class '''
        b = Base(1)
        self.assertTrue(type(b) is Base)

    def test_1_1(self):
        ''' Test ID '''
        self.set_zero()
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
        ''' Some more ids '''
        self.set_zero()
        b = Base(-1)
        b2 = Base(0)
        b3 = Base()
        self.assertEqual(b.id, -1)
        self.assertEqual(b2.id, 0)
        self.assertEqual(b3.id, 1)

    def test_15_1(self):
        ''' Test to_json_string method '''
        self.set_zero()
        r = Rectangle(10, 7, 2, 8)
        r_dict = r.to_dictionary()
        json_dictionary = Base.to_json_string([r_dict])
        self.assertTrue(type(r_dict) is dict)
        self.assertTrue(type(json_dictionary) is str)
        self.assertEqual(
            json_dictionary, '[{"id": 1, "width": 10, \
"height": 7, "x": 2, "y": 8}]'
        )

    def test_15_2(self):
        ''' More to_json_string tests '''
        json_dictionary = Base.to_json_string([])
        self.assertTrue(type(json_dictionary) is str)
        self.assertEqual(json_dictionary, "[]")

    def test_15_3(self):
        self.set_zero()
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        r1, r2 = r1.to_dictionary(), r2.to_dictionary()
        json_dictionary = Base.to_json_string([r1, r2])
        self.assertTrue(type(json_dictionary) is str)
        self.assertEqual(json_dictionary, '[{"id": 1, "width": 1, \
"height": 2, "x": 3, "y": 4}, {"id": 2, "width": 5, \
"height": 6, "x": 7, "y": 8}]')

    def test_16_1(self):
        ''' Testing save_to_file method '''
        self.set_zero()
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6)
        Rectangle.save_to_file([r1, r2])
        if os.path.exists('Rectangle.json'):
            string = StringIO()
            sys.stdout = string
            with open('Rectangle.json', 'r') as f:
                print(f.read())
            output = string.getvalue()
            self.assertEqual(output, '[{"id": 1, "width": 1, \
"height": 2, "x": 3, "y": 4}, {"id": 2, "width": 5, \
"height": 6, "x": 0, "y": 0}]\n')
            os.remove('Rectangle.json')

    def test_16_2(self):
        ''' More tests for save_to_file method '''
        Rectangle.save_to_file([])
        if os.path.exists('Rectangle.json'):
            string = StringIO()
            sys.stdout = string
            with open('Rectangle.json', 'r') as f:
                print(f.read())
            output = string.getvalue()
            self.assertEqual(output, "[]\n")
            os.remove('Rectangle.json')

    def test_16_3(self):
        ''' More tests for save_to_file method '''
        self.set_zero()
        r1 = Square(1, 2, 3, 4)
        r2 = Square(5, 6)
        Square.save_to_file([r1, r2])
        if os.path.exists('Square.json'):
            string = StringIO()
            sys.stdout = string
            with open('Square.json', 'r') as f:
                print(f.read())
            output = string.getvalue()
            self.assertEqual(output, '[{"id": 4, "size": 1, \
"x": 2, "y": 3}, {"id": 1, "size": 5, \
"x": 6, "y": 0}]\n')
            os.remove('Square.json')

    def test_16_4(self):
        ''' More tests for save_to_file method '''
        Square.save_to_file([])
        if os.path.exists('Square.json'):
            string = StringIO()
            sys.stdout = string
            with open('Square.json', 'r') as f:
                print(f.read())
            output = string.getvalue()
            self.assertEqual(output, "[]\n")
            os.remove('Square.json')

    def test_17_1(self):
        ''' Tests for from_json_string method '''
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_dictionary = Base.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_dictionary)
        self.assertTrue(type(list_output) is list)
        self.assertTrue(type(json_dictionary) is str)
        self.assertEqual(json_dictionary, '[{"id": 89, "width": 10, \
"height": 4}, {"id": 7, "width": 1, "height": 7}]')

    def test_17_2(self):
        ''' More tests for from_json_string method '''
        list_input = None
        output = Base.from_json_string(list_input)
        self.assertEqual(output, [])

    def test_17_3(self):
        ''' More tests for from_json_string method '''
        list_input = []
        json_dictionary = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_dictionary)
        self.assertEqual(list_output, [])

    def test_18_1(self):
        ''' Dictionary to instance test '''
        self.set_zero()
        r1 = Rectangle(1, 2, 3)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 3/0 - 1/2')

    def test_18_2(self):
        ''' Dictionary to instance test '''
        self.set_zero()
        s1 = Square(1, 2, 3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(s1.__str__(), '[Square] (1) 2/3 - 1')

    def test_19_1(self):
        ''' Tests for load_from_file method '''
        self.set_zero()
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        if os.path.exists('Rectangle.json'):
            list_output = Rectangle.load_from_file()
            for i, rect in enumerate(list_output):
                self.assertTrue(type(rect) is Rectangle)
                self.assertEqual(rect.__str__(), list_input[i].__str__())
            os.remove('Rectangle.json')

    def test_19_2(self):
        ''' More tests for load_from_file method '''
        self.set_zero()
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6)
        list_input = [s1, s2]
        Square.save_to_file(list_input)
        if os.path.exists('Square.json'):
            list_output = Square.load_from_file()
            for i, sq in enumerate(list_output):
                self.assertTrue(type(sq) is Square)
                self.assertEqual(sq.__str__(), list_input[i].__str__())
            os.remove('Square.json')

    def test_19_3(self):
        ''' More tests for load_from_file method '''
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])

    def test_19_4(self):
        ''' More tests for load_from_file method '''
        list_output = Square.load_from_file()
        self.assertEqual(list_output, [])

    def test_20_1(self):
        ''' Tests for save_to_file_csv method '''
        self.set_zero()
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(2, 4)
        list_rectangles = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles)
        if os.path.exists('Rectangle.csv'):
            list_rectangles_output = Rectangle.load_from_file_csv()
            for i, rect in enumerate(list_rectangles_output):
                self.assertTrue(type(rect) is Rectangle)
                self.assertEqual(rect.__str__(), list_rectangles[i].__str__())
            os.remove('Rectangle.csv')

    def test_20_2(self):
        ''' More tests for save_to_file_csv method '''
        self.set_zero()
        s1 = Square(1, 2, 3)
        s2 = Square(2, 4)
        list_squares = [s1, s2]
        Square.save_to_file_csv(list_squares)
        if os.path.exists('Square.csv'):
            list_squares_output = Square.load_from_file_csv()
            for i, sq in enumerate(list_squares_output):
                self.assertTrue(type(sq) is Square)
                self.assertEqual(sq.__str__(), list_squares[i].__str__())
            os.remove('Square.csv')


if __name__ == '__main__':
    unittest.main()
