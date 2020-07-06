def quartiles(l):
    l.sort()
    if len(l) % 2 == 0:
        Q2 = (l[int(len(l) / 2) - 1] + l[int(len(l) / 2)]) / 2
        lower_half = l[0:int(len(l) / 2)]
    else:
        Q2 = l[int(len(l) / 2)]
        lower_half = l[0:int(len(l) / 2 + 1)]
    upper_half = l[int(len(l) / 2):]
    if len(lower_half) % 2 == 0:
        Q1 = (lower_half[int(len(lower_half) / 2) - 1] + lower_half[int(len
            (lower_half) / 2)]) / 2
    else:
        Q1 = lower_half[int(len(lower_half) / 2)]
    if len(upper_half) % 2 == 0:
        Q3 = (upper_half[int(len(upper_half) / 2) - 1] + upper_half[int(len
            (upper_half) / 2)]) / 2
    else:
        Q3 = upper_half[int(len(upper_half) / 2)]
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4, 5]) == (2.0, 2.5, 4.0)
    assert quartiles([1, 1, 2, 2, 3, 3, 4, 4]) == (1.5, 2.5, 3.5)
