# Heap

Heaps are almost complete binary-trees. Like binary-trees they can be
stored as arrays. They must maintain a min or max heap property: child nodes
can't be larger than their parents in a max heap.

A heap stored as an array:
`[16, 14, 10, 8, 7, 9, 3, 2, 4, 1]`

Its representation as an (incomplete) binary-tree.
```
                      _______16_______
               _____14_____      _____10_____
          ____8____    ____7    9            3
         2         4  1
```

The index (1-based) of a node's left child, where *i* is the parent's
index, is `i * 2`. For the right child just add 1.

The height of the heap, where *n* is the number of nodes, is
`floor(log2(n))`.

The index of the last non-leaf node is `floor(n/2)`.

Heaps have many uses, e.g. sorting (Heap sort) and priority queues. For sorting
a max heap is usually prefered, while for priority queues min heaps are mainly
used.

"*Hence, we can build a max-heap from an unordered array in linear time.*",
Cormen, et al, p. 159.

## JavaScript

Max heap. `buildMaxHeap()` runs `maxHeapify()` on every non-leaf node
in reverse order. This reorders the array in such a way that the max heap
property is maintained. `maxHeapify()` is top-down (sinks).

## Python

See [Sorting/Heap-Sort/](https://github.com/tinfante/algorithms-and-data-structures/tree/master/Sorting/Heap-Sort).
Also a max heap that that does sinking. The only major
difference is the `heap_sort` function. All that does is iterate over every
index in reverse, swapping the first array element (guaranteed to be
the max value in the heap) for the last array element. It then decrements the
heap size by 1 and runs `max_heap` from the first array index, thus
maintaining the max heap property. It repeats this process for all remaining
array items, which results in an ascendingly-ordered array.

##### References

* Cormen, et al., *Introduction to Algorithms*, Third Ed., MIT press, 2009, pp. 151-159.
* Sedgewick & Wayne, *Algorithms*, Fourth Ed., Addison-Wesley, 2011, pp. 317-313.
