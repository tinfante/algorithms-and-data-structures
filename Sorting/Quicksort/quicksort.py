#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy
from random import randint


def _partition(lst, left, right, pivot):
    lst[right], lst[pivot] = lst[pivot], lst[right]
    new_pivot_pos = left
    for i in range(left, right):
        if lst[i] < lst[right]:
            lst[i], lst[new_pivot_pos] = lst[new_pivot_pos], lst[i]
            new_pivot_pos += 1
    lst[new_pivot_pos], lst[right] = lst[right], lst[new_pivot_pos]
    return new_pivot_pos


def _quicksort(lst, left, right):
    if left < right:
        pivot = randint(left, right)
        pivot = _partition(lst, left, right, pivot)
        _quicksort(lst, left, pivot)
        _quicksort(lst, pivot+1, right)


def quicksort(_list):
    lst = copy(_list)
    if len(lst) > 1:
        _quicksort(lst, 0, len(lst)-1)
    return lst
