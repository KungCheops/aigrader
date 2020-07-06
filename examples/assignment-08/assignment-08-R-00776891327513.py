from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    min_value = l[0]
    max_value = l[0]
    avg_value = l[0]
    sum_values = 0
    for val in l:
        if val < min_value:
            min_value = val
        if val > max_value:
            max_value = val
        sum_values += val
    avg_value = sum_values / len(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    total = sum(l)
    for val in l:
        if val < 1.0:
            a += 1
        elif val < 2.0:
            b += 1
        elif val < 3.0:
            c += 1
        elif val < 4.0:
            d += 1
        elif val < 5.0:
            e += 1
        elif val < 6.0:
            f += 1
        elif val < 7.0:
            g += 1
        elif val < 8.0:
            h += 1
        elif val < 9.0:
            i += 1
        else:
            j += 1
    bin_count = [a, b, c, d, e, f, g, h, i, j]
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert stats(gdp)
    assert stats(le)


def histogram2(l):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    total = sum(l)
    for val in l:
        if val < total * 0.1:
            a += 1
        elif val < total * 0.2:
            b += 1
        elif val < total * 0.3:
            c += 1
        elif val < total * 0.4:
            d += 1
        elif val < total * 0.5:
            e += 1
        elif val < total * 0.6:
            f += 1
        elif val < total * 0.7:
            g += 1
        elif val < total * 0.8:
            h += 1
        elif val < total * 0.9:
            i += 1
        else:
            j += 1
    bin_count = [a, b, c, d, e, f, g, h, i, j]
    return bin_count
