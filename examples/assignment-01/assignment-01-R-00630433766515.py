# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below
    a,b = 0,1
    yield a
    yield b
    while a+b <= limit:
        a,b = b,a+b
        yield b
    

def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = []
    # Your code below
    seq = fib(limit)
    for x in seq:
        list.append(x)
    return list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
    # Print sequence
    # print(list_fib(20))
