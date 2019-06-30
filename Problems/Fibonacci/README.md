# Fibonacci

Different solutions for the Fibonacci sequence. Note that the simple recursive
solutions decrease n to 0, while the iterative and tail-recursive solutions
increase 0 to n.


## Python

Five different solutions. The first one is the basic recursive solution. The
second and third add memoization to that solution. The fourth is an iterative
solution, so it doesn't cause stack overflows. The fifth and last one just
makes the iterative solution into a generator so that the whole sequence can be
returned.

## Clojure

Here, to avoid stack overflows, instead of transforming recursion to a loop,
tail recursion is used.
