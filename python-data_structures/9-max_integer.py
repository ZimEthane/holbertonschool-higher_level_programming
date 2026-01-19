#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in my_list:
        if i == max(my_list):
            return i
    return None
