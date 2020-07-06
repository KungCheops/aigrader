# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below
    first = 0
    second = 1

    # In the assert statement there was a 0 in the start.
    # Uncomment the below if-statement for this functionality.
    # I think it should start with 1 though (as described in the
    # assignment). That is how it works without this if-statement.
    #if first == 0:
    #    yield first

    while second <= limit:
        first_ = first
        first = second
        yield second
        second = second + first_

def list_fib(limit) :
    # Construct a list of Fibonacci series
    #list = []
    # Your code below
    fn = fib(limit)
    list = [number for number in fn]
   # for number in fn:
   #     list.append(number)
    return list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    #assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert list_fib(20) == [1, 1, 2, 3, 5, 8, 13]
    #print(list_fib(20))


