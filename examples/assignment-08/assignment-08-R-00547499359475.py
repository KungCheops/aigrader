from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    assert len(l) != 0, 'empty list'
    min_value = l[0]
    for val in l:
        if val <= min_value:
            min_value = val
    max_value = l[0]
    for val in l:
        if val >= max_value:
            max_value = val
    sum_values = sum(l)
    summation = 0
    size = len(l)
    for val in l:
        summation += val
    avg_value = summation / size
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    sumV, minv, maxv, avgv = stats(l)
    diff = maxv - minv
    dist = diff / 10
    bin_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in l:
        if minv <= i <= minv + dist:
            bin_count[0] = bin_count[0] + 1
        elif minv + dist <= i <= minv + 2 * dist:
            bin_count[1] = bin_count[1] + 1
        elif minv + 2 * dist <= i <= minv + 3 * dist:
            bin_count[2] = bin_count[2] + 1
        elif minv + 3 * dist <= i <= minv + 4 * dist:
            bin_count[3] = bin_count[3] + 1
        elif minv + 4 * dist <= i <= minv + 5 * dist:
            bin_count[4] = bin_count[4] + 1
        elif minv + 5 * dist <= i <= minv + 6 * dist:
            bin_count[5] = bin_count[5] + 1
        elif minv + 6 * dist <= i <= minv + 7 * dist:
            bin_count[6] = bin_count[6] + 1
        elif minv + 7 * dist <= i <= minv + 8 * dist:
            bin_count[7] = bin_count[7] + 1
        elif minv + 8 * dist <= i <= minv + 9 * dist:
            bin_count[8] = bin_count[8] + 1
        elif minv + 9 * dist <= i <= minv + 10 * dist:
            bin_count[9] = bin_count[9] + 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    print(stats(gdp))
    print(histogram(le))
