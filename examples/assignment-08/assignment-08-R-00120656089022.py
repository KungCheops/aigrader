from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    sum_values = 0
    for val in l:
        sum_values += val
    min_value = l[0]
    for x in l:
        if x < min_value:
            min_value = x
    max_value = l[0]
    for x in l:
        if x > max_value:
            max_value = x
    count_n = 0
    for val in l:
        count_n += 1
    sum_n = 0
    for vals in l:
        sum_n += vals
    avg_value = sum_n / count_n
    return sum_values, min_value, max_value, avg_value


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
stats(gdp)
