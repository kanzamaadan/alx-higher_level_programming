#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set()
    for i in range(len(my_list)):
        my_set.add(my_list[i])
    total = sum(my_set)
    return total
