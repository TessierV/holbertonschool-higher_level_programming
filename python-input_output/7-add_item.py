#!/usr/bin/python3
""" This sys import """
import sys


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
