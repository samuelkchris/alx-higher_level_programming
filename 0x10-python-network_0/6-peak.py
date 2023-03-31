#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    lst = list_of_integers
    beg = 0
    end = len(lst)-1

    if lst[beg] > lst[beg+1]:
        return lst[beg]
    if lst[end] > lst[end-1]:
        return lst[end]

    mid = (beg+end)//2
    if lst[mid-1] < lst[mid] and lst[mid+1] < lst[mid]:
        return lst[mid]
    if lst[mid] < lst[mid-1]:
        return find_peak(lst[beg:mid+1])
    elif lst[mid] < lst[mid+1]:
        return find_peak(lst[mid:end+1])
    else:
        return lst[beg]
    
