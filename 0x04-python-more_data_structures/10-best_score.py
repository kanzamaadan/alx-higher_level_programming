#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    bst_key, bst_val = None, -float('inf')
    for key, value in a_dictionary.items():
        if value > bst_val:
            bst_val = value
            bst_key = key
    return bst_key
