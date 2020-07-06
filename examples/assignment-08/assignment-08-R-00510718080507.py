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
    min_value = 10000000
    for val in l:
        if val < min_value:
            min_value = val
    max_value = -10000000
    for val in l:
        if val > max_value:
            max_value = val
    length = 0
    for val in l:
        length += 1
    avg_value = sum_values / length
    return sum_values, min_value, max_value, avg_value


def histogram(l):
    l.sort()
    range = l[-1] - l[0]
    numberOfBins = 10
    stepper = int(round(range / numberOfBins))
    listOfGroups = []
    groupOne = l[0], l[0] + stepper
    listOfGroups.append(groupOne)
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        newGroup = listOfGroups[i][1], listOfGroups[i][1] + 1
        listOfGroups.append(newGroup)
    bin_count = []
    for group in listOfGroups:
        counter = 0
        for value in l:
            if value >= group[0] and value <= group[1]:
                counter = counter + 1
        bin_count.append(counter)
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
