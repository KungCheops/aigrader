# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib (limit) :
    a,b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b
    return

def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = []
    gen = fib(limit)
    lists = [val for val in gen]
    return lists
        

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]