#!/usr/bin/python3
def best_score(a_dictionary):
    return sorted(a_dictionary, key=a_dictionary.get, reverse=True)[0]
