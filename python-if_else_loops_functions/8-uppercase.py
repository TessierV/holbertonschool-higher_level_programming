#!/usr/bin/python3
def uppercase(str):
    for i in str:
        i = ord(i)
        if 97 <= i <= 122:
            i -= 32
        print("{}".format(chr(i)), end="")
    print(end='\n')
