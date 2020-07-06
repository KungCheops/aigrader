from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    if not l:
        return 0, 0, 0, 0
    sum_values = sum(l)
    min_value = l[0]
    max_value = l[0]
    for val in l:
        if val < min_value:
            min_value = val
        elif val > max_value:
            max_value = val
    avg_value = sum_values / len(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    min = stats(l)[1]
    dif = stats(l)[2] - min
    intervalsize = dif / 10
    bin_count = [0] * 10
    for val in l:
        i = 0
        for u in range(10):
            if val - min >= u * intervalsize and val - min < (u + 1
                ) * intervalsize:
                i = u
            elif val - min >= u * intervalsize and val - min <= (u + 1
                ) * intervalsize and u == 9:
                i = u
        bin_count[i] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
