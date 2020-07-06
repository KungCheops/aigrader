def indexString(s, k):
    ds = {}
    for i in range(len(s)):
        key = ''
        for j in range(k):
            if i + j >= len(s):
                break
            nxt = s[i + j]
            key += nxt
        if len(key) != k:
            continue
        if key in ds:
            ds[key] += 1
        else:
            ds[key] = 1
    return ds


def query(ds, q):
    if q not in ds:
        return 0
    count = ds[q]
    return count


def frequentKmer(s, k, t):
    kmers = []
    for k, v in indexString(s, k).items():
        if v >= t:
            kmers.append(k)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    s = 'AAASSSDDDSAAA'
    assert indexString(s, 2) == {'AA': 4, 'AS': 1, 'SS': 2, 'SD': 1, 'DD': 
        2, 'DS': 1, 'SA': 1}
    assert frequentKmer(s, 2, 2) == ['AA', 'SS', 'DD']
    assert frequentKmer(s, 2, 3) == ['AA']
    assert frequentKmer(s, 2, 4) == ['AA']
    assert frequentKmer(s, 2, 5) == []
