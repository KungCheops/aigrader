import GDPvsLE


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


def average(l):
    avg_values = sum(l) / len(l)
    return avg_values


def stats(l):
    sum_values = sum(l)
    min_value = min(l)
    max_value = max(l)
    avg_value = average(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    bin_num = 10
    minimum = min(l)
    value_range = max(l) - minimum
    step = float(value_range) / float(bin_num)
    bin_count = [0] * bin_num
    for val in l:
        try:
            bin_count[int((val - minimum) / step)] += 1
        except IndexError as e:
            bin_count[bin_num - 1] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert histogram([3, 15, 27, 26, 28, 30, 25, 4, 7, 12]) == [2, 1, 0, 1,
        1, 0, 0, 0, 3, 2]
    print('Stats about life expectancy: ' + str(stats(GDPvsLE.le)))
    print("Life expectancy's histogram: " + str(histogram(GDPvsLE.le)))
    print('Stats about GDP: ' + str(stats(GDPvsLE.gdp)))
    print('GDP histogram: ' + str(histogram(GDPvsLE.gdp)))
