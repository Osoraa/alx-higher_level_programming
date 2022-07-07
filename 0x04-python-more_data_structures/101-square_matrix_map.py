#!/usr/bin/python3
def square_matrix_map(matrix=[]) -> list:
    return list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
