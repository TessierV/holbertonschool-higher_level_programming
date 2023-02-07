#!/usr/bin/python3
"""" Function """


def write_file(filename="", text=""):
    """
    Write a function that writes a string to a text file (UTF8)
    and returns the number of characters written:
    """
    with open(filename, encoding="utf-8") as my_file:
        data = my_file.read()
        return len(data)
