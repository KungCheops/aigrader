from GDPvsLE import *


def sum(l):
    sum_values = 0
    for val in l:
        sum_values += val
    return sum_values


def stats(l):
    avg_value = 0
    min_value = l[0]
    max_value = l[0]
    sum_values = sum(l)
    for number in l:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
        avg_value = sum_values / len(l)
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    bin_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    min1 = stats(l)[1]
    max1 = stats(l)[2]
    r = max1 - min1
    n = r / 10
    for i in l:
        if min1 <= i <= min1 + n:
            bin_count[0] += 1
        else:
            for x in range(1, 10):
                if min1 + x * n < i <= min1 + (x + 1) * n:
                    bin_count[x] += 1
                    break
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
print(stats(gdp))
print(stats(le))
print(histogram(gdp))
print(histogram(le))
