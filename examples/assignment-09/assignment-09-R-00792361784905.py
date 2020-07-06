def quartiles(l):
    l.sort()
    Q1 = 0
    Q2 = 0
    Q3 = 0
    if len(l) % 2 != 0:
        a = int(len(l) / 2)
        Q2 = l[a]
    elif len(l) % 2 == 0:
        b = int(len(l) / 2 - 1)
        c = int(len(l) / 2)
        Q2 = (l[b] + l[c]) / 2
    if len(l) % 2 == 0 and len(l) / 2 % 2 != 0:
        d = int(len(l) / 2 / 2)
        Q1 = l[d]
        e = int(len(l) / 2 / 2 + len(l) / 2)
        Q3 = l[e]
    elif len(l) % 2 == 0 and len(l) / 2 % 2 == 0:
        f = int(len(l) / 2 / 2 - 1)
        g = int(len(l) / 2 / 2)
        Q1 = (l[f] + l[g]) / 2
        h = int(len(l) / 2 / 2 - 1 + len(l) / 2)
        i = int(len(l) / 2 / 2 + len(l) / 2)
        Q3 = (l[h] + l[i]) / 2
    elif len(l) % 2 != 0 and (len(l) + 1) / 2 % 2 != 0:
        j = int((len(l) + 1) / 2 / 2)
        Q1 = l[j]
        k = int((len(l) + 1) / 2 / 2 - 1 + (len(l) + 1) / 2)
        Q3 = l[k]
    elif len(l) % 2 != 0 and (len(l) + 1) / 2 % 2 == 0:
        m = int((len(l) + 1) / 2 / 2 - 1)
        n = int((len(l) + 1) / 2 / 2)
        Q1 = (l[m] + l[n]) / 2
        o = int((len(l) + 1) / 2 / 2 - 2 + (len(l) + 1) / 2)
        p = int((len(l) + 1) / 2 / 2 - 1 + (len(l) + 1) / 2)
        Q3 = (l[o] + l[p]) / 2
    return Q1, Q2, Q3


if __name__ == '__main__':
    assert quartiles([1, 1, 2, 2, 2, 3, 3, 4, 4]) == (2.0, 2.0, 3.0)
    assert quartiles([1, 2, 3, 4, 5, 6]) == (2.0, 3.5, 5.0)
    assert quartiles([1, 2, 3, 4, 5, 6, 7]) == (2.5, 4.0, 5.5)
    assert quartiles([1, 2, 3, 4, 5, 6, 7, 8]) == (2.5, 4.5, 6.5)
    assert quartiles([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (3.0, 5.0, 7.0)
