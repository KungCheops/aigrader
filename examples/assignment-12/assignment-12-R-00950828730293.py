def indexString(s, k):
    s = s.upper()
    ds = {}
    a = ''
    c = 0
    for i in range(len(s) - k + 1):
        for j in range(k):
            a = a + s[i + c]
            c = c + 1
        if a in ds:
            ds[a] = ds[a] + 1
        else:
            ds[a] = 1
        a = ''
        c = 0
    return ds


def query(ds, q):
    q = q.upper()
    count = ds[q]
    return count


def frequentKmer(s, k, t):
    kmers = []
    ds = indexString(s, k)
    for key, value in ds.items():
        if query(ds, key) >= t:
            kmers.append(key)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    assert query(indexString('aaccaac', 3), 'aAC') == 2
    assert frequentKmer('aattaacttgtggggttgaaacc', 3, 2) == ['AAC', 'TTG',
        'GGG']
