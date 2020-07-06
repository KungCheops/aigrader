from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    sum_values = sum(l)
    min_value = l[0]
    for i in l:
        if i < min_value:
            min_value = i
    max_value = l[0]
    for i in l:
        if i > max_value:
            max_value = i
    avg_value = sum_values / len(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    bin_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    bin = (stats(l)[2] - stats(l)[1]) / 10
    for i in l:
        if i >= stats(l)[1] and i < stats(l)[1] + bin:
            bin_count[0] += 1
        elif i >= stats(l)[1] + bin and i < stats(l)[1] + 2 * bin:
            bin_count[1] += 1
        elif i >= stats(l)[1] + 2 * bin and i < stats(l)[1] + 3 * bin:
            bin_count[2] += 1
        elif i >= stats(l)[1] + 3 * bin and i < stats(l)[1] + 4 * bin:
            bin_count[3] += 1
        elif i >= stats(l)[1] + 4 * bin and i < stats(l)[1] + 5 * bin:
            bin_count[4] += 1
        elif i >= stats(l)[1] + 5 * bin and i < stats(l)[1] + 6 * bin:
            bin_count[5] += 1
        elif i >= stats(l)[1] + 6 * bin and i < stats(l)[1] + 7 * bin:
            bin_count[6] += 1
        elif i >= stats(l)[1] + 7 * bin and i < stats(l)[1] + 8 * bin:
            bin_count[7] += 1
        elif i >= stats(l)[1] + 8 * bin and i < stats(l)[1] + 9 * bin:
            bin_count[8] += 1
        else:
            bin_count[9] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert histogram([0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == [1, 1, 1, 
        1, 1, 1, 1, 1, 1, 1]
    assert histogram([0, 1]) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert stats([0, 0]) == (0, 0, 0, 0)
    print(stats(gdp))
    print(histogram(gdp))
    print(stats(le))
    print(histogram(le))
