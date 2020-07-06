def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    sum_values = 0
    min_value = float('inf')
    max_value = float('-inf')
    number = 0
    avg_value = 0
    for val in l:
        number += 1
        sum_values += val
        if val < min_value:
            min_value = val
        if val > max_value:
            max_value = val
        avg_value = sum_values / number
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    min_value = float('inf')
    max_value = float('-inf')
    range_value = 0
    bin_value = 0
    for val in l:
        if val < min_value:
            min_value = val
        if val > max_value:
            max_value = val
    range_value = max_value - min_value
    bin_value = range_value / 10
    bin_count = []
    for j in range(0, 10):
        bin_count.insert(j, 0)
    i = 0
    max_bin = 0
    min_bin = 0
    while i < 10:
        max_bin = min_value + (i + 1) * bin_value
        min_bin = min_value + i * bin_value
        for val in l:
            if val >= min_bin and val < max_bin:
                bin_count[i] += 1
            if i == 9:
                if val == 10:
                    bin_count[i] += 1
        i += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
