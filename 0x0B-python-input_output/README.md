# 0x0B-python-input\_output

**Python OOP Inheritance***

man or help:

- python3

## Resources

**Read or watch:**

    - [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
    - [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
    - [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf)(until “11.4 Binary Files” (included))
    - [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
    - [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
    - [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)(ch. 8 p 180-183 and ch. 14 p 326-333)
    - [All about py-file I/O](https://techvidvan.com/tutorials/python-file-read-write/)

# Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file 
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string 
- How to convert a JSON string to a Python data structure
# Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. 
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.
 
# Requirements

# General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

# Python Test Cases

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my\_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my\_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my\_module").my\_function.__doc__)' and python3 -c 'print(__import__("my\_module").MyClass.my\_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# Tasks

**0. Read file**

	Write a function that reads a text file (UTF8) and prints it to stdout:

	- Prototype: def read\_file(filename=""):
	- You must use the with statement
	- You don’t need to manage file permission or file doesn't exist exceptions.
	- You are not allowed to import any module

**1. Write to a file**

	Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

	- Prototype: def write\_file(filename="", text=""):
	- You must use the with statement
	- You don’t need to manage file permission exceptions.
	- Your function should create the file if doesn’t exist.
	- Your function should overwrite the content of the file if it already exists.
	- You are not allowed to import any module

**2. Append to a file**

	Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

	- Prototype: def append\_write(filename="", text=""):
	- If the file doesn’t exist, it should be created
	- You must use the with statement
	- You don’t need to manage file permission or file doesn't exist exceptions.
	- You are not allowed to import any module

**3. To JSON string**

	Write a function that returns the JSON representation of an object (string):
	
	- Prototype: def to\_json\_string(my\_obj):
	- You don’t need to manage exceptions if the object can’t be serialized.

**4. From JSON string to Object**

	Write a function that returns an object (Python data structure) represented by a JSON string:

	- Prototype: def from\_json\_string(my\_str):
	- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

**5. Save Object to a file **

	Write a function that writes an Object to a text file, using a JSON representation:

	- Prototype: def save_to_json_file(my_obj, filename):
	- You must use the with statement
	- You don’t need to manage exceptions if the object can’t be serialized.
	- You don’t need to manage file permission exceptions.

**6. Create object from a JSON file**

	Write a function that creates an Object from a “JSON file”:

	- Prototype: def load_from_json_file(filename):
	- You must use the with statement
	- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
	- You don’t need to manage file permissions / exceptions.

**7. Load, add, save**

	Write a script that adds all arguments to a Python list, and then save them to a file:
	
	- You must use your function save_to_json_file from 5-save_to_json_file.py
	- You must use your function load_from_json_file from 6-load_from_json_file.py
	- The list must be saved as a JSON representation in a file named add_item.json
	- If the file doesn’t exist, it should be created
	- You don’t need to manage file permissions / exceptions.

**8. Class to JSON**
	
	Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

	- Prototype: def class_to_json(obj):
	- obj is an instance of a Class
	- All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
	- You are not allowed to import any module

**9. Student to JSON**

	Write a class Student that defines a student by:
	
	- Public instance attributes:
		
		- first_name
		- last_name
		- age
	
	- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
	- Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
	- You are not allowed to import any module
