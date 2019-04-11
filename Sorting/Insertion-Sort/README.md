# Insertion Sort

| Worst case | Average case | Best case |
|:----------:|:------------:|:---------:|
| O(n<sup>2</sup>)      | O(n<sup>2</sup>)        | O(n)

This algorithm sorts an array by choosing an element from left to right, and then comparing that element with previous elements (from right to left). If the current element is less than the previous element, it is inserted before that previous element, and this process is repeated until we get to either a previous element that is less than the current one, or we reach the beginning of the array. We then choose the next current element (repeating the comparison with previous items) until we get to the end of the array, at which point the algorithm terminates and the array is sorted.

It's quite efficient for small arrays, so it can be used as a replacement in divide and conquer approaches when the subproblem is small enough. It's also good when the array is already sorted (achieving O(n) time complexity for this best case scenario) or partially sorted (when items' original positions are nearby their final position). The worst case scenario is when the array is reverse sorted, since the inner loop will always have to check all previous elements.

Moving elements is done in-place, so the space complexity is O(n). Shifting items larger than the current element to the right is frequently done one element at a time rather than in bulk.

##### References

* Cormen, et al., *Introduction to Algorithms*, Third Ed., MIT press, 2009, pp. 16-22.
* Heineman, et al., *Algorithms in a nutshell*, First Ed., O'Reilly, 2009, pp. 69-73.
* Sedgewick & Wayne, *Algorithms*, Fourth Ed., Addison-Wesley, 2011, pp. 250-252.

## Python

This implementation, rather than swapping the current and previous values one index at a time, first finds the correct index at which the current element has to be inserted, and only then inserts it. In this way, previous elements that are larger than the current element are moved to the right *en masse*.

## Clojure

This is a recursive implementation. Since Clojure has immutable data structures, the array can't be modified in-place. Instead, with each recursion, new modified arrays are created, so space complexity is not O(n). Additionally, shifting elements to the right is done one element at a time, so --barring language differences-- this is the inferior solution.
