from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    sum_values = 0
    min_value = l[0]
    max_value = l[0]
    counter = 0
    for x in l:
        sum_values += x
        if x < min_value:
            min_value = x
        if x > max_value:
            max_value = x
        counter += 1
        avg_value = sum_values / counter
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    min_value = l[0]
    max_value = l[0]
    for x in l:
        if x < min_value:
            min_value = x
        if x > max_value:
            max_value = x
    total_range = max_value - min_value
    bin_size = total_range / 10
    bins = [None] * 10
    for i in range(10):
        bins[i] = min_value + (i + 1) * bin_size
    bin_count = [0] * 10
    for x in l:
        bin = 0
        while x > bins[bin]:
            bin += 1
        bin_count[bin] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
