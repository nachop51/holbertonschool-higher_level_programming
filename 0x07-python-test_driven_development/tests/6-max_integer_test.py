#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for tests"""

    def test_list(self):
        """Tests a normal list"""
        result = max_integer([124, 22, 533])
        self.assertEqual(result, 533)

    def test_letter(self):
        """Test passing a letter"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'a'])

    def test_none(self):
        """Test passing none"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_negatives(self):
        """Test with negative numbers"""
        result = max_integer([-20, -15, -33])
        self.assertEqual(result, -15)

    def test_empty(self):
        """Tests empty list case"""
        result = max_integer([])
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
