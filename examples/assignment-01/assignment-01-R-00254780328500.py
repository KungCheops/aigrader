#!/usr/bin/python3

def fib(limit):
    a, b = 1, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

def list_fib(limit):
    return list(fib(limit))
