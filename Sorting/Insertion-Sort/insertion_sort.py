#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import copy


def insertion_sort(_list):
    slist = copy(_list)
    for i in range(1, len(slist)):
        for j in reversed(range(0, i)):
            if slist[i] > slist[j]:
                slist.insert(j+1, slist.pop(i))
                break
        else:
        # when for-j loop ends without a break: all s[j] values are larger
        # than or equal to s[i], so s[i] must go at the start of the list.
            slist.insert(0, slist.pop(i))
    return slist
