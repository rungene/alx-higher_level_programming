# 0x0C. Python - Almost a circle

# Background Context

The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.

In this project, you will review everything about Python:

- Import
- Exceptions
- Class
- Private attribute
- Getter/Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read/Write file

You will also learn about:

- args and kwargs
- Serialization/Deserialization
- JSON

# Resources

- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

# Requirements

## Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should be documented: python3 -c 'print(__import__("my\_module").__doc__)'
- All your classes should be documented: python3 -c 'print(__import__("my\_module").MyClass.__doc__)'
- All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my\_module").my\_function.__doc__)' and python3 -c 'print(__import__("my\_module").MyClass.my\_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

# Python Unit Tests

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- All your test files should be python files (extension: .py)
- All your test files and folders should start with test_
- Your file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test\_base.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test\_models/test\_base.py
- We strongly encourage you to work together on test cases so that you don’t miss any edge case

# Tasks

**0. If it's not tested it doesn't work**

All your files, classes and methods must be unit tested and be PEP 8 validated.

**1. Base class**

Write the first class Base:

Create a folder named models with an empty file __init__.py inside - with this file, the folder will become a Python package

Create a file named models/base.py:

    - Class Base: 
    - private class attribute __nb_objects = 0
    - class constructor: def __init/__(self, id=None)::

        - if id is not None, assign the public instance attribute id with this argument value - you can assume id is an integer and you don’t need to test the type of it
        - otherwise, increment __nb\_objects and assign the new value to the public instance attribute id

This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)