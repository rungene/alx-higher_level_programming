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
