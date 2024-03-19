#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # Start the loop from len(my_list) - 1 down to 0 (inclusive)
    for i in range(len(my_list) - 1, -1, -1):
        if not my_list:
            pass
        else:
            # Print the integer at index i of the list
            print("{}".format(my_list[i]))
