from collections import defaultdict


def indexString(s, k):
    if type(s) != str or type(k) != int:
        raise TypeError('s should be a string and k should be an integer')
    ds = defaultdict(int)
    for i in range(len(s)):
        if len(s[i:i + k]) == k:
            ds[s[i:i + k]] = ds[s[i:i + k]] + 1
    return ds


def query(ds, q):
    count = ds[q]
    return count


def frequentKmer(s, k, t):
    kmers = []
    ds = indexString(s, k)
    for key in ds:
        if query(ds, key) >= t:
            kmers.append(key)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    assert len(indexString('mississippi', 2)) == 7
    assert frequentKmer('mississippi', 2, 2) == ['is', 'ss', 'si']
