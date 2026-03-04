

def fib_recursive(n:int) -> int:
    """Returns the Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_memo(n:int, cache:dict=None) -> int:
    """Returns the Fibonacci number using memoization."""
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n < 0:
        raise ValueError("n must be non-negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
        return cache[n]
    
def fib_iter(n:int) -> int:
    """Returns the Fibonacci number using iteration."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == '__main__':
    import time

    tests = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (10, 55),
        (20, 6765),
        (35, 9227465),
        (42, 267914296),
    ]

    def test_func(fib_func):
        """
        Tests the Fibonacci function against known values.
        """
        for n, expected in tests:
            start_time = time.perf_counter()
            result = fib_func(n)
            end_time = time.perf_counter()
            duration = end_time - start_time
            print(f"{fib_func.__name__}({n}) = {result} (expected {expected}), took {duration:.6f} seconds")
            assert result == expected


    test_func(fib_recursive)
    test_func(fib_memo)
    test_func(fib_iter)