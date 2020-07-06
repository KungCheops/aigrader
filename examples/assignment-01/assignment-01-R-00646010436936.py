# Scaffold for solution to DIT873 / DAT346, Programming task 1
def fib(limit):
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    i = 0
    j = 1
    yield i
    yield j
    while (i+j <= limit):
        i,j = j, i+j
        yield j
    return

def list_fib(limit):
    # a list of Fibonacci series
    list = []
    for i in fib(limit):
        list.append(i)
    return list


if __name__ == '__main__':
    list = list_fib(20)
    assert list == [0, 1, 1, 2, 3, 5, 8, 13]
    print(list)


