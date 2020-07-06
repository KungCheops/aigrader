# Scaffold for solution to DIT873 / DAT346, Programming task 1


def fib (limit) :
    # Given an input limit, calculate the Fibonacci series within [0,limit]
    # The first two numbers of the series are always equal to 1,
    # and each consecutive number returned is the sum of the last two numbers.
    # You should use generators for implementing this function
    # See https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
    # Your code below

    # First n

    a, b, counter = 0, 1, 0

    while True:
        if (counter > limit): break
        yield a
        a, b = b, a + b
        counter += 1

#f = fib(7)
#for x in f:
#    print(x)
#print(type(f))

def list_fib(limit) :
    # Construct a list of Fibonacci series
    list = []
    # Your code below

    # Here I wrote two alternative ways:

    # Alternative 1
    return [i for i in fib(limit) if i < limit]

    # Alternative 2
#    a, b = 0, 1

#    if limit == 0 or limit == 1:
#        print(limit)
#    else:
#        list.append(a)
#        list.append(b)
#        temp = 0
#        while temp < limit:
#            temp = a + b
#            if (temp > limit): break
#            list.append(temp)
#            a = b
#            b = temp
#    return list

#f = list_fib(20)
#for x in f:
#    print(x)
#print(type(f))


# The following is called if you execute the script from the commandline
# e.g. with python solution.py

if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]

