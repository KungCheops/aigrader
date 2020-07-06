# Solution to DIT873 / DAT346, Programming task 1

def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    n1 = 0
    n2 = 1
    yield n1
    while n2 <= limit:
        yield n2
        n1, n2 = n2, n1+n2

    yield 'end'



def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = []
    
    fib_gen = fib(limit)

    fib_n = next(fib_gen)
    while fib_n != 'end':
        list.append(fib_n)
        fib_n = next(fib_gen)

    return list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    # print(list_fib(20))
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]

