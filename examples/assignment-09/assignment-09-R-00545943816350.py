from GDPvsLE import *


def quartiles(l):
    n = len(l)
    l.sort()
    if n % 2 == 0:
        median1 = l[n // 2]
        median2 = l[n // 2 - 1]
        Q2 = (median1 + median2) / 2
        l1 = l[:n // 2]
        a = len(l1)
        m1 = l1[a // 2]
        m2 = l1[a // 2 - 1]
        Q1 = (m1 + m2) / 2
        l2 = l[n // 2:]
        b = len(l2)
        me1 = l2[b // 2]
        me2 = l2[b // 2 - 1]
        Q3 = (me1 + me2) / 2
    else:
        Q2 = l[n // 2]
        l1 = l[:n // 2 + 1]
        a = len(l1)
        Q1 = l1[a // 2]
        l2 = l[n // 2:]
        b = len(l2)
        Q3 = l2[b // 2]
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
print(quartiles(gdp))
print(quartiles(le))
print(quartiles([1, 1, 2, 2, 3, 3, 4, 4]))
