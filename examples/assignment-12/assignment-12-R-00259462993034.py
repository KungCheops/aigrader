from collections import Counter


def indexString(s, k):
    s = s.lower()
    sub = [s[i:k + i] for i in range(len(s) - k + 1)]
    ds = dict(Counter(sub))
    return ds


def query(ds, q):
    q = q.lower()
    count = 0
    if q in ds:
        count += ds[q]
    return count


def frequentKmer(s, k, t):
    kmers = []
    ss = indexString(s, k)
    for k, v in ss.items():
        if ss[k] >= t:
            kmers.append(k)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
