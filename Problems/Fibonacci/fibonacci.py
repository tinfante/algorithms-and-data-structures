def fib1(n):
    """
    Typical recursive solution. Causes maximum recursion depth exceeded error
    and is very slow for n > ~50.
    """
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)


def fib2(n, memo=None):
    """
    Recursive solution, but with manual memoization. Also causes recusion depth
    exceeded error but is much faster.
    """
    if memo is None:
        memo = {0: 0, 1: 1}
    if n not in memo:
        memo[n] = fib2(n-1, memo) + fib2(n-2, memo)
    return memo[n]


from functools import lru_cache
@lru_cache(maxsize=None)
def fib3(n):
    """
    Recursive solution with Python's builtin memoization decorator.
    """
    if n < 2:
        return n
    return fib3(n-1) + fib3(n-2)


def fib4(n):
    """
    Iterative solution, doesn't cause recursion limit exceeded error.
    """
    if n == 0:
        return 0
    last, next_ = 0, 1
    for _ in range(1, n):
        last, next_ = next_, last + next_
    return next_


def fib5(n):
    """
    Iterative solution with a generator. Returns the whole sequence, not
    just the nth element. Just iterate over fib5(n) or do list(fib5(n)).
    """
    yield 0
    if n > 0:
        yield 1
    last, next_ = 0, 1
    for _ in range(1, n):
        last, next_ = next_, last + next_
        yield next_
