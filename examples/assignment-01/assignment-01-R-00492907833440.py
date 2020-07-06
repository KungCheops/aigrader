# Scaffold for solution to DIT873 / DAT346, Programming task 1

def fib (limit):
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below
    f_0 = 0
    f_1 = 1
    if limit == 0:
        yield f_0
    elif limit > 0:
        yield f_0
        yield f_1
        while (f_0 + f_1) < limit:
            yield f_0 + f_1
            f_1 = f_0 + f_1
            f_0 = f_1 - f_0

def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = []

    # Create a generator for generating Fibonacci series
    gen = fib(limit)

    # Use the generator to create a list of Fibonacci numbers
    while True:
        try:
            list.append(next(gen))
        except:
            break
    return list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
