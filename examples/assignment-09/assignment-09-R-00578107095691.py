def sum(l):
    s = 0
    for val in l:
        s += val
    return s


def mean(l):
    il = len(l)
    if il == 0:
        return 0
    return sum(l) / il


def median(l):
    l.sort()
    il = len(l)
    if il == 0:
        return 0
    if il % 2 == 0:
        return mean(l[int(il / 2) - 1:int(il / 2) + 1])
    return l[int(il / 2)]


"""
Computes Q1, Q2 (the median), Q3 for a list
"""


def quartiles(l):
    l.sort()
    il = len(l)
    Q2 = median(l)
    c1 = il / 2
    c2 = il / 2
    if il % 2 != 0:
        c1 = (il - 1) / 2
        c2 = c1 + 1
    lo = l[:int(c1)]
    hi = l[int(c2):]
    if il % 2 != 0:
        lo.append(Q2)
        hi.append(Q2)
    Q1 = median(lo)
    Q3 = median(hi)
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 2, 3, 4]) == (1.5, 2.5, 3.5)
    assert quartiles([1, 2, 3, 4, 5]) == (2.0, 3.0, 4.0)
