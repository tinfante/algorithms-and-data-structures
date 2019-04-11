#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy


def selection_sort_min(_list):
    slist = copy(_list)
    for i in range(len(slist)):
        min_index = i
        for j in range(i+1, len(slist)):
            if slist[j] < slist[min_index]:
                min_index = j
        slist.insert(i, slist.pop(min_index))
    return slist


def selection_sort_max(_list):
    slist = copy(_list)
    for i in reversed(range(len(slist))):
        max_index = i
        for j in range(0, i):
            if slist[j] > slist[max_index]:
                max_index = j
        slist[i], slist[max_index] = slist[max_index], slist[i]
    return slist
