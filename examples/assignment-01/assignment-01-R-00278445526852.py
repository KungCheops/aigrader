# Scaffold for solution to DIT873 / DAT346, Programming task 1



def fib(limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below

    # Initialize.
    x, y = 0, 1

    # Create generator logic.
    while x <= limit:
        yield x
        x, y = y, x + y

def list_fib(limit) :
    # Construct a list of Fibonacci series.
    # Your code below
    gen = fib(limit)
    return list(gen)

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]

