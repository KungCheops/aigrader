from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def min(l):
    min_value = l[0]
    for i in l:
        if i < min_value:
            min_value = i
    return min_value


def max(l):
    max_value = l[0]
    for i in l:
        if i > max_value:
            max_value = i
    return max_value


def avg(l):
    avg_value = sum(l) / len(l)
    return avg_value


def stats(l):
    min_value = min(l)
    max_value = max(l)
    sum_values = sum(l)
    avg_value = avg(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    interval = 0
    interval = (max(l) - min(l)) / 10
    low = min(l)
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
    c10 = 0
    for i in l:
        if low <= i < low + interval:
            c1 += 1
        elif low + interval <= i < low + 2 * interval:
            c2 += 1
        elif low + 2 * interval <= i < low + 3 * interval:
            c3 += 1
        elif low + 3 * interval <= i < low + 4 * interval:
            c4 += 1
        elif low + 4 * interval <= i < low + 5 * interval:
            c5 += 1
        elif low + 5 * interval <= i < low + 6 * interval:
            c6 += 1
        elif low + 6 * interval <= i < low + 7 * interval:
            c7 += 1
        elif low + 7 * interval <= i < low + 8 * interval:
            c8 += 1
        elif low + 8 * interval <= i < low + 9 * interval:
            c9 += 1
        else:
            c10 += 1
    bin_count = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert stats(gdp)
