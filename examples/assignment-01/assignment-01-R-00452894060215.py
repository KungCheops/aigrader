def fib (limit) :
    n1 = 0
    n2 = 1
    while n1 < limit:
        yield n1
        n1, n2 = n2, n1+n2

def list_fib(limit) :
    a = list(fib(limit))
    return a

if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
