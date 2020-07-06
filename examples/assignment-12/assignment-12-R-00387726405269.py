def indexString(s, k):
    ds = {}
    for i in range(len(s) - k + 1):
        if s[i:i + k] in ds.keys():
            ds[s[i:i + k]] += 1
        else:
            ds[s[i:i + k]] = 1
    return ds


def query(ds, q):
    if q in ds:
        count = ds[q]
    else:
        count = 0
    return count


def frequentKmer(s, k, t):
    kmers = []
    for i in indexString(s, k).keys():
        if indexString(s, k)[i] >= t:
            kmers.append(i)
    return kmers


if __name__ == '__main__':
    assert query(indexString('AAAAA', 3), 'AAA') == 3
    assert indexString('HAAAALLLO', 3) == {'HAA': 1, 'AAA': 2, 'AAL': 1,
        'ALL': 1, 'LLL': 1, 'LLO': 1}
    assert frequentKmer('HAAAALLLO', 3, 2) == ['AAA']
