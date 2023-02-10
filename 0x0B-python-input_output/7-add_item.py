#!/usr/bin/python3
"""
Created on Friday 10.02.2023
@author: Rungene
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
file_name = 'add_item.json'

try:
    list_add = load_from_json_file(file_name)
except Exception:
    list_add = []

for i in range(1, len(args)):
    list_add.append(args[i])

try:
    save_to_json_file(list_add, file_name)
except Exception:
    pass
