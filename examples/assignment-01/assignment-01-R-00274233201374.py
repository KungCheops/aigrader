
def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below
    x0=0
    x1=1
    while x0<=limit:
        yield x0
        x0,x1=x1,x0+x1
    return     

def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = []
    # Your code below
    for i in fib(limit):
        list.append(i)
    return list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]


