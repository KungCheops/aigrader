from __future__ import generators

def fib(limit):
    a, b = 0, 1
    for i in range(limit):
        yield a
        a, b = b, a + b

def list_fib(limit):
    list = []
    list = [ a for a in fib(limit) if a < limit]
    print(list)
    return list

if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
