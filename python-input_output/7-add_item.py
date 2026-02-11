#!/usr/bin/python3
"""
This module contains a function that adds all arguments to a Python list,
and then save them to a file.
"""


import json
from sys import argv


def add_item(filename, *args):
    """
    Adds all arguments to a Python list, and then save them to a file.

    Args:
        filename (str): the name of the file where the list will be saved.
        *args: variable length argument list to be added to the list.

    """

    try:
        with open(filename, 'r', encoding="utf-8") as file:
            my_list = json.load(file)
    except FileNotFoundError:
        my_list = []

    my_list.extend(args)

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_list, file)
