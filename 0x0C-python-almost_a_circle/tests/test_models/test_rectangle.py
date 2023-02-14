#!/usr/bin/python3
"""
test_rectangel unittest module
Created on Monday 13.02.2023
@author: Rungene
"""

import unittest
from models.rectangle import Rectangle
import inspect
import pep8


class TestRec(unittest.TestCase):
    """"
    TestRec - class for testing Rectangle class methods
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_rectangle_conform_pep8(self):
        """
        Test rectangle.py conforms to PEP8
        """
        pep8_code_style = pep8.StyleGuide(quiet=True)
        result = pep8_code_style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_classrectangletest_conform_pep8(self):
        """
        Test test_rectangle.py conforms to PEP8
        """
        pep8_code_style = pep8.StyleGuide(quiet=True)
        result = pep8_code_style.check_files(
                 ['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_rectanglemodule_docstring(self):
        """
        tests if rectangle module doc string exists
        """
        # doc = __import__('models/base').__doc__
        self.assertTrue(len('models/rectangle.py'.__doc__) >= 1)

    def test_class_doc_string(self):
        """
        test if class dosctring exists
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_method_doc_string(self):
        """
        test if method docsting exists
        """
        for doc_mthds in self.setup:
            self.assertTrue(len(doc_mthds[1].__doc__) >= 1)

    def test_expected_values(self):
        """
        Testing expected Normal values just for width and height
        x, y and id
        """
        R0 = Rectangle(1, 2)
        R1 = Rectangle(1, 2, 3)
        R2 = Rectangle(1, 2, 3, 4)
        R3 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual([R0.width, R0.height, R0.x, R0.y, R0.id],
                         [1, 2, 0, 0, 1])
        self.assertEqual([R1.width, R1.height, R1.x, R1.y, R1.id],
                         [1, 2, 3, 0, 2])
        self.assertEqual([R2.width, R2.height, R2.x, R2.y, R2.id],
                         [1, 2, 3, 4, 3])
        self.assertEqual([R3.width, R3.height, R3.x, R3.y, R3.id],
                         [1, 2, 3, 4, 5])

    def test_wrong_input_vals(self):
        """
        Testing for zero and negative values
        """
        with self.assertRaises(ValueError):
            R = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            R = Rectangle(-1, -1)
        with self.assertRaises(ValueError):
            R = Rectangle(1, 1, -1, -1)
        with self.assertRaises(TypeError):
            R = Rectangle()
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_input_types(self):
        """
        Testing for different input types
        Raise exception where necessary
        """
        with self.assertRaises(TypeError):
            R = Rectangle('height', 'width')
        with self.assertRaises(TypeError):
            R = Rectangle(1.2, 1.3)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 1, 'x', 'y')
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 2.3, 1.3)
        with self.assertRaises(TypeError):
            R = Rectangle(True, False)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, True, False)
        with self.assertRaises(TypeError):
            R = Rectangle([1, 2], 3, 4, 5)
        with self.assertRaises(TypeError):
            R = Rectangle((1, 2), 3, 4, 5)
        with self.assertRaises(TypeError):
            R = Rectangle((1, 2), 'x', 'y')
        with self.assertRaises(TypeError):
            R = Rectangle({1: 1}, 2, 3, 4)
        with self.assertRaises(TypeError):
            R = Rectangle({1: 2, 2: 3}, 5, 6)

    def test_area_mthd(self):
        """"
        Testing the area method with
        """
        R = Rectangle(10, 10)
        self.assertEqual(R.area(), 100)
        with self.assertRaises(TypeError):
            A = R.area(1)

    def test_str_mthd(self):
        """
        Testing the str method returns the corret formated string
        """
        r_string = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", str(r_string))
