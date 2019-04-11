#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy


def _merge(list1, list2):
    merged = []
    while list1 and list2:
        if list1[0] < list2[0]:
            merged.append(list1.pop(0))
        else:
            merged.append(list2.pop(0))
    # empty lists are considered falsy
    non_empty_list = list1 or list2
    merged.extend(non_empty_list)
    return merged


def merge_sort(_list):
    if len(_list) < 2:
        return copy(_list)
    middle = len(_list) // 2
    left = merge_sort(_list[:middle])
    right = merge_sort(_list[middle:])
    merged = _merge(left, right)
    return merged
