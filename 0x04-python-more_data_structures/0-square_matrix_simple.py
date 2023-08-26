#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    squared_matrix = [[num**2 for num in row] for row in new_matrix]
    return squared_matrix
