#!/usr/bin/
"""
module matrix_divided

"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div

    Args:
        matrix (list of lists of int/float): The matrix to be divided
        div (int/float): The divisor

    Returns:
        list of lists of float: A new matrix with the divided values

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
                   or if div is not a number
        ZeroDivisionError: If div is zero
        TypeError: If rows of the matrix are not the same size
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
