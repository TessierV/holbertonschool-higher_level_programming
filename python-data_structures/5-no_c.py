#!/usr/bin/python3
def no_c(my_string):
    new_list = ""
    for i in (my_string):
        if i != 'C' and i != 'c':
            new_list += i
    return new_list
