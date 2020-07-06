# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below
    m1 = 0
    m2 = 1
    while m1 <= limit:
        yield m1
        res = m1 + m2
        m1 = m2
        m2 = res

def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = [i for i in fib(limit)]
    return list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]