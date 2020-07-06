def indexString(s, k):
    ds = {}
    position = 0
    while position < len(s):
        substring = s[position] * k
        if s.find(substring, position) != -1:
            if substring in ds.keys():
                ds[substring] += 1
            else:
                ds[substring] = 1
        position += 1
    return ds


def query(ds, q):
    count = ds[q]
    return count


def frequentKmer(s, k, t):
    kmers = set()
    ds = indexString(s, k)
    for substring in ds.keys():
        if query(ds, substring) >= t:
            kmers.add(substring)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    assert frequentKmer('aaabbccdd', 2, 2) == {'aa'}
    assert frequentKmer('aAabbccdd', 2, 2) == set()
    assert frequentKmer('aaabbccdd', 2, 1) == {'aa', 'bb', 'cc', 'dd'}
    assert frequentKmer('aaabbccdd', 2, 3) == set()
    assert frequentKmer('aaabbccdd', 3, 2) == set()
    assert frequentKmer('', 2, 2) == set()
    assert frequentKmer('ababcdcd', 2, 1) == set()
