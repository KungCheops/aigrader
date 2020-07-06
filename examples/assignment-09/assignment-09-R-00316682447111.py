from GDPvsLE import *


def quartiles(l):
    sortdata = sorted(l)
    mid = len(sortdata) // 2
    if len(sortdata) % 2 == 0:
        Q2 = (sortdata[mid - 1] + sortdata[mid]) / 2
    else:
        Q2 = sortdata[mid]
    if len(sortdata) % 2 == 0:
        lowerQ = sortdata[:mid]
        upperQ = sortdata[mid:]
        midQ1 = len(lowerQ) // 2
        if len(lowerQ) % 2 == 0:
            Q1 = (lowerQ[midQ1 - 1] + lowerQ[midQ1]) / 2
        else:
            Q1 = lowerQ[midQ1]
        midQ3 = len(upperQ) // 2
        if len(upperQ) % 2 == 0:
            Q3 = (upperQ[midQ3 - 1] + upperQ[midQ3]) / 2
        else:
            Q3 = upperQ[midQ3]
    else:
        lowerQ = sortdata[:mid + 1]
        upperQ = sortdata[mid:]
        midQ1 = len(lowerQ) // 2
        if len(lowerQ) % 2 == 0:
            Q1 = (lowerQ[midQ1 - 1] + lowerQ[midQ1]) / 2
        else:
            Q1 = lowerQ[midQ1]
        midQ3 = len(upperQ) // 2
        if len(upperQ) % 2 == 0:
            Q3 = (upperQ[midQ3 - 1] + upperQ[midQ3]) / 2
        else:
            Q3 = upperQ[midQ3]
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
quartiles(gdp)
