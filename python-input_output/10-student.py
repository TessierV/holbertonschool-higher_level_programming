#!/usr/bin/python3
"""Studient"""


class Student:
    """
    Write a class Student that defines a student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        list = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                for i in self.__dict__:
                    list[i] = self.__dict__[i]
                return list
