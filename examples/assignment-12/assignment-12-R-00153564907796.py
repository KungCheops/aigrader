def indexString(s, k):
    l = []
    for i in range(0, len(s) - k + 1):
        l.append(s[i:i + k])
    ds = {}
    for i in l:
        if i in ds:
            ds[i] = ds[i] + 1
        else:
            ds[i] = 1
    return ds


def query(ds, q):
    if q in ds:
        count = ds[q]
    else:
        print(q, 'is not in ', s)
    return count


def frequentKmer(s, k, t):
    ds = indexString(s, k)
    kmers = []
    for key, value in ds.items():
        if value >= t:
            kmers.append(key)
    if len(kmers) == 0:
        print('There is no substring with occurence', t)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAA', 3), 'AAA') == 2
