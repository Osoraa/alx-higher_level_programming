#!/usr/bin/python3
"""The matrix multiplication module.

Simple Use:

    >>> func = __import__("1 00-matrix_mul").matrix_mul

    >>> print(func([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    [[7, 10], [15, 22]]

"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a: First matrix of type list of lists.
        m_b: Second matrix of type list of lists.

    Returns:
        Result of matrix multipliction.

    """

    # Error strings
    not_list_err = "{} must be a list"
    not_l_list_err = "{} must be a list of lists"
    empty_err = "{} can't be empty"
    int_float_err = "{} should contain only integers or floats"
    not_rect_err = "each row of {} must be of the same size"

    m_dict = {"m_a": m_a, "m_b": m_b}  # for easy iteration

    # Chec if inputs meet criteria
    for key, value in m_dict.items():
        if not isinstance(value, list):
            raise TypeError(not_list_err.format(key))

        if not value:
            raise ValueError(empty_err.format(key))

        if not all(isinstance(row, list) for row in value):
            raise TypeError(not_l_list_err.format(key))

        row_len = len(value[0])

        for row in value:
            if row_len != len(row):
                raise TypeError(not_rect_err.format(key))

            if not row:
                raise ValueError(empty_err.format(key))

            if not all(type(col) in (int, float) for col in row):
                raise TypeError(int_float_err.format(key))

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Transpose matrix m_b
    m_b = [[row[i] for row in m_b] for i in range(len(m_b[0]))]

    # Multiply matrices and return result
    return [[sum(i * j for i, j in zip(r, c)) for c in m_b] for r in m_a]


if __name__ == "__main__":
    m_a = [
        [1, 2.2, 3.3, 4],
        [5, 6, 7, 8.8],
    ]
    m_b = [[1.1, 2, 3.3], [4.0, 5.5, 6], [7, 8, 9], [10.01, 11, 12.3]]
    print(matrix_mul(m_a, m_b))
