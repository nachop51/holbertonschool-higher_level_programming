#!/usr/bin/python3
""" Unit Tests for square module """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys


class RectangleTest(unittest.TestCase):
    """ Unit Tests class for square tests """

    def set_zero(self):
        """ Sets to 0 the instance counter of base """
        Base._Base__nb_objects = 0

    def test_10_0(self):
        s = Square(1)
        self.assertTrue(type(s) is Square)

    def test_10_1(self):
        self.set_zero()
        s = Square(10)
        s2 = Square(1, 2)
        s3 = Square(5, 2, 3)
        s4 = Square(1, 2, 3, -1)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.id, 1)
        self.assertEqual(s2.width, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s3.height, 5)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 3)
        self.assertEqual(s4.id, -1)
        self.assertEqual(s4.y, 3)
        self.assertEqual(s4.x, 2)

    def test_10_2(self):
        s = Square(10)
        s2 = Square(1, 2)
        s3 = Square(5, 2, 3)
        s4 = Square(1, 2, 3, -1)
        self.assertEqual(s.area(), 100)
        self.assertEqual(s2.area(), 1)
        self.assertEqual(s3.area(), 25)
        self.assertEqual(s4.area(), 1)

    def test_10_3(self):
        self.set_zero()
        s = Square(10)
        s2 = Square(1, 2)
        s3 = Square(5, 2, 3)
        s4 = Square(1, 2, 3, -1)
        self.assertEqual(s.__str__(), "[Square] (1) 0/0 - 10")
        self.assertEqual(s2.__str__(), "[Square] (2) 2/0 - 1")
        self.assertEqual(s3.__str__(), "[Square] (3) 2/3 - 5")
        self.assertEqual(s4.__str__(), "[Square] (-1) 2/3 - 1")

    def test_10_4(self):
        s = Square(3, 1, 1, 10)
        string = StringIO()
        sys.stdout = string
        s.display()
        output = string.getvalue()
        self.assertEqual(output, "\n ###\n ###\n ###\n")

    def test_10_5(self):
        s = Square(3, 0, 1, 10)
        string = StringIO()
        sys.stdout = string
        s.display()
        output = string.getvalue()
        self.assertEqual(output, "\n###\n###\n###\n")

    def test_10_6(self):
        s = Square(3, 1, 0, 10)
        string = StringIO()
        sys.stdout = string
        s.display()
        output = string.getvalue()
        self.assertEqual(output, " ###\n ###\n ###\n")

    def test_10_7(self):
        with self.assertRaises(TypeError) as e:
            s = Square("1")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_10_8(self):
        with self.assertRaises(TypeError) as e:
            s = Square(1, "1")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_10_9(self):
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, "betty")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_10_10(self):
        with self.assertRaises(ValueError) as e:
            s = Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_10_11(self):
        with self.assertRaises(ValueError) as e:
            s = Square(-1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_10_12(self):
        with self.assertRaises(ValueError) as e:
            s = Square(1, -1)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_10_13(self):
        with self.assertRaises(ValueError) as e:
            s = Square(1, 0, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_10_14(self):
        class MyInt(int):
            """ MyInt class """
        with self.assertRaises(TypeError) as e:
            s = Square(MyInt(1))
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_10_15(self):
        class MyInt(int):
            """ MyInt class """
        with self.assertRaises(TypeError) as e:
            s = Square(1, MyInt(1))
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_10_16(self):
        class MyInt(int):
            """ MyInt class """
        with self.assertRaises(TypeError) as e:
            s = Square(1, 1, MyInt(1))
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_11_1(self):
        s = Square(10)
        s.size = 5
        self.assertEqual(s.size, 5)

    def test_11_2(self):
        s = Square(10)
        with self.assertRaises(TypeError) as e:
            s.size = "5"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_11_3(self):
        s = Square(10)
        with self.assertRaises(ValueError) as e:
            s.size = 0
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_11_4(self):
        class MyInt(int):
            """ MyInt class """
        with self.assertRaises(TypeError) as e:
            s = Square(10)
            s.size = MyInt(5)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_12_1(self):
        s = Square(10)
        s.update(10)
        self.assertEqual(s.__str__(), "[Square] (10) 0/0 - 10")

    def test_12_2(self):
        s = Square(10, 10)
        s.update(10, 2)
        self.assertEqual(s.__str__(), "[Square] (10) 10/0 - 2")

    def test_12_3(self):
        s = Square(10, 10, 10)
        s.update(10, 2, 3)
        self.assertEqual(s.__str__(), "[Square] (10) 3/10 - 2")

    def test_12_4(self):
        s = Square(10, 10, 10, 10)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.__str__(), "[Square] (10) 3/4 - 2")

    def test_12_5(self):
        s = Square(10, 10, 10, 10)
        s.update(10, 2, 3, 4, "5")
        self.assertEqual(s.__str__(), "[Square] (10) 3/4 - 2")

    def test_12_6(self):
        s = Square(10, 10, 10, 10)
        s.update(10, 2, 3, 4, x=8, y=9, size=4, id=89)
        self.assertEqual(s.__str__(), "[Square] (10) 3/4 - 2")

    def test_12_7(self):
        s = Square(10, 10, 10, 10)
        s.update(1, x=8, y=9, size=4, id=89)
        self.assertEqual(s.__str__(), "[Square] (1) 10/10 - 10")

    def test_12_8(self):
        s = Square(10, 10, 10, 10)
        s.update(x=8, y=9, size=4, id=89)
        self.assertEqual(s.__str__(), "[Square] (89) 8/9 - 4")

    def test_12_8(self):
        s = Square(10, 10, 10, 10)
        s.update(x=8, id=89, size=4, y=9)
        self.assertEqual(s.__str__(), "[Square] (89) 8/9 - 4")

    def test_12_9(self):
        s = Square(10, 10, 10, 10)
        s.update(size=5, y=3)
        self.assertEqual(s.__str__(), "[Square] (10) 10/3 - 5")

    def test_12_10(self):
        s = Square(10, 10, 10, 10)
        s.update(id=5, x=3)
        self.assertEqual(s.__str__(), "[Square] (5) 3/10 - 10")

    def test_12_11(self):
        s = Square(10, 10, 10, 10)
        s.update(id=5, size=3, x=3)
        self.assertEqual(s.__str__(), "[Square] (5) 3/10 - 3")

    def test_14_1(self):
        s = Square(10, 10, 10, 10)
        self.assertEqual(s.to_dictionary(), {'x': 10, 'y': 10,
                                             'id': 10, 'size': 10})

    def test_14_2(self):
        s = Square(10, 10, 10, 10)
        s.update(id=5, size=3, x=3)
        self.assertEqual(s.to_dictionary(), {'x': 3, 'y': 10,
                                             'id': 5, 'size': 3})

    def test_14_3(self):
        s1 = Square(10, 6, 3, 4)
        s1_dict = s1.to_dictionary()
        s2 = Square(1)
        s2.update(**s1_dict)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

    def test_14_4(self):
        self.set_zero()
        s1 = Square(5, 2)
        self.assertEqual(s1.to_dictionary(), {'x': 2, 'y': 0, 'id': 1,
                                              'size': 5})


if __name__ == '__main__':
    unittest.main()
