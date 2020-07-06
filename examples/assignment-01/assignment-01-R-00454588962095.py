
def fib (limit) :
    n1 = 0
    n2 = 1
    while n1 < limit:
        yield a
        n1, n2 = n2, n1+n2

def list_fib(limit) :
    return [x for x in fib(limit)]

if __name__ == "__main__":
    fiblist = list_fib(20)
    print(f'Fibonacci sequence: {list_fib(20)}')
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]