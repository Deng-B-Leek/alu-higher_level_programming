#!/usr/bin/python3
"""Module for matrix_divided function.
Divides all elements of a matrix by a number.
Validates matrix structure and divisor type.
Returns a new matrix with values rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args: matrix and div.
    Returns: new matrix.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(e, (int, float))
                    for row in matrix for e in row)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(e / div, 2) for e in row] for row in matrix]
