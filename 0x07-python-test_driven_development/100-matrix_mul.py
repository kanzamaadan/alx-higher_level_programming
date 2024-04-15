#!/usr/bin/python3
"""module containing function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices

    Arguments:
        @m_a (list of lists): a list of lists of integers or floats
        @m_b (list of lists): a list of lists of integers or floats
    Raises:
        ValueError: if m_a or m_b is not a list
        ValueError: if m_a or m_b is not a list of lists
        TypeError: if m_a or m_b is empty (it means: = [] or = [[]])
        TypeError: if one element of those list of lists
        is not an integer or a float
        TypeError: if m_a or m_b is not a rectangle
        (all 'rows' should be of the same size)
        ValueError: If m_a and m_b can't be multiplied
        Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("{} must be a list".format
                        ("m_a" if not isinstance(m_a, list) else "m_b"))

    if len(m_a) == 0 or len(m_b) == 0 or m_a == [[]] or m_b == [[]]:
        raise ValueError("{} can't be empty".format
                         ("m_a" if len(m_a) == 0 else "m_b"))

    for eachrow in m_a:
        for n in eachrow:
            if not isinstance(n, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(eachrow) != len(m_a[0]):
            raise TypeError("each row of m_a must should be of the same size")
        if len(eachrow) != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")

    for eachrow in m_b:
        for n in eachrow:
            if not isinstance(n, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(eachrow) != len(m_b[0]):
            raise TypeError("each row of m_b must should be of the same size")

    x = []
    new1_matrix = []
    n = 0
    for rowA in range(len(m_a)):
        x = []
        for colB in range(len(m_b[0])):
            for a in range(len(m_a[0])):
                n += m_a[rowA][a] * m_b[a][colB]
            x.append(n)
            n = 0
        new1_matrix.append(x)

    return new1_matrix
