# Scaffold for solution to DIT873 / DAT346, Programming task 1
import timeit


def fib(limit):
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below
    num_1 = 0
    num_2 = 1
    fib_gen = yield num_1
    fib_gen = yield num_2
    while num_1 + num_2 <= limit:
        num_1, num_2 = num_2, num_1 + num_2
        fib_gen = yield num_2
    return fib_gen


def rec_fib(num_1, num_2, limit):
    if num_1 + num_2 <= limit:
        rec_fib(num_2, (num_1 + num_2), limit)
    return num_2


def list_fib(limit):
    # Construct a list of Fibonacci series
    list = [_ for _ in fib(limit)]
    return list


# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]

    # Code to test the time difference
    # between the generator's solution
    # and the recursive solution
    # limit = 100000000000000000000000000
    # start = timeit.default_timer()
    # list_fib(limit)
    # stop = timeit.default_timer()
    # print("Time with generator: " + str(stop - start))
    # start = timeit.default_timer()
    # rec_fib(0, 1, limit)
    # stop = timeit.default_timer()
    # print("Time with recursion: " + str(stop - start))


