#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_score, total_weight = float(0), float(0)
    for s, w in my_list:
        total_score += s * w
        total_weight += w
    return total_score/total_weight
