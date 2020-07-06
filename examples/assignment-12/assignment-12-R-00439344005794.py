def indexString(s, k):
    ds = {}
    substring = [s[i:i + k] for i in range(len(s) - k + 1)]
    for i in substring:
        ds[i] = substring.count(i)
    return ds


def query(ds, q):
    count = ds[q]
    return count


def frequentKmer(s, k, t):
    Substring = list()
    ds = {}
    kmers = list()
    ds = indexString(s, k)
    for i in ds:
        if ds[i] >= t:
            kmers.append(i)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
