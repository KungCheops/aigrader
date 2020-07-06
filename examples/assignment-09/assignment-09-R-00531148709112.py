def quartiles(l):
    value = []
    list = []
    i = 0
    Q1 = 0.0
    Q2 = 0.0
    Q3 = 0.0
    while i < len(l):
        for val in l:
            value.insert(i, val)
            i += 1
    value = sorted(value)
    if len(l) % 2 == 1:
        Q2 = value[len(l) // 2]
        Q1 = value[len(l) // 2 // 2]
        Q3 = value[len(l) // 2 + len(l) // 2 // 2]
    elif len(l) % 4 == 2:
        Q2 = (value[len(l) // 2 - 1] + value[len(l) // 2]) / 2
        Q1 = value[(len(l) // 2 - 1) // 2]
        Q3 = value[len(l) // 2 + len(l) // 2 // 2]
    else:
        Q1 = (value[len(l) // 2 // 2] + value[len(l) // 2 // 2 - 1]) / 2
        Q3 = (value[len(l) // 2 + len(l) // 2 // 2 - 1] + value[len(l) // 2 +
            len(l) // 2 // 2]) / 2
        Q2 = (Q1 + Q3) / 2
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
