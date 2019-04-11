# Merge Sort

| Worst case | Average case | Best case |
|:----------:|:------------:|:---------:|
| O(*n* log *n*)      | O(*n* log *n*)        | O(*n* log *n*)

Merge Sort is an efficient divide and conquer algorithm with two parts.

1. Split the original *n* length unsorted array into two *n*/2 length
sub-arrays, and recursively continue dividing the sub-arrays until recursion
bottoms-out. The condition for terminating the recursion is when we have
sub-arrays with only one element, in which case the sub-array is already
sorted.
2. Merge two sub-arrays by removing the smallest first element from either one
and adding it to a new array, repeating the process until one of the sub-arrays
is empty. We can then add all the remaining elements from the other non-empty
sub-array to the merged array, thus producing a longer sorted array out of the
shorter sub-arrays. Continue merging sub-arrays until we have only one array
with all the elements from the original input array, which will be sorted.

This sorting algorithm has the advantage of having an optimum time complexity,
O(*n* log *n*), for the average and worst case scenarios, and being relatively
easy to implement. The downside is that sorting isn't done in-place. New arrays
are created at each recursion step. Since it has auxiliary space requirements
it's not a good choice when there are space restrictions.

Here we can see a representation of the recursion tree and sub-arrays for the
array ```[5, 4, 3, 8, 7, 1, 6, 2]```. For simplicity's sake it's an even
2<sup>3</sup> length array.

```
                            [5,4,3,8,7,1,6,2]
                             /            \
                         [5,4,3,8]        [7,1,6,2]
                          /   \              /   \
                     [5,4]     [3,8]    [7,1]     [6,2]
                     /  \      /  \      /  \      /  \
                   [5]  [4]  [3]  [8]  [7]  [1]  [6]  [2]

```
The algorithm traverses this tree depth-first, at each node it creates a copy
of both halves of the current array and then first calls itself with the first
sub-array as argument, then with the second sub-array, and it finally merges
the results of both calls. When recursion bottoms out (sub-arrays have only one
element), it will start merging from the bottom-up.

```
                            [1,2,3,4,5,6,7,8]
                             /            \
                         [3,4,5,8]        [1,2,6,7]
                          /   \              /   \
                     [4,5]     [3,8]    [1,7]     [2,6]
                     /  \      /  \      /  \      /  \
                   [5]  [4]  [3]  [8]  [7]  [1]  [6]  [2]

```

##### References

* Cormen, et al., *Introduction to Algorithms*, Third Ed., MIT Press, 2009, pp.
30-37.
* Sedgewick & Wayne, *Algorithms*, Fourth Ed., Addison-Wesley, 2011, pp.
270-282.

## Python

There is not much to say here that isn't covered in the description above, and
the code is straightforward. It would be interesting to see how an iterative
solution behaves in Python. Not because of the recursion limit of 1000 --we can
see in the recursion trees above that the depth of a tree is log *n*, so we
could sort a 2<sup>1000</sup> length array-- but to see if it could be sped up.
Maybe .pop() and/or .extend() methods contribute quite a bit?

## Clojure

Pretty much the same as the Python implementation. The ```-merge``` function
uses ```recur```, which applies tail-call optimization. Not that it matters
much since ```merge-sort``` doesn't, and the stack limit is much larger in
Clojure than in Python anyway. But ```recur``` might contribute a bit to
this solution's speed.
