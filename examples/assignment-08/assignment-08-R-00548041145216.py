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


def average(l):
    return sum(l) / len(l)


def stats(l):
    sum_values = sum(l)
    min_value = min(l)
    max_value = max(l)
    avg_value = average(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    interval_size = abs(max(l) - min(l)) / 10
    lower_bound = min(l)
    upper_bound = lower_bound + interval_size
    bin_count = []
    interval = 0
    while interval < 10:
        bin_count.append(0)
        for val in l:
            if val <= upper_bound and val >= lower_bound:
                bin_count[interval] += 1
            val += 1
        lower_bound = upper_bound
        upper_bound = lower_bound + interval_size
        interval += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert stats([-10, 0, 10]) == (0, -10, 10, 0)
    assert histogram([-10, 0.5, 10]) == [1, 0, 0, 0, 0, 1, 0, 0, 0, 1]
print('Statistics of gdp per capita : (sum, min, max, avg) \n', stats(gdp))
