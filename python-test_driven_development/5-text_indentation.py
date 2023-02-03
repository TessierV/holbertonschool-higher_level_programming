#!/usr/bin/python3
""" print square"""


def text_indentation(text):
    """prints a text with 2 new lines char: [.,?:]"""
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    else:
        i = 0
        try:
            while text[i]:
                i += 1
                print(text[i], end="")
                if text[i] in ['.', '?', ':']:
                    print(text[i], end="\n"*2)
                    i += 1
                    while text[i] == " ":
                        i += 1
        except:
            pass
