#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_list = set(my_list)
    new_list = list(set_list)
    result = 0
    for i in new_list:
        result = result + i
    return result
