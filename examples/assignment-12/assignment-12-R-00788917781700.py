def indexString(s, k):
    newlist = []
    e = k
    ds = {}
    for i in range(len(s)):
        res = s[i:e]
        if len(res) == k:
            newlist.append(res)
        e += 1
    for i in newlist:
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
    my_dict = {}
    my_dict = indexString(s, k)
    for key in my_dict:
        if my_dict[key] >= t:
            kmers.append(key)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
