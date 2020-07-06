from GDPvsLE import GDPvsLE
import math


def sum(l):
    """ Return sum of elements in a list.

    :type l:  list
    :param l: list of values

    :rtype: float
    """
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    """ Returns statistics for list of values
    including min, max, average and sum of elements

    :type l:  list
    :param l: list of values

    :rtype: tuple
    """
    min_value = l[0]
    max_value = l[0]
    sum_values = 0
    for val in l:
        if val < min_value:
            min_value = val
        if val > max_value:
            max_value = val
        sum_values += val
    avg_value = sum_values / len(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    """ Computes a histogram given a Python list. 
    Split the range of possible values between largest and smallest
    value in the list into ten equal-sized intervals and count how 
    many values fall into each of the ten intervals.

    :type l: list
    :param l: list of values

    :rtype: list[int]
    """
    _, min_value, max_value, _ = stats(l)
    range_ = max_value - min_value
    r = range_ / 10
    count = lambda l, low, high: len([val for val in l if val > low and val <=
        high])
    low, high = min_value - 1, min_value + r
    bin_count = []
    for i in range(10):
        if i == 9:
            high = max_value
        bin_count.append(count(l, low, high))
        low = high
        high = low + r
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert histogram([1, 0.4, 0.1, 0]) == [2, 0, 0, 1, 0, 0, 0, 0, 0, 1]
print(histogram(GDPvsLE.gdp))
print(histogram(GDPvsLE.le))
print(stats(GDPvsLE.gdp))
