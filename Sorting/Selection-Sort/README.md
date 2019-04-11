# Selection Sort

| Worst case | Average case | Best case |
|:----------:|:------------:|:---------:|
| O(n<sup>2</sup>)      | O(n<sup>2</sup>)        | O(n<sup>2</sup>)

This algorithm is arguably one of the worst sorting algorithms since it has quadratic time complexity for the best, average and worst case scenarios. It's usually slower than Insertion Sort, but like this algorithm sorting is done in-place, so space complexity is O(n).

The sorting process is as follows. Iterate over all the array indexes. At each iteration step this index will divide the array into a sorted sub-array (empty at the first iteration) and an unsorted one (the whole array at first). Then, in the inner loop, find the minimum (or maximum) value in the unsorted sub-array and move it to the end of the sorted sub-array (or the beginning if finding the maximum value). When the algorithm terminates the sorted sub-array will contain all the elements of the original array, and the unsorted sub-array will be empty.

* Heineman, et al., *Algorithms in a nutshell*, First Ed., O'Reilly, 2009, pp. 91-92.
* Sedgewick & Wayne, *Algorithms*, Fourth Ed., Addison-Wesley, 2011, pp. 248-249.

## Python

### insertion_sort_min()

Iterates over the array's indexes from left to right and then iterates from this index to the end of the array to find the minimum value. It then moves that minimum value to the end of the sorted sub-array.

### insertion_sort_max()

Iterates over the array's indexes ```i``` in reverse order, from right to left, and then checks ```array[0:i+1]``` to find the maximum value, which is then moved to the beginning of the sorted sub-array (now on the right hand side). The inner loop is replaced by ```max(enumerate(array[0:i+1]))```, but even though the inner loop is gone, all the values in the unsorted sub-array still have to be checked.
