from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    l.sort()
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values, l[0], l[len(l) - 1], sum_values / len(l)


def histogram(l):
    minValue = min(l)
    maxValue = max(l)
    interval = (maxValue - minValue) / 10.0
    bin_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in l:
        if i == maxValue:
            bin_count[int(i // interval) - 1] += 1
        else:
            bin_count[int(i / interval)] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
