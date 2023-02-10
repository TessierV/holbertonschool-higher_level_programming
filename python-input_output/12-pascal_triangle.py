#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """Pascal triangle"""
    list = []
    if n <= 0:
        return list
    else:
        for i in range(1, len(list)):
            for j in range(1, len(list[i]) - 1):
                list[i][j] = list[i - 1][j - 1] + list[i - 1][j]
        return list
