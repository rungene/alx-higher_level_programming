#!/usr/bin/python3
"""
test_square unittest module
Created on Monday 15.02.2023
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
    TestSquare - class for testing Rectangle class methods
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
        Test test_square module  conforms to PEP8
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
