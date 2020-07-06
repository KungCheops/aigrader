def indexString(s, k):
    if not s or not k:
        return None
    if len(s) == 0:
        return None
    if k == 0:
        return None
    i = 0
    ds = []
    while i < len(s) - k + 1:
        a = s[i:i + k]
        ds.append(a)
        i += 1
    return ds


def query(ds, q):
    if not ds or not q:
        return None
    count = 0
    for d in ds:
        if d == q:
            count = count + 1
    return count


def frequentKmer(s, k, t):
    kmers = []
    listofKmers = indexString(s, k)
    for k in listofKmers:
        if listofKmers.count(k) >= t:
            if k not in kmers:
                kmers.append(k)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    assert query(indexString('LaLa Laannd', 2), 'La') == 3
    assert query(indexString('LaLa Laannd', 2), None) is None
    assert frequentKmer('ATTTGGACCTCCGGGTATATA', 2, 3) == ['AT', 'GG', 'TA']
