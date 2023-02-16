#!/usr/bin/python3
"""
test_square unittest module
Created on Wed 15.02.2023
@author: Rungene
"""

import unittest
from models.square import Square
import inspect
import pep8
import sys
import io
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """"
    TestSquare - class for testing Square class methods
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Square, inspect.isfunction)

    def test_square_conform_pep8(self):
        """
        Test square.py conforms to PEP8
        """
        pep8_code_style = pep8.StyleGuide(quiet=True)
        result = pep8_code_style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_test_square_conform_pep8(self):
        """
        Test test_square.py conforms to PEP8
        """
        pep8_code_style = pep8.StyleGuide(quiet=True)
        result = pep8_code_style.check_files(
                 ['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_square_module_docstring(self):
        """
        tests if square module doc string exists
        """
        # doc = __import__('models/base').__doc__
        self.assertTrue(len('models/square.py'.__doc__) >= 1)

    def test_class_doc_string(self):
        """
        test if class dosctring exists
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_method_doc_string(self):
        """
        test if method docsting exists
        """
        for doc_mthds in self.setup:
            self.assertTrue(len(doc_mthds[1].__doc__) >= 1)

    def test_expected_values(self):
        """
        Testing expected Normal values just for size
        x, y and id
        """
        s0 = Square(1, 2)
        s1 = Square(1, 2, 3)
        s2 = Square(1, 2, 3, 4)
        self.assertEqual([s0.size, s0.x, s0.y, s0.id],
                         [1, 2, 0, 1])
        self.assertEqual([s1.size, s1.x, s1.y, s1.id],
                         [1, 2, 3, 2])
        self.assertEqual([s2.size, s2.x, s2.y, s2.id],
                         [1, 2, 3, 4])

    def test_wrong_input_vals(self):
        """
        Testing for zero and negative values
        """
        with self.assertRaises(ValueError):
            S = Square(0, 0)
        with self.assertRaises(ValueError):
            S = Square(-1, -1)
        with self.assertRaises(ValueError):
            S = Square(1, 1, -1, -1)
        with self.assertRaises(TypeError):
            S = Square()
        with self.assertRaises(TypeError):
            S = Square(1, 2, 3, 4, 5, 6, 7)

    def test_input_types(self):
        """
        Testing for different input types
        Raise exception where necessary
        """
        with self.assertRaises(TypeError):
            S = Square('size', 'x')
        with self.assertRaises(TypeError):
            S = Square(1.2, 1.3)
        with self.assertRaises(TypeError):
            S = Square(1, 'x', 'y')
        with self.assertRaises(TypeError):
            S = Square(1, 2, 2.3, 1.3)
        with self.assertRaises(TypeError):
            S = Square(True, False)
        with self.assertRaises(TypeError):
            S = Square(1, 2, True, False)
        with self.assertRaises(TypeError):
            S = Square([1, 2], 3, 4, 5)
        with self.assertRaises(TypeError):
            S = Square((1, 2), 3, 4, 5)
        with self.assertRaises(TypeError):
            S = Square((1, 2), 'x', 'y')
        with self.assertRaises(TypeError):
            S = Square({1: 1}, 2, 3, 4)
        with self.assertRaises(TypeError):
            S = Square({1: 2, 2: 3}, 5, 6)

    def test_area_mthd(self):
        """"
        Testing the area method
        """
        S = Square(10, 10)
        self.assertEqual(S.area(), 100)
        with self.assertRaises(TypeError):
            A = S.area(1)

    def test_str_mthd(self):
        """
        Testing the str method returns the corret formated string
        """
        r_string = Square(1, 2, 3, 4)
        self.assertEqual("[Square] (4) 2/3 - 1", str(r_string))

    def test_display1_mthd(self):
        """"
        Testing the display method prints as expected
        """
        S = Square(2, 0, 0, 1)
        with redirect_stdout(io.StringIO()) as buffer_io:
            S.display()
            out = buffer_io.getvalue()
            self.assertEqual(out, ('#' * 2 + '\n') * 2)

    def test_update_args(self):
        """
        Testing update method(args).confirming it updates as expected
        """
        r1 = Square(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(89, r1.id)
        r1.update(89, 2)
        self.assertEqual(2, r1.size)
        r1.update(89, 2, 3)
        self.assertEqual(10, r1.x)
        r1.update(89, 2, 3, 4)
        self.assertEqual(10, r1.y)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(5, r1.y)

    def test_update_kwargs(self):
        """
        Testing update method(kwargs).confirming it updates as expected
        """
        r1 = Square(10, 10, 10, 10)
        r1.update(size=1)
        self.assertEqual(10, r1.size)
        r1.update(size=1, x=2)
        self.assertEqual([10, 2], [r1.size, r1.x])
        r1.update(y=1, size=2, x=3, id=89)
        self.assertEqual([1, 10, 3, 89], [r1.y, r1.size, r1.x, r1.id])
        r1.update(x=1, size=2, y=3)
        self.assertEqual([1, 10, 3], [r1.x, r1.size, r1.y])
        r1.update(x=9, y=10)
        self.assertEqual([9, 10], [r1.x, r1.y])
