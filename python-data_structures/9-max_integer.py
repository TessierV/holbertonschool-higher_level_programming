#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if len(my_list) != 0:
        for i in my_list:
            if i > max:
                max = i
        return max
    elif len(my_list) == 0:
        return None
