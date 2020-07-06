from GDPvsLE import *


def len_val(l):
    lenl = 0
    for i in l:
        lenl += 1
    return lenl


def min_val(l):
    min_value = l[0]
    for i in l:
        if i < min_value:
            min_value = i
    return min_value


def sortier(l):
    list = []
    while len_val(l) > 0:
        list.append(min_val(l))
        l.remove(min_val(l))
    return list


def quartiles(l):
    l = sortier(l)
    if len_val(l) % 2 == 1:
        Q2 = float(l[int((len_val(l) - 1) / 2)])
        l1 = l[:int((len_val(l) - 1) / 2) + 1]
        l2 = l[int((len_val(l) - 1) / 2):]
        Q1 = float(l1[int((len_val(l1) - 1) / 2)])
        Q3 = float(l2[int((len_val(l2) - 1) / 2)])
    else:
        Q2 = float((l[int(len_val(l) / 2)] + l[int(len_val(l) / 2 - 1)]) / 2)
        l1 = l[:int(len_val(l) / 2)]
        l2 = l[int(len_val(l) / 2):]
        Q1 = float((l1[int(len_val(l1) / 2)] + l1[int(len_val(l1) / 2 - 1)]
            ) / 2)
        Q3 = float((l2[int(len_val(l2) / 2)] + l2[int(len_val(l2) / 2 - 1)]
            ) / 2)
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
