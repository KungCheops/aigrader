
# Given an input limit, calculate the Fibonacci series within [0,limit]
# The first two numbers of the series are always equal to 1,
# and each consecutive number returned is the sum of the last two numbers.

def fib (limit) :
    # Using a generator expression, implement a function  fib(limit) which takes an integer
    # “limit” as an input and calculate the Fibonacci series, within this limit, by using
    # only two variables in the function.
    fib_list = [0,1]
    yield fib_list[0]
    yield fib_list[1] # there's probably a better way to return the beginning of the list

    while fib_list[-1] + fib_list[-2] <= limit:
        next =  (fib_list[-1] + fib_list[-2])
        yield next
        fib_list.append(next)

def list_fib(limit) :
    # returns a list for the calculated Fibonacci series
    fib_list = fib(limit)

    return(list(fib_list))

# The following is called if you execute the script from the commandline
# e.g. with python solution.py
if __name__ == "__main__":
    list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]