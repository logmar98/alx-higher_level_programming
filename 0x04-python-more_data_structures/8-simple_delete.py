#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == '':
        return 0
    del a_dictionary[key]
