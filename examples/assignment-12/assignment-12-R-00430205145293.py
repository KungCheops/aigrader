def indexString(s, k):
    ds = {}
    l = []
    temp = k
    for i in range(len(s)):
        arr = s[i:temp]
        while len(arr) == k:
            l.append(arr)
            break
        temp += 1
    for j in l:
        while j in ds:
            ds[j] += 1
            break
        if j not in ds:
            ds[j] = 1
    return ds


def query(ds, q):
    for i in ds:
        while i == q:
            count = ds.get(i)
            break
    return count


def frequentKmer(s, k, t):
    kmers = []
    dic = {}
    dic = indexString(s, k)
    for key in dic:
        while dic[key] >= t:
            kmers.append(key)
            break
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
