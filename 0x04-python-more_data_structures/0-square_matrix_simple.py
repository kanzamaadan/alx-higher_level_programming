#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    my_matrix = [
        [0 for _ in range(len(matrix[0]))]
        for _ in range(len(matrix))
    ]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Compute the square of each element
            square = matrix[i][j] * matrix[i][j]
            # Store the squared value in the new matrix
            my_matrix[i][j] = square

    return my_matrix
