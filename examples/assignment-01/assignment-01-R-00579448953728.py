# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below

    #Initial values
    a = 0 
    b = 1
    while True:
        yield a
        b = a + b
        a = b - a

        #Break Fibonacci series once it passes limit
        if(limit <  a):
            break
def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = []
    # Your code below
    it = fib(limit)
    for item in it:
         list.append(item)

    return list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    print(list_fib(20))
    #assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]

