def fib(limit):
    elem1 = 0
    elem2 = 1
    while elem1 <= limit:
        yield elem1
        print(elem1)
        elem1, elem2 = elem2, elem1 + elem2
    return

def list_fib(limit):
    print(list(fib(limit)))
    return list(fib(limit))

if __name__ == "__main__":
    assert (list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]),"Violates Fibonacci series"