#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if i[-1] == j:
                print("{:d}".format(int(j)), end="")
            else:
                print("{:d}".format(int(j)), end=" ")
        print()
