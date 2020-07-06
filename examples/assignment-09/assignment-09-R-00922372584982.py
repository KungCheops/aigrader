from GDPvsLE import *
from math import *


def median(l):
    if len(l) % 2 != 0:
        index_Q2 = floor(len(l) / 2)
        Q2 = l[index_Q2]
    else:
        index_Q2 = int(len(l) / 2) - 1
        Q2 = (l[index_Q2] + l[index_Q2 + 1]) / 2
    return index_Q2, Q2


def quartiles(l):
    if len(l) == 0:
        return 0
    l.sort()
    index_Q2, Q2 = median(l)
    bottom_half = []
    top_half = []
    i = 0
    while i < len(l):
        if i < index_Q2 or i == index_Q2 and len(l) % 2 == 0:
            bottom_half.append(l[i])
        elif i == index_Q2 and len(l) % 2 != 0:
            bottom_half.append(l[i])
            top_half.append(l[i])
        else:
            top_half.append(l[i])
        i += 1
    Q1 = median(bottom_half)[1]
    Q3 = median(top_half)[1]
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 2, 3, 4]) == (1.5, 2.5, 3.5)
    assert quartiles([1, 2, 3, 4, 5]) == (2, 3, 4)
    assert quartiles([1, 2, 3, 4, 5, 6]) == (2, 3.5, 5)
    assert quartiles([-3, -2, -1, 2]) == (-2.5, -1.5, 0.5)
    assert quartiles([]) == 0
    assert quartiles([1]) == (1, 1, 1)
    assert quartiles([1, 2]) == (1, 1.5, 2)
print('Q1, median, Q3) : \n', quartiles(gdp))
