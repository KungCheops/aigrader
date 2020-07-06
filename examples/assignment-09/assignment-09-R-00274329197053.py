from GDPvsLE import *


def split_half(l):
    n = len(l)
    half = int(n / 2)
    if n % 2 == 0:
        return l[:half], l[n - half:]
    else:
        return l[:half + 1], l[n - half - 1:]


def median(l):
    n = len(l)
    if len(l) % 2 == 0:
        return (l[int(n / 2) - 1] + l[int(n / 2)]) / 2
    else:
        return l[int(n / 2)]


def quartiles(l):
    l.sort()
    Q2 = float(median(l))
    split = split_half(l)
    Q1 = float(median(split[0]))
    Q3 = float(median(split[1]))
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 2, 3, 4, 5]) == (2.0, 3.0, 4.0)
    assert quartiles([1, 2, 3, 4, 5, 6]) == (2.0, 3.5, 5.0)
    assert quartiles([2, 1, 1]) == (1.0, 1.0, 1.5)
    print('Quartiles for GDP:', quartiles(gdp))
    print('Quartiles for LE:', quartiles(le))
