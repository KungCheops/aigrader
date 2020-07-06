def fib (limit) :
    a = 0
    b = 1
    

    while (a <= limit):
        #Yield let us return a and then resume without starting over
        yield a
        old_a = a
        a = b
        b = old_a+b

#Construct a list of Fibonacci series
def list_fib(limit):
    return list(fib(limit))

if __name__ == "__main__":
    assert list_fib(21) == [0, 1, 1, 2, 3, 5, 8, 13, 21]

