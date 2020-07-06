from GDPvsLE import *


def findMiddle(list):
    midpoint = -1
    halfIndex = len(list) / 2
    hi = int(halfIndex)
    if len(list) % 2 == 0:
        midpoint = (list[int(halfIndex)] + list[int(halfIndex) + 1]) / 2
    else:
        midpoint = list[int(halfIndex)]
    return midpoint


def quartiles(list):
    list = sorted(list)
    Q2 = findMiddle(list)
    halfIndex = int(len(list) / 2) + 1
    if len(list) % 2 == 0:
        firstHalf = list[:halfIndex]
        Q1 = findMiddle(firstHalf)
        secondHalf = list[halfIndex + 1:]
        Q3 = findMiddle(secondHalf)
    else:
        Q1 = findMiddle(list[:halfIndex])
        Q3 = findMiddle(list[halfIndex:len(list) - 1])
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
