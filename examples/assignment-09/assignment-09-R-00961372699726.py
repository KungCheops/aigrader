from GDPvsLE import *


def median(l):
    sortedList = sorted(l)
    mid = len(sortedList) // 2
    if len(sortedList) % 2 == 0:
        return (sortedList[mid - 1] + sortedList[mid]) / 2.0
    else:
        return sortedList[mid]


def quartiles(l):
    sortedList = sorted(l)
    mid = len(sortedList) // 2
    Q2 = median(sortedList)
    if len(sortedList) % 2 == 0:
        Q1 = median(sortedList[:mid])
        Q3 = median(sortedList[mid:])
    else:
        Q1 = median(sortedList[:mid + 1])
        Q3 = median(sortedList[mid:])
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 1, 2, 2, 3, 3, 4, 4]) == (1.5, 2.5, 3.5)
    assert quartiles([121, 22, 13, 4, 5]) == (5, 13, 22)
    assert quartiles([-111, -121, 22, 13, 4]) == (-111, 4, 13)
    assert quartiles([-121, 22, 15, 4, 5, 3000]) == (4, 10, 22)
