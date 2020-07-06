from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    sum_values = 0
    for val in l:
        sum_values += val
    min_value = l[0]
    for min in l:
        if min < min_value:
            min_value = min
    max_value = l[0]
    for max in l:
        if max > max_value:
            max_value = max

    def leng(l):
        leng = 0
        for i in l:
            leng += 1
        return leng
    avg_value = sum(l) / leng(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    bin_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    minl = min(l)
    maxl = max(l)
    interval = (maxl - minl) / 10
    for i in l:
        if i == maxl:
            bin_count[int(i // interval) - 1] += 1
        else:
            bin_count[int(i / interval)] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
