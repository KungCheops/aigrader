def indexString(s, k):
    s = s.lower()
    i = 0
    ds = {}
    try:
        while i + k <= len(s):
            str = s[i:i + k]
            i += 1
            if not str in ds.keys():
                ds[str] = 1
            else:
                ds[str] += 1
    except:
        print(f'You need to input an integer, not "{k}"')
    return ds


def query(ds, q):
    try:
        q = q.lower()
        count = ds[q]
        return count
    except:
        print(f'The string "{q}" does not exist')


def frequentKmer(s, k, t):
    s = s.lower()
    try:
        ds = indexString(s, k)
        kmers = [key for key, value in ds.items() if value >= t]
        print(
            f'The substrings of length {k} with more or equal to {t} occurences:'
            )
        print(kmers)
        return kmers
    except:
        print(f'The k and t parameters must be integers')


if __name__ == '__main__':
    s = 'AAASSSDDDSAAA'
    assert indexString(s, 2) == {'aa': 4, 'as': 1, 'ss': 2, 'sd': 1, 'dd': 
        2, 'ds': 1, 'sa': 1}
    assert frequentKmer(s, 2, 2) == ['aa', 'ss', 'dd']
    assert frequentKmer(s, 2, 3) == ['aa']
    assert frequentKmer(s, 2, 4) == ['aa']
    assert frequentKmer(s, 2, 5) == []
    assert indexString('HAAAALLLO', 3) == {'haa': 1, 'aaa': 2, 'aal': 1,
        'all': 1, 'lll': 1, 'llo': 1}
    assert frequentKmer('HAAAALLLO', 3, 2) == ['aaa']
