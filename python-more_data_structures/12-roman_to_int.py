#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    numList = []
    dict = {'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500,
            'M': 1000}
    if not roman_string or isinstance(roman_string, str):
        for romanC in roman_string:
            for convertKey in dict:
                if romanC == convertKey:
                    numList.append(dict[convertKey])
        char = 0
        for i in numList:
            if (i > char):
                result -= char
            else:
                result += char
            char = i
        result += char
        return result
    return 0
