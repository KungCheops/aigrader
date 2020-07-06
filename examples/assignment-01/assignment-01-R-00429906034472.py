# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib (limit) :
    first = 0
    second = 1
    while first<=limit:
        yield first
        if(second<=limit):
            yield second   
        first = first + second
        second = first + second
    return

def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = [ x for x in fib(limit)]
    return list

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]

