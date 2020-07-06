from collections import Counter
from itertools import groupby


def indexString(s, k):
    ds = []
    for i, c in enumerate(s):
        if i < len(s) - k + 1:
            ds.append(s[i:i + k])
    result = Counter(ds)
    return result


def query(ds, q):
    return ds[q]


def frequentKmer(s, k, t):
    kmer = []
    freq = indexString(s, k)
    for f, i in freq.items():
        if i >= t:
            kmer.append(f)
    return kmer


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
