def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def min(l):
    min_value = l[0]
    for val in l:
        if val < min_value:
            min_value = val
    return min_value


def max(l):
    max_value = l[0]
    for val in l:
        if val > max_value:
            max_value = val
    return max_value


def avg(l):
    return sum(l) / len(l)


def stats(l):
    sum_values = sum(l)
    min_value = min(l)
    max_value = max(l)
    avg_value = avg(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    t = (max(l) - min(l)) / 10
    bin_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in l:
        if min(l) <= i < min(l) + t:
            bin_count[0] += 1
        elif min(l) + t <= i < min(l) + 2 * t:
            bin_count[1] += 1
        elif min(l) + 2 * t <= i < min(l) + 3 * t:
            bin_count[2] += 1
        elif min(l) + 3 * t <= i < min(l) + 4 * t:
            bin_count[3] += 1
        elif min(l) + 4 * t <= i < min(l) + 5 * t:
            bin_count[4] += 1
        elif min(l) + 5 * t <= i < min(l) + 6 * t:
            bin_count[5] += 1
        elif min(l) + 6 * t <= i < min(l) + 7 * t:
            bin_count[6] += 1
        elif min(l) + 7 * t <= i < min(l) + 8 * t:
            bin_count[7] += 1
        elif min(l) + 8 * t <= i < min(l) + 9 * t:
            bin_count[8] += 1
        elif min(l) + 9 * t <= i <= max(l):
            bin_count[9] += 1
    return bin_count


if __name__ == '__main__':
    l = [7, 0, 8, 5]
    assert sum(l) == 20
    assert min(l) == 0
    assert max(l) == 8
    assert avg(l) == 5
    assert min([6, 1, 2, 3, 4, 5]) == 1
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert histogram([0, 0.1, 0.3, 0.7, 1.5, 10]) == [4, 1, 0, 0, 0, 0, 0, 
        0, 0, 1]
    assert histogram([0, 0.1, 0.3, 0.7, 1.5, 1.8, 1.9, 2.0, 10]) == [4, 3, 
        1, 0, 0, 0, 0, 0, 0, 1]
    assert histogram([0, 1.5, 1.8, 1.9, 2.0, 3.0, 4.0, 5.0, 10]) == [1, 3, 
        1, 1, 1, 1, 0, 0, 0, 1]
