#!/usr/bin/python3
"""
Unittest class module
Created on Monday 13.02.2023
@author: Rungene
"""

import unittest
from models.base import Base
import inspect
import pep8


class TestBase(Unittest.Testcase):
    """"
    TestBase - class for testing Base class methods
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_base_conform_pep8(self):
        """
        Test base.py conforms to PEP8
        """
        pep8_code_style = pep8.StyleGuide(quiet=True)
        result = pep8_code_style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_classbasetest_conform_pep8(self):
        """
        Test tes_base.py conforms to PEP8
        """
        pep8_code_style = pep8.StyleGuide(quiet=True)
        result = pep8_code_style.check_files(
                 ['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_basemodule_docstring(self):
        """
        tests if base module doc string exists
        """
        doc = __import__('models/base.py').__doc__
        self.assertTrue(len(doc) >= 1)

    def test_class_docstring(self):
        """
        test if class dosctring exists
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_method_docstring(self):
        """
        test if method docsting exists
        """
        for doc_mthd in cls.setup:
            self.assertTrue(len(doc_mthd[1].__doc__) >= 1)
