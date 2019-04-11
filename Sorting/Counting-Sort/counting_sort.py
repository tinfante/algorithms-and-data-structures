#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter


def counting_sort(A, k):
    """
    Follows Cormen, et al. very closely. Only sorts in range(0,k) where k is
    a positive integer. It's also stable. Obviously, it won't be good for
    arrays that have big min-mix differences and a lot of missing values from
    that range.
    """
    C = [0] * (k + 1)
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    # C[i] now contains the number of elements equal to i.
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    # C[i] now contains the number of elements less than or equal to i.
    B = [None] * len(A)
    for j in reversed(range(len(A))):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B


def counting_sort_v2(A, min_, max_):
    """
    Avoids the second loop in solution above and can also handle
    negative numbers. Note though, that like in that loop, we are still
    iterating over all the range(min,max) (or range(len(C))), we actually
    avoided iterating over range(len(A)) twice. It's not stable. Values that
    go in S come from the C index (to which we substract min), not from A.
    """
    C = [0] * (max_ - min_ + 1)
    for x in A:
        C[x - min_] += 1
    S = []
    for n, c in enumerate(C, start=min_):
        S += [n] * c
    return S


def counting_sort_v3(A, min_, max_):
    """
    Maybe this can't be called Counting Sort anymore, since C becomes a
    dictionary instead of an array. But it does have the advantage of being
    able to sort arrays with huge gaps in them (e.g. [3, 1, 9000000, 2, 5])
    without creating an array for all the min-max range. One still has to
    iterate over all the range though, as well as over range(len(A)), which
    is the same as sum of the ranges at the end of the list comprehension,
    that is, sum(C.values()) == len(A).
    """
    C = Counter(A)
    S = [x for x in range(min_, max_+1) if x in C for _ in range(C[x])]
    return S


A = [2, 5, 3, 0, 2, 3, 0, 3]
print(counting_sort(A, max(A)))

N = [2, -2, 5, -1, 3, 0, -2, 2, 3, 0, 3]
print(counting_sort_v2(N, min(N), max(N)))
print(counting_sort_v3(N, min(N), max(N)))
