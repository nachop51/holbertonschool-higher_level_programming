#!/usr/bin/python3
""" Unit Tests for rectangle module """
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class RectangleTest(unittest.TestCase):
    """ Unit Tests class for rectangle tests """

    def set_zero(self):
        """ Sets to 0 the instance counter of base """
        Base._Base__nb_objects = 0

    def test_2_0(self):
        ''' Type test for Rectangle class '''
        r = Rectangle(1, 1)
        self.assertTrue(type(r) is Rectangle)

    def test_2_1(self):
        ''' Rectangle class id tests '''
        self.set_zero()
        r = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        r3 = Rectangle(1, 1, 0, 0, -1)
        r4 = Rectangle(1, 1, 0, 0, 0)
        r5 = Rectangle(1, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, -1)
        self.assertEqual(r4.id, 0)
        self.assertEqual(r5.id, 3)
        self.assertEqual(Base._Base__nb_objects, 3)

    def test_2_2(self):
        ''' Tests for setters '''
        r = Rectangle(1, 1)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 1)

    def test_2_3(self):
        ''' Tests for setters '''
        r = Rectangle(5, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)

    def test_2_4(self):
        ''' Tests for setters '''
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_2_5(self):
        ''' Tests for setters '''
        self.set_zero()
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)
        self.assertEqual(Base._Base__nb_objects, 0)
        r = Rectangle(1, 1)
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_2_6(self):
        ''' Tests for setters '''
        self.set_zero()
        r1 = Rectangle(1, 2, 3, 4, -1)
        r2 = Rectangle(1, 2, 3, 4, 0)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r3.id, 1)

    def test_3_0(self):
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        self.assertEqual("height must be > 0", str(e.exception))

    def test_3_1(self):
        ''' Testing exceptions '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle("a", 1)
        self.assertEqual("width must be an integer", str(e.exception))

    def test_3_2(self):
        ''' Testing exceptions '''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, 1)
        self.assertEqual("width must be > 0", str(e.exception))

    def test_3_3(self):
        ''' Testing exceptions '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "a")
        self.assertEqual("height must be an integer", str(e.exception))

    def test_3_4(self):
        ''' Testing exceptions '''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -1)
        self.assertEqual("height must be > 0", str(e.exception))

    def test_3_5(self):
        ''' Testing exceptions '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, "a")
        self.assertEqual("x must be an integer", str(e.exception))

    def test_3_6(self):
        ''' Testing exceptions '''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 1, -1)
        self.assertEqual("x must be >= 0", str(e.exception))

    def test_3_7(self):
        ''' Testing exceptions '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, "a")
        self.assertEqual("y must be an integer", str(e.exception))

    def test_3_8(self):
        ''' Testing exceptions '''
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 1, 1, -1)
        self.assertEqual("y must be >= 0", str(e.exception))

    def test_3_9(self):
        ''' Testing exceptions '''
        class MyInt(int):
            ''' MyInt class '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(MyInt(1), MyInt(1))
        self.assertEqual("width must be an integer", str(e.exception))

    def test_3_10(self):
        ''' Testing exceptions '''
        class MyInt(int):
            ''' MyInt class '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, MyInt(1))
        self.assertEqual("height must be an integer", str(e.exception))

    def test_3_11(self):
        ''' Testing exceptions '''
        class MyInt(int):
            ''' MyInt class '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, MyInt(1))
        self.assertEqual("x must be an integer", str(e.exception))

    def test_3_12(self):
        ''' Testing exceptions '''
        class MyInt(int):
            ''' MyInt class '''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 1, 1, MyInt(1))
        self.assertEqual("y must be an integer", str(e.exception))

    def test_4_0(self):
        ''' Wrong amount of params '''
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError) as e:
            r.area(5)
        self.assertEqual(
            "area() takes 1 positional argument \
but 2 were given", str(e.exception))

    def test_4_1(self):
        ''' Tests for area method '''
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)

    def test_4_2(self):
        ''' More tests for area method '''
        r = Rectangle(15, 8)
        self.assertEqual(r.area(), 120)

    def test_4_3(self):
        ''' More tests for area method '''
        r = Rectangle(1, 2, 1, 1)
        self.assertEqual(r.area(), 2)

    def test_5_1(self):
        ''' Tests for display method '''
        r = Rectangle(4, 6)
        string = StringIO()
        sys.stdout = string
        r.display()
        output = string.getvalue()
        self.assertEqual(output, "####\n####\n####\n####\n####\n####\n")

    def test_5_2(self):
        ''' Tests for display method '''
        r = Rectangle(2, 3)
        string = StringIO()
        sys.stdout = string
        r.display()
        output = string.getvalue()
        self.assertEqual(output, "##\n##\n##\n")

    def test_5_3(self):
        ''' Tests for display method '''
        r = Rectangle(1, 1)
        string = StringIO()
        sys.stdout = string
        r.display()
        output = string.getvalue()
        self.assertEqual(output, "#\n")

    def test_6_1(self):
        ''' Tests for str method '''
        self.set_zero()
        r = Rectangle(1, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 0/0 - 1/1")

    def test_6_2(self):
        ''' Tests for str method '''
        r = Rectangle(6, 3, 1, 7)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 1/7 - 6/3")

    def test_6_3(self):
        ''' Tests for str method '''
        r = Rectangle(5, 5, 1, 1, -5)
        self.assertEqual(r.__str__(), "[Rectangle] (-5) 1/1 - 5/5")

    def test_6_4(self):
        ''' Tests for str method '''
        r = Rectangle(5, 5, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (3) 1/0 - 5/5")

    def test_6_5(self):
        ''' Tests for str method '''
        r = Rectangle(5, 5, 0, 3)
        self.assertEqual(r.__str__(), "[Rectangle] (4) 0/3 - 5/5")

    def test_7_1(self):
        ''' Tests for upgraded display method '''
        r = Rectangle(4, 4, 2, 1)
        string = StringIO()
        sys.stdout = string
        r.display()
        output = string.getvalue()
        self.assertEqual(output, """
  ####
  ####
  ####
  ####
""")

    def test_7_2(self):
        ''' Tests for upgraded display method '''
        r = Rectangle(3, 3, 1, 1)
        string = StringIO()
        sys.stdout = string
        r.display()
        output = string.getvalue()
        self.assertEqual(output, """
 ###
 ###
 ###
""")

    def test_7_3(self):
        ''' Tests for upgraded display method '''
        r = Rectangle(3, 3, 0, 3)
        string = StringIO()
        sys.stdout = string
        r.display()
        output = string.getvalue()
        self.assertEqual(output, """


###
###
###
""")

    def test_7_4(self):
        ''' Tests for upgraded display method '''
        r = Rectangle(3, 3, 0, 0)
        string = StringIO()
        sys.stdout = string
        r.display()
        output = string.getvalue()
        self.assertEqual(output, "###\n###\n###\n")

    def test_7_5(self):
        ''' Tests for upgraded display method '''
        r = Rectangle(3, 3, 3, 0)
        string = StringIO()
        sys.stdout = string
        r.display()
        output = string.getvalue()
        self.assertEqual(output, """   ###
   ###
   ###
""")

    def test_8_1(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r.__str__(), "[Rectangle] (10) 10/10 - 10/10")

    def test_8_2(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_8_3(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 2/10")

    def test_8_4(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 10/10 - 2/3")

    def test_8_5(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/10 - 2/3")

    def test_8_6(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_9_1(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(height=2)
        self.assertEqual(r.__str__(), "[Rectangle] (10) 10/10 - 10/2")

    def test_9_2(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=3)
        self.assertEqual(r.__str__(), "[Rectangle] (10) 10/10 - 3/10")

    def test_9_3(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(x=8, width=4)
        self.assertEqual(r.__str__(), "[Rectangle] (10) 8/10 - 4/10")

    def test_9_4(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(y=9, height=5)
        self.assertEqual(r.__str__(), "[Rectangle] (10) 10/9 - 10/5")

    def test_9_5(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(x=8, y=9, width=4, height=5)
        self.assertEqual(r.__str__(), "[Rectangle] (10) 8/9 - 4/5")

    def test_9_6(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(x=8, y=9, width=4, height=5, id=89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 8/9 - 4/5")

    def test_9_7(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(x=8, y=9, width=4, height=5, id=89, test=10)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 8/9 - 4/5")

    def test_9_8(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(x=8, y=9, width=4, height=5, id=89, test=10)
        r.update(id=15, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (15) 2/9 - 4/5")

    def test_9_9(self):
        ''' Tests for update method '''
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(1, 1, 1, 1, 1, x=8, y=9, width=4, height=5, id=89, test=10)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 1/1 - 1/1")

    def test_9_10(self):
        ''' Tests for update method '''
        self.set_zero()
        r = Rectangle(2, 2)
        r.update(16, 7, x=8, y=9, width=4, height=5, id=89, test=10)
        self.assertEqual(r.__str__(), "[Rectangle] (16) 0/0 - 7/2")

    def test_9_11(self):
        ''' Tests for update method '''
        self.set_zero()
        r = Rectangle(2, 2)
        r.update(16, 7, x=8, y=9, width=4, height=5, id=89, test=10)
        r.update(id=15, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (15) 2/0 - 7/2")

    def test_13_1(self):
        ''' Tests for to_dictionary method '''
        r = Rectangle(1, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1})

    def test_13_2(self):
        ''' Tests for to_dictionary method '''
        r = Rectangle(1, 2, 3, 4, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1})

    def test_13_3(self):
        ''' Tests for to_dictionary method '''
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(**{'x': 6, 'y': 7, 'id': 8, 'height': 9, 'width': 10})
        d = r.to_dictionary()
        self.assertEqual(d, {'x': 6, 'y': 7, 'id': 8,
                             'height': 9, 'width': 10})

    def test_13_4(self):
        ''' Tests for to_dictionary method '''
        self.set_zero()
        r = Rectangle(1, 1)
        d = r.to_dictionary()
        self.assertEqual(d, {'x': 0, 'y': 0, 'id': 1, 'height': 1, 'width': 1})

    def test_13_5(self):
        ''' Tests for to_dictionary method '''
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dict)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)
        self.assertTrue(r1.to_dictionary() == r2.to_dictionary())

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

    def test_16_5(self):
        ''' More tests for save_to_file method '''
        Rectangle.save_to_file(None)
        if os.path.exists('Rectangle.json'):
            string = StringIO()
            sys.stdout = string
            with open('Rectangle.json', 'r') as f:
                print(f.read())
            output = string.getvalue()
            self.assertEqual(output, "[]\n")
            os.remove('Rectangle.json')


if __name__ == '__main__':
    unittest.main()
