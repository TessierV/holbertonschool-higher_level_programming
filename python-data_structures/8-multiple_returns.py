#!/usr/bin/python3
def multiple_returns(sentence):
    mulreturn = ""
    if len(sentence) != "":
        mulreturn = len(sentence), sentence[0]
    else:
        mulreturn = 0, None
    return mulreturn