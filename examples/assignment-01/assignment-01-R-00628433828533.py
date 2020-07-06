# Scaffold for solution to DIT873 / DAT346, Programming task 1

def fib(limit):
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below
    a = 0
    b = 1
    while a <= limit:
        yield a
        print(a)
        a, b = b, a + b

    return


def list_fib(limit):
    # Changed 2 lines from the code shell. Simplified it :)
    return list(fib(limit))


if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
