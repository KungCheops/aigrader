# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib(limit):
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below
    fib_list = []
    for i in range(limit):
        if i <= 0:
            n = 0
            fib_list.append(n)
        elif i <= 2:
            n = 1
            fib_list.append(n)
        else:
            n = fib_list[i-1] + fib_list[i-2]
            fib_list.append(n)
        yield n
    return


def list_fib(limit):
    # Construct a list of Fibonacci series
    list = []
    # Your code below
    generator = fib(limit)
    element = next(generator)
    while element < limit:
        list.append(element)
        element = next(generator)

    return list


# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
