# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions

    
    # NOTE: The assignment requires that only 2 variables are used in the code
    # This will make the code harder to read as no intermitten variables are used

    # Sanity check of the limit
    if not isinstance(limit, int) or limit < 0:
        raise Exception('Invalid argument')

    
    # The fibonacci series is calculated using the two previous values in the series
    fib_minus_2 = 0
    fib_minus_1 = 1

    
    # Lets handle the two special cases first since their update rule does not follow the general update rule
    yield fib_minus_2

    if limit < fib_minus_1:
        return  
    yield fib_minus_1


    # Produce the series by generating values up and including the limit, as the interval are closed
    while fib_minus_2 + fib_minus_1 <= limit:
        # Yield the current value
        yield fib_minus_2 + fib_minus_1
        # Update by moving the previous to the second previous and the current to the previous
        fib_minus_2, fib_minus_1 = fib_minus_1, fib_minus_2 + fib_minus_1

def list_fib(limit) :
    # Construct a list of Fibonacci series using list comprehension

    # Use list comprehension to get all values from the generator
    return [f for f in fib(limit)]


# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert list_fib(21) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
    assert list_fib(1) == [0, 1, 1]

