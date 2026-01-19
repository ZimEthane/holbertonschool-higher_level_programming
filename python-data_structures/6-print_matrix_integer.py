#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for first_idx in matrix:
        for second_idx in matrix[first_idx]:
            if second_idx == matrix[first_idx][-1]:
                print("{:d}".format(second_idx), end="")
            else:
                print("{:d}".format(second_idx), end=" ")
        print("")
