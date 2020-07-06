def indexString(s, k):
    ds = {}
    for i in range(len(s) - k + 1):
        if s[i:i + k] in ds.keys():
            ds[s[i:i + k]] += 1
        else:
            ds[s[i:i + k]] = 1
    return ds


def query(ds, q):
    if q in ds:
        count = ds[q]
    else:
        count = 0
    return count


def frequentKmer(s, k, t):
    kmers = []
    for k, v in indexString(s, k).items():
        if v >= t:
            kmers.appends(k)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
