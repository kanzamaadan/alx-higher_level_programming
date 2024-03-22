#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value  # Update the existing key-value pair
    else:
        a_dictionary[key] = value  # Add a new key-value pair
    return a_dictionary
