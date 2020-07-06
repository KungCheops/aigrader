# Scaffold for solution to DIT873 / DAT346, Programming task 1

# Generator to be used by fib (limit) 
def sumFib(limit):
    minusTwo=0
    minusOne=1
    while minusTwo+minusOne<=limit:
        minusTwo, minusOne=minusOne, minusTwo+minusOne
    yield minusOne

# Generator to be used by list_fib(limit)
def sumFibList(limit):
    minusTwo=0
    minusOne=1
    yield minusTwo 
    yield minusOne
    while minusTwo+minusOne<=limit:
        minusTwo, minusOne=minusOne, minusTwo+minusOne
        yield minusOne

# Function fib(limit)
def fib (limit) :
    return next(sumFib(limit))

# Function list_fib(limit)
def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = []
    # Your code below
    for x in sumFibList(limit):
        list.append(x)
    return list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(10))
    print(list_fib(10))
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]

