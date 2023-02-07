#!/usr/bin/python3
""" This json import """
import sys

"""
Write a script that adds all arguments
to a Python list, and then save them to a file:
"""

file = '6-load_from_json_file.py'
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('file').load_from_json_file


try:
    for i in sys.argv[1:]:
        list.append(i)
    list = load("add_item.json")
except Exception:
    list = []

save(list, "add_item.json")
