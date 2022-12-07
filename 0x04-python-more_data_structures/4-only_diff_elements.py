#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set3 = set_1.difference(set_2)
    set4 = set_2.difference(set_1)
    return set3 | set4
