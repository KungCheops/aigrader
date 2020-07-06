def indexString(s, k):
    if not s or k > len(s):
        return None
    ds = dict()
    s = list(s)
    for i in range(0, len(s) - k + 1):
        c = ''.join(s[i:i + k])
        ds[c] = ds.get(c, 0) + 1
    return ds


def query(ds, q):
    count = ds.get(q, 0) if q else None
    return count


def frequentKmer(s, k, t):
    kmers = [x for x, y in indexString(s, k).items() if y >= t]
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    assert indexString('mississippi', 2) == {'mi': 1, 'is': 2, 'ss': 2,
        'si': 2, 'ip': 1, 'pp': 1, 'pi': 1}
    assert indexString('', 2) is None
    assert indexString('mississippi', 500) is None
    assert query(indexString('mississippi', 2), 'ss') == 2
    assert query(indexString('mississippi', 2), 'pp') == 1
    assert query(indexString('mississippi', 2), '_') == 0
    assert query(indexString('mississippi', 2), '') is None
    assert query(indexString('all', 2), 'll') == 1
    assert query(indexString('all', 1), 'l') == 2
    assert frequentKmer('mississippi', 2, 2) == ['is', 'ss', 'si']
    assert frequentKmer('mississippi', 2, 500) == []
