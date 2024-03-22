#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Step 1: Extract Keys and Sort Them
    sorted_keys = sorted(a_dictionary.keys())

    # Step 2: Print Sorted Dictionary
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
