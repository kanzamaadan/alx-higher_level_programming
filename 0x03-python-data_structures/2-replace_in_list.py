#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # Check if the index is negative or out of range
    if idx < 0 or idx >= len(my_list):
        # Return the original list without modifying anything
        return my_list
    # If the index is valid, replace the element at the specified index
    my_list[idx] = element
    # Return the modified list
    return my_list
