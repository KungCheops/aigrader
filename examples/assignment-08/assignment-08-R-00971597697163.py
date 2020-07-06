from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def calc_min(l):
    min_value = l[0]
    for val in l:
        if min_value > val:
            min_value = val
    return min_value


def calc_max(l):
    max_value = l[0]
    for val in l:
        if max_value < val:
            max_value = val
    return max_value


def calc_avg(l):
    avg_value = sum(l) / len(l)
    return avg_value


def stats(l):
    if len(l) == 0:
        return
    sum_values = sum(l)
    min_value = calc_min(l)
    max_value = calc_max(l)
    avg_value = calc_avg(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    min_value = calc_min(l)
    max_value = calc_max(l)
    my_range = (max_value - min_value) / 10
    bin_count = [0] * 10
    for val in l:
        i = 0
        while (i < 10) & (val > min_value + (i + 1) * my_range):
            i += 1
        bin_count[i] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    print(stats(gdp))
    print(histogram(le))
