def indexString(s, k):
    ds = {}
    stillequal = True
    if k == 0:
        return ds
    for i in range(len(s) - k + 1):
        for j in range(k):
            if s[i] != s[i + j]:
                stillequal = False
        if stillequal:
            if s[i] in ds:
                ds[s[i]] += 1
            else:
                ds[s[i]] = 1
        stillequal = True
    return ds


def query(ds, q):
    count = ds[q[0]]
    return count


def frequentKmer(s, k, t):
    kmers = []
    cons_chars = indexString(s, k)
    for char in cons_chars:
        if cons_chars[char] >= t:
            kmers.append(k * char)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
