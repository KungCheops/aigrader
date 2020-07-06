from GDPvsLE import *


def quartiles(l):
    n = len(l)
    l.sort()
    if n % 2 == 0:
        Q2 = (l[int(n / 2 - 1)] + l[int(n / 2)]) / 2
        h1 = l[:int(n / 2)]
        h2 = l[int(n / 2):]
    elif n % 2 != 0:
        Q2 = l[int((n - 1) / 2)]
        h1 = l[:int((n + 1) / 2)]
        h2 = l[int((n - 1) / 2):]
    n1 = len(h1)
    n2 = len(h2)
    if n1 % 2 == 0:
        Q1 = (h1[int(n1 / 2 - 1)] + h1[int(n1 / 2)]) / 2
    elif n1 % 2 != 0:
        Q1 = h1[int((n1 - 1) / 2)]
    if n2 % 2 == 0:
        Q3 = (h2[int(n2 / 2 - 1)] + h2[int(n2 / 2)]) / 2
    elif n2 % 2 != 0:
        Q3 = h2[int((n2 - 1) / 2)]
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 2, 3, 4, 5, 6, 7, 8]) == (2.5, 4.5, 6.5)
    assert quartiles([1, 2, 3, 4, 5, 6, 7]) == (2.5, 4, 5.5)
    assert quartiles([7, 3, 2, 4, 8, 6, 1, 5]) == (2.5, 4.5, 6.5)
    assert quartiles([4, 2, 3, 7, 5, 6, 1]) == (2.5, 4, 5.5)
