from collections import defaultdict


def indexString(s, k):
    ds = defaultdict(int)
    if not s or k < 1:
        print('Please enter a valid string and a valid number of characters')
    else:
        s = s.lower()
        for i in range(len(s) - k + 1):
            substring = s[i:i + k]
            ds[substring] += 1
    return ds


def query(ds, q):
    count = 0
    if not q:
        print('Please enter a valid query')
    else:
        q = q.lower()
        count = ds[q]
    return count


def frequentKmer(s, k, t):
    kmers = []
    ds = indexString(s, k)
    for key, val in ds.items():
        if val >= t:
            kmers.append(key)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    assert frequentKmer('AAAAA', 3, 3) == ['aaa']
    assert frequentKmer('abracadabra', 2, 2) == ['ab', 'br', 'ra']
    assert query(indexString('abracadabra', 2), 'ab') == 2
