#!/usr/bin/python3

def magic_calculation(a, b):
    """Calculates the magic"""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for i in range(4, 5):
            c = add(c, i)
            return (c)
    else:
        return (sub(a, b))
