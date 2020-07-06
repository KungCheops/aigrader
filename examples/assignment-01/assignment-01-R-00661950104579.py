def fib (limit) :
    """
    Calculate the values of the Fibonacci series within [0,limit]
    Args:
        limit (int): Upper (inclusive) limit of the series.
    Returns:
        A generator of the series on the interval.
    """
    x, y = 0, 1
    while x <= limit:
        yield x
        x, y = y, x + y

def list_fib(limit) :
    """
    Construct a list of the Fibonacci series within [0,limit]
    Args:
        limit (int): Upper (inclusive) limit of the series.
    Returns:
        A list of the series on the interval.
    """
    return list(fib(limit))

if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]