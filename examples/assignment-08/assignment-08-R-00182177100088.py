def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def max(l):
    max_value = l[0]
    for val in l:
        if val > max_value:
            max_value = val
    return max_value


def min(l):
    min_value = l[0]
    for val in l:
        if val < min_value:
            min_value = val
    return min_value


def avg(l):
    return sum(l) / len(l)


def stats(l):
    sum_values = 0
    max_value = max(l)
    min_value = min(l)
    avg_value = sum(l) / len(l)
    for val in l:
        sum_values += val
        if val != max_value and val != min_value:
            print('continue reading')
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    bin_count = 0
    max_value = max(l)
    min_value = min(l)
    for val in l:
        if min_value < val < max_value and bin_count <= 10:
            bin_count += 1
            print(bin_count)
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
