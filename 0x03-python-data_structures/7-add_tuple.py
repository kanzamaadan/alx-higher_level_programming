#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Concat tuple of 2 zeros to tuple_a, ensure it has at least 2 elements
    tuple_a += (0, 0)

    # Concat tuple of 2 zeros to tuple_b, ensure it has at least 2 elements
    tuple_b += (0, 0)

    # Return a tuple containing the sums of
    #corresponding elements of tuple_a and tuple_b
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
