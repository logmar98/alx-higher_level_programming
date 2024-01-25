#!/usr/bin/python3
'''function that finds the hightest number.'''


def find_peak(list_of_integers):
    '''Finds a hightest number'''
    
    if list_of_integers is None or list_of_integers == []:
        return None
    sorted_list = sorted(list_of_integers)
    return sorted_list[-1]
