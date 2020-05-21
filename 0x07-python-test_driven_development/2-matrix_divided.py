#!/usr/bin/python3
"""matrix_divided"""


def matrix_divided(matrix, div):
    """Used for divide each element of a matrix

    Arguments:
        matrix {list [int, float]} -- the matrix to be divided
        div {[int]} -- divisor

    Raises:
        TypeError: "matrix must be a matrix (list of lists) of integers/floats"
        ZeroDivisionError: "division by zero"
        TypeError: "Each row of the matrix must have the same size")

    Returns:
        [list] -- New matrix divided
    """
    TypeErr = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(TypeErr)

    len_item = len(matrix[0])
    for item in matrix:
        if len(item) != len_item:
            raise TypeError("Each row of the matrix must have the same size")
        for inside in item:
            if not isinstance(inside, (int, float)):
                raise TypeError(TypeErr)
    for item in matrix:
        new_matrix.append(list(map(lambda i: round(i / div, 2), item)))
    return new_matrix
