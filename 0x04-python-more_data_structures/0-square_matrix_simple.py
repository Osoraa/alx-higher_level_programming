#!/usr/bin/python3


def square_matrix_simple(matrix=[]) -> list[int]:
    return [[col * col for col in row] for row in matrix]


if __name__ == "__main__":
    square_matrix_simple()
