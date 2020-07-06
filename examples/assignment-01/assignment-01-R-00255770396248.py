#!/usr/bin/env python3

def fib(limit) :
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b,a+b

def list_fib(limit):
    list = []
    for g in fib(limit):
        list.append(g)
    return list

if __name__ == "__main__":
    assert list_fib(20) == [0,1,1,2,3,5,8,13]
