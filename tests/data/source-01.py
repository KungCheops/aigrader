

def fib (limit) :
    a = 0
    b = 1
    yield b
    while True:
        if a+b > limit:
            return
        yield a+b
        a,b = b,a
        b += a


def list_fib(limit) :
    list = []
    generator = fib(limit)
    list = [i for i in generator]
    return list


if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
