#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for index, col in enumerate(row):
                print("{:d}".format(col), end=" "
                      if index != len(row) - 1 else "\n")


if __name__ == "__main__":
    print_matrix_integer()
