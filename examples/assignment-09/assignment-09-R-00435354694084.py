from GDPvsLE import *


def sortL(l):
    new_list = []
    while l:
        minimum = l[0]
        for x in l:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        l.remove(minimum)
    return new_list


def LenList(l):
    strlen = 0
    for c in l:
        strlen += 1
    return strlen


def quartiles(l):
    l = sortL(l)
    lenL = LenList(l)
    if lenL % 2 != 0:
        Q2 = float(l[lenL // 2])
        Q1 = float(l[int(lenL * 0.25)])
        Q3 = float(l[int(lenL * 0.75)])
    if lenL % 2 == 0:
        Q2 = float((l[round(lenL / 2) - 1] + l[round(lenL / 2)]) / 2)
        Q1 = float((l[int(lenL * 0.25)] + l[int(lenL * 0.25 - 1)]) / 2)
        Q3 = float((l[int(lenL * 0.75)] + l[int(lenL * 0.75 - 1)]) / 2)
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
