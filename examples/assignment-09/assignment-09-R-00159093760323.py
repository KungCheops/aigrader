from GDPvsLE import *


def quartiles(l):
    l.sort()
    Q1 = median(l)
    l1 = []
    l2 = []
    if len(l) % 2 == 0:
        for i in range(0, int(len(l) / 2)):
            l1.append(l[i])
        for i in range(int(len(l) / 2), len(l)):
            l2.append(l[i])
    else:
        for i in range(0, int(len(l) / 2) + 1):
            l1.append(l[i])
        for i in range(int(len(l) / 2), len(l)):
            l2.append(l[i])
    Q2 = median(l1)
    Q3 = median(l2)
    return Q1, Q2, Q3


def median(l):
    if len(l) % 2 == 1:
        return l[int(len(l) / 2)]
    else:
        a = int(len(l) / 2)
        return (l[a] + l[a - 1]) / 2


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
