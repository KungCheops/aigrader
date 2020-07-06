from GDPvsLE import *


def quartiles(l):
    if len(l) < 4:
        print('It works only with a list that contains more than 3 elements')
    L = sorted(l)
    if len(L) % 2 == 0:
        Q2 = (L[int(len(L) / 2 - 1)] + L[int(len(L) / 2)]) / 2
        Q1 = (L[int(len(L) / 4 - 1)] + L[int(len(L) / 4)]) / 2
        Q3 = (L[int(3 * len(L) / 4 - 1)] + L[int(3 * len(L) / 4)]) / 2
    else:
        Q2 = L[int(len(L) / 2)]
        Q1 = L[int(len(L) / 4)]
        Q3 = L[int(3 * len(L) / 4)]
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 2, 3, 4, 5]) == (2, 3, 4)
    assert quartiles([2, 1, 5, 4, 3]) == (2, 3, 4)
    assert quartiles([1, 2, 3, 4]) == (1.5, 2.5, 3.5)
    quartiles(gdp)
    quartiles(le)
