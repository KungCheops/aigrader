from typing import List
from GDPvsLE import *


def sum(list):
    sum_values = 0
    for val in list:
        sum_values += val
    return sum_values


def min_val(list):
    low_value = list[0]
    for val in range(len(list)):
        if list[val] < low_value:
            low_value = list[val]
    return low_value


def maximum(list):
    max = list[0]
    for val in range(len(list)):
        if list[val] > max:
            max = list[val]
    return max


""" a function which takes a Python list as an input argument and returns a tuple of sum, 
minimal value, maximal value, and average."""


def stats(list):
    sum_values = sum(list)
    min_value = min_val(list)
    max_value = maximum(list)
    avg_value = sum_values / len(list)
    return sum_values, min_value, max_value, avg_value


def histogram(list):
    numBins = 10
    binWidth = int((maximum(list) - min_val(list)) / numBins)
    bin_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(list)):
        if list[i] == maximum(list):
            bin_count[9] += 1
        else:
            bin_count[int(binWidth * list[i])] += 1
    return bin_count


if __name__ == '__main__':
    assert sum([1, 2, 3, 4, 5]) == 15
    assert sum([0, -1]) == -1
    assert stats([1, 2, 3, 4, 5]) == (15, 1, 5, 3.0)
    assert stats([0, -2, 6, 11]) == (15, -2, 11, 3.75)
    assert histogram([0, 0.1, 0.3, 1.5, 10]) == [3, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    assert histogram([0, 9, 10]) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 2]
