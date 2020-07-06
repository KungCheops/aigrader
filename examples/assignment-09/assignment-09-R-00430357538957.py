from GDPvsLE import *


def quartiles(l):
    l = sorted(l)
    halt_point = int(len(l) / 2)
    bottom_half = l[:halt_point]
    upper_half = l[halt_point:]
    if len(l) % 2 == 1:
        bottom_half.append(l[halt_point])
    Q1 = compute_median(bottom_half)
    Q2 = compute_median(l)
    Q3 = compute_median(upper_half)
    return Q1, Q2, Q3


def compute_median(l):
    if len(l) % 2 == 1:
        return l[int(len(l) / 2)]
    else:
        mid = int(len(l) / 2)
        return sum(l[mid - 1:mid + 1]) / 2


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 2, 3, 4, 5, 6, 7, 8]) == (2.5, 4.5, 6.5)
    print(quartiles(gdp))
