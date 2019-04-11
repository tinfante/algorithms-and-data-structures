# -*- coding: utf-8 -*-

from copy import copy


def left(i):
    # alternatively: (i + 1 << 1) - 1
    return i * 2 + 1


def right(i):
    # alternatively: i + 1 << 1
    return i * 2 + 2


def max_heapify(a, heap_size, i):
    largest = i
    l = left(i)
    r = right(i)

    if l < heap_size and a[l] > a[i]:
        largest = l

    if r < heap_size and a[largest] < a[r]:
        largest = r

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)


def build_max_heap(a, heap_size):
    for i in range(heap_size-1, -1, -1):
        max_heapify(a, heap_size, i)


def heap_sort(array):
    a = copy(array)
    heap_size = len(a)
    build_max_heap(a, heap_size)
    for i in range(heap_size-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        max_heapify(a, i, 0)
    return a
