from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    if len(l) == 0:
        return 0, 0, 0
    sum_values = sum(l)
    min_value = l[0]
    max_value = l[0]
    avg_value = 0
    for val in l:
        avg_value += val
        if val < min_value:
            min_value = val
        if val > max_value:
            max_value = val
    avg_value /= len(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    bin_count = [0] * 10
    sum_values, min_value, max_value, avg_value = stats(l)
    val_range = max_value + 1 - min_value
    intervals = val_range / 10
    for val in l:
        bin_count[int((val - min_value) / intervals)] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
