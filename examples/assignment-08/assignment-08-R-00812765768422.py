from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    agg = 0
    n = len(l)
    max_value = None
    min_value = None
    for value in l:
        if not max_value or max_value < value:
            max_value = value
        if not min_value or min_value > value:
            min_value = value
        agg += value
    sum_values = agg
    avg_value = agg / n
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    bins = 10
    bin_count = [0] * bins
    sum_values, min_value, max_value, avg_value = stats(l)
    bin_range = max_value - min_value
    bin_size = bin_range / bins
    for value in l:
        bin_index = int((value - min_value) / bin_size)
        bin_index = min(bin_index, bins - 1)
        bin_count[bin_index] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert stats(range(-100, 1)) == (-5050, -100, 0, -50)
    assert stats(range(100, -1, -1)) == (5050, 0, 100, 50)
    assert stats(range(-5, 6)) == (0, -5, 5, 0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert histogram(range(-5, 5)) == [1] * 10
    assert histogram(range(-10, 10)) == [2] * 10
    assert histogram([-999, 55]) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert histogram([-1, 10]) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    print(stats(le))
    print(stats(gdp))
    print(histogram(le))
    print(histogram(gdp))
