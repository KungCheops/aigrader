# Scaffold for solution to DIT873 / DAT346, Programming task 1
# Generator preserver the local variable even after exiting the "loop"   

def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below
    a, b = 0, 1
    while a < limit:
        yield a         #returns a, and keeps the value of a.
        a, b = b, a + b
        
def list_fib(limit) :
    # Construct a list of Fibonacci series
    # Your code below
    return list(fib(limit))  #Puts fib(limit)into a list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]

