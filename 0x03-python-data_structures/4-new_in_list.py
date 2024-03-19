#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Create a shallow copy of the original list
    copy = my_list[:]  # Create a shallow copy of the original list
    copy[idx] = element
    return copy
