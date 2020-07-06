def indexString(s, k):
    sublist = []
    no_occ = k
    ds = {}
    for i in range(len(s)):
        result = s[i:no_occ]
        if len(result) == k:
            sublist.append(result)
        no_occ += 1
    for i in sublist:
        if i in ds:
            ds[i] += 1
        else:
            ds[i] = 1
    return ds


def query(ds, q):
    for c in ds:
        if c == q:
            count = ds.get(c)
    return count


def frequentKmer(s, k, t):
    kmers = []
    b_dict = {}
    b_dict = indexString(s, k)
    for key in b_dict:
        if b_dict[key] >= t:
            kmers.append(key)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
