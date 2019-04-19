# Priority Queue

Priority queues can be implemented several ways, using different underlying
data structures. Using arrays (and linked lists) there are two alternatives:
keeping a sorted array and inserting a new item in its correct position,
or searching for the maximum value when dequeuing an item. Either the
insert or remove operation might take N. Using a heap data stucture, both
operations are guaranteed to be fast. 

| Data Structure  | Insert max   | Remove max |
|:---------------:|:------------:|:----------:|
| Ordered array   | N            | 1          |
| Unordered array | 1            | N          |
| Heap            | log *n*      | log *n*    |

## JavaScript

A lazy (search for max when dequeuing) unordered array implementation.

##### References

* Cormen, et al., *Introduction to Algorithms*, Third Ed., MIT press, 2009, pp. 162-165.
* Sedgewick & Wayne, *Algorithms*, Fourth Ed., Addison-Wesley, 2011, pp. 308-322.
* McMillan, *Data Structures and Algorithms with JavaScript*, First Ed., O'Reilly, 2014, pp. 70-72.
