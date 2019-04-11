# Stack

Asd asd asd

## Python

The Stack class simulates a (fixed-size) array, but it uses a `list` (a
dynamic-size array in Python) that is forced to have a fixed size. Stack items
can also be of different and of any type and size. So the advantages of real
arrays (memory and lookup efficiency) are negated. It can be instanced by
providing the size for the array and optionally an iterable of initial values
(`list`, `tuple`, `str`, `set`, etc.). I intentionally did not inherit from the
`list` class, which already has the `.pop()` and `.append()` methods (the
[recommended way of implementing stacks](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks)),
as it felt wrong to overwrite them. Raising over- and underflow
errors is also only meant to be illustrative since IndexErrors would happen
anway.

##### References

* Cormen, et al., *Introduction to Algorithms*, Third Ed., MIT press, 2009, pp. 232-234.
* Sedgewick & Wayne, *Algorithms*, Fourth Ed., Addison-Wesley, 2011, pp. 120-171.
