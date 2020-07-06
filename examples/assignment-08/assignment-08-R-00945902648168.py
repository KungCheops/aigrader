from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    min_value = l[0]
    max_value = l[0]
    for i in l:
        if i < min_value:
            min_value = i
    for i in l:
        if i > max_value:
            max_value = i
    length_value = 0
    for i in l:
        length_value += 1
    sum_values = sum(l)
    avg_value = sum_values / length_value
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    bin_count = [0] * 10
    n = (max(l) - min(l)) / 10
    for j in range(10):
        for i in l:
            if i <= min(l) + (j + 1) * n and not i < min(l) + j * n:
                bin_count[j] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
