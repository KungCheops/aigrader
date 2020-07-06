# Scaffold for solution to DIT873 / DAT346, Programming task 1

def fib(limit):
    """
    Given an input limit, calculate the Fibonacci series within [0,limit]
    The first two numbers of the series are always equal to 1,
    and each consecutive number returned is the sum of the last two numbers.
    You should use generators for implementing this function
    See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    """
    prev = 0
    curr = 1

    while prev <= limit:
        yield prev
        curr = prev + curr
        prev = curr - prev


def list_fib(limit):
    """
    Construct a list of Fibonacci series
    """
    list = []
    next = 1

    if limit >= 0:
        list.append(0)
    if limit >= 1:
        list.append(1)

    while next <= limit:
        list.append(next)
        next = list[-1] + list[-2]

    return list


if __name__ == "__main__":
    for num in fib(20):
        print(num)
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
