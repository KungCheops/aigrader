def fib(limit):
    f_now, f_next = 0, 1
    while f_now <= limit:
        yield f_now
        f_now, f_next = f_next, f_now+f_next


def list_fib(limit):
    return [fib_i for fib_i in fib(limit)]


if __name__ == "__main__":
    assert list_fib(20) == [0, 1, 1, 2, 3, 5, 8, 13]
