def indexString(s, k):
    ds = {}
    for i in range(len(s)):
        pattern = ''
        for j in range(k):
            if i + j >= len(s):
                break
            character = s[i + j]
            pattern += character
        if len(pattern) != k:
            continue
        if pattern in ds:
            ds[pattern] += 1
        else:
            ds[pattern] = 1
    return ds


def query(ds, q):
    if q not in ds:
        print('Not found')
        return 0
    count = ds[q]
    return count


def frequentKmer(s, k, t):
    kmer = []
    for k, l in indexString(s, k).items():
        if l >= t:
            kmers.append(k)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    assert query(indexString('NILSSS', 2), 'SS') == 2
    assert query(indexString('LLAAAAAAAALL', 2), 'LL') == 2
