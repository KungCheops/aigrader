from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    if len(l) == 0:
        return None
    sum_values = 0
    for val in l:
        sum_values += val
    min_value = l[0]
    max_value = l[0]
    for val in l:
        if val < min_value:
            min_value = val
        if val > max_value:
            max_value = val
    avg_value = sum_values / len(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    if len(l) <= 1:
        return None
    min_value = l[0]
    max_value = l[0]
    for val in l:
        if val < min_value:
            min_value = val
        if val > max_value:
            max_value = val
    interval = (max_value - min_value) / 10
    bin_count = [0] * 10
    for val in l:
        for i in range(0, 10):
            if val <= min_value + (i + 1) * interval:
                bin_count[i] += 1
                break
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert stats([]) is None
    assert stats([1]) == (1, 1, 1, 1)
    assert histogram([]) is None
    assert histogram([0]) is None
    assert histogram([0, 100]) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    print('Stats for GDP:', stats(gdp))
    print('Histogram for GDP:', histogram(gdp))
