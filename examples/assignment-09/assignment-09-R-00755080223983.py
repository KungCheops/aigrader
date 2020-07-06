from GDPvsLE import *
import math
bottom_half = []
top_half = []


def quartiles(l):
    n = len(l)
    l.sort()
    if n % 2 != 0:
        lim = math.floor(n / 2)
        Q2 = float(l[lim])
        for i in range(0, lim):
            bottom_half.append(l[i])
        Q1 = float(bottom_half[math.floor(len(bottom_half) / 2)])
        for i in range(lim, n):
            top_half.append(l[i])
        Q3 = float(top_half[math.floor(len(top_half) / 2)])
    else:
        lim = math.floor(n / 2)
        Q2 = float((l[lim - 1] + l[lim]) / 2)
        for i in range(0, lim):
            bottom_half.append(l[i])
        Q1 = float((bottom_half[math.floor(len(bottom_half) / 2)] +
            bottom_half[math.floor(len(bottom_half) / 2) - 1]) / 2)
        for i in range(lim + 1, n):
            top_half.append(l[i])
        Q3 = float((top_half[math.floor(len(top_half) / 2)] + top_half[math
            .floor(len(top_half) / 2) - 1]) / 2)
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
