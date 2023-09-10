#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
            new_string = ' '.join(str(elem) for elem in i)
            print("{}".format(new_string))
