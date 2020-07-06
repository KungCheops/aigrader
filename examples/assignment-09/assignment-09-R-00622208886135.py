from GDPvsLE import *
import math


def quartiles(l):
    l1 = []
    l2 = []
    Q1 = 0
    Q2 = 0
    Q3 = 0
    list_length = len(l)
    l.sort()
    if list_length % 2 != 0:
        S = list_length // 2
        Q2 = l[S]
        for i in range(0, S):
            l1.append(l[i])
        Q1 = l1[len(l1) / 2]
        for i in range(S, list_length):
            l2.append(l[i])
        Q3 = l2[len(l2) / 2]
    else:
        S = list_length / 2
        Q2 = (l[S - 1] + l[S]) / 2
        for i in range(0, S):
            l1.append(l[i])
        Q1 = (l1[len(l1) / 2] + l1[len(l1) / 2 - 1]) / 2
        for i in range(S + 1, list_length):
            l2.append(l[i])
        Q3 = (l2[len(l2) / 2] + l2[len(l2) / 2 - 1]) / 2
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles(gdp)
    print(quartiles([2, 3, 6, 2, 5, 5, 6, 7, 8, 9, 8, 5, 7]))
    print(quartiles(gdp))
