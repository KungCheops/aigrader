def indexString(s, k):
    ds = dict()
    s = s.lower()
    for i in range(len(s) - k + 1):
        if s.count(s[i], i, k + i) == k:
            if s[i:k + i] in ds.keys():
                ds[s[i:k + i]] += 1
            else:
                ds.update({s[i:i + k]: 1})
    return ds


def query(ds, q):
    count = 0
    q = q.lower()
    for i in ds.keys():
        if q == i:
            count = ds.get(i)
    return count


def frequentKmer(s, k, t):
    ds = dict()
    s = s.lower()
    kmers = []
    for i in range(len(s) - k + 1):
        if s.count(s[i], i, k + i) == k:
            if s[i:k + i] in ds.keys():
                ds[s[i:k + i]] += 1
            else:
                ds.update({s[i:i + k]: 1})
    for j in ds.keys():
        if t <= ds[j]:
            kmers.append(j)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
