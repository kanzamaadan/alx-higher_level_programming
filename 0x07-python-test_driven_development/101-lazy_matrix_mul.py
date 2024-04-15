#!/usr/bin/python3
"""function that multiplies 2 matrices by using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices by using NumPy
    Args:
        @m_a: the 1st matrix to multiply
        @m_b: the 1st matrix to multiply
    Returns:
        Return the multiplication of two matrices
    """
    return (np.matmul(m_a, m_b))
