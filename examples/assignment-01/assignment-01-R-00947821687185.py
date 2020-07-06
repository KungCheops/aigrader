# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a+b
        if b > limit:
            break
        yield b

def list_fib(limit) :
    # Construct a list of Fibonacci series
    return [i for i in fib(limit)]

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]

