import GDPvsLE


def quartiles(l):
    Q2 = find_median(l)
    Q1 = find_median(l[:int(len(l) / 2) + len(l) % 2])
    Q3 = find_median(l[int(len(l) / 2):])
    return Q1, Q2, Q3


def find_median(l):
    if len(l) % 2 == 0:
        median = (l[int(len(l) / 2) - 1] + l[int(len(l) / 2)]) / 2.0
    else:
        median = l[int(len(l) / 2)]
    return median


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 1, 2, 2, 3, 3, 4, 4]) == (1.5, 2.5, 3.5)
    assert quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (3, 5, 7)
    assert quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (3, 5.5, 8)
    GDPvsLE.gdp.sort()
    print(quartiles(GDPvsLE.gdp))
    GDPvsLE.le.sort()
    print(quartiles(GDPvsLE.le))
