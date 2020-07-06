from GDPvsLE import gdp


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def min(l):
    if len(l) == 0:
        return 0
    m = l[0]
    for val in l:
        if val < m:
            m = val
    return m


def max(l):
    if len(l) == 0:
        return 0
    m = l[0]
    for val in l:
        if val > m:
            m = val
    return m


def avg(l):
    if len(l) == 0:
        return 0
    return sum(l) / len(l)


def stats(l):
    sum_values = sum(l)
    min_value = min(l)
    max_value = max(l)
    avg_value = sum_values / len(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    bin_count = [0] * 10
    n = 10
    xmin = min(l)
    xmax = max(l)
    w = (xmax - xmin) / n
    if w == 0:
        w = 1
    for val in l:
        bin = int((val - xmin) / w)
        if val == xmax:
            bin = n - 1
        bin_count[bin] += 1
    return bin_count


if __name__ == '__main__':
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    l = [5, 4, 2, 1, 4, 52, -3, 88]
    assert sum(l) == 153
    assert min(l) == -3
    assert max(l) == 88
    assert avg(l) == 19.125
    assert histogram([0, 0.1, 0.3, 0.7, 1.5, 10]) == [4, 1, 0, 0, 0, 0, 0, 
        0, 0, 1]
    assert histogram([0, 0.1, 0.3, 0.7, 1.5, 1.8, 1.9, 2.0, 10]) == [4, 3, 
        1, 0, 0, 0, 0, 0, 0, 1]
    assert histogram([0, 1.5, 1.8, 1.9, 2.0, 3.0, 4.0, 5.0, 10]) == [1, 3, 
        1, 1, 1, 1, 0, 0, 0, 1]
    print('stats: {0}'.format(stats(gdp)))
