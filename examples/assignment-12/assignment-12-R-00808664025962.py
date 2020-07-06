def indexString(s, k):
    ds = {}
    for i in range(len(s) - k + 1):
        substr = s[i:i + k]
        if substr in ds.keys():
            ds[substr] += 1
        else:
            ds[substr] = 1
    return ds


def query(ds, q):
    count = 0
    if q in ds.keys():
        count = ds[q]
    return count


def frequentKmer(s, k, t):
    kmers = []
    ds = indexString(s, k)
    for substr in ds:
        if ds[substr] >= t:
            kmers.append(substr)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
